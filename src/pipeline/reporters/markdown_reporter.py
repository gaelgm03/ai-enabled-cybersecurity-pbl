"""
Markdown report generator.
"""

from pathlib import Path
from typing import Union
from datetime import datetime, timezone

from ..schema import ScanReport, FindingType, Severity


class MarkdownReporter:
    """Generates Markdown reports from scan results."""
    
    SEVERITY_ICONS = {
        Severity.CRITICAL: "🔴",
        Severity.HIGH: "🟠",
        Severity.MEDIUM: "🟡",
        Severity.LOW: "🟢",
    }
    
    TYPE_ICONS = {
        FindingType.SECRET: "🔐",
        FindingType.TYPO: "📝",
        FindingType.DEPENDENCY: "📦",
        FindingType.SQLI: "💉",
    }
    
    def __init__(self, report: ScanReport):
        self.report = report
    
    def generate(self) -> str:
        """Generate Markdown report."""
        self.report.compute_summary()
        
        lines = [
            "# Security Scan Report",
            "",
            f"**Scan ID:** `{self.report.scan_id}`  ",
            f"**Timestamp:** {self.report.timestamp}  ",
            f"**Target:** `{self.report.target_path}`",
            "",
            "---",
            "",
            "## Summary",
            "",
            f"**Total Findings:** {self.report.summary['total_findings']}",
            "",
        ]
        
        # By severity
        if self.report.summary.get("by_severity"):
            lines.append("### By Severity")
            lines.append("")
            lines.append("| Severity | Count |")
            lines.append("|----------|-------|")
            for sev in ["critical", "high", "medium", "low"]:
                count = self.report.summary["by_severity"].get(sev, 0)
                if count > 0:
                    icon = self.SEVERITY_ICONS.get(Severity(sev), "")
                    lines.append(f"| {icon} {sev.capitalize()} | {count} |")
            lines.append("")
        
        # By type
        if self.report.summary.get("by_type"):
            lines.append("### By Type")
            lines.append("")
            lines.append("| Type | Count |")
            lines.append("|------|-------|")
            for ftype, count in self.report.summary["by_type"].items():
                icon = self.TYPE_ICONS.get(FindingType(ftype), "")
                lines.append(f"| {icon} {ftype.capitalize()} | {count} |")
            lines.append("")
        
        lines.append("---")
        lines.append("")
        
        # Detailed findings
        lines.append("## Findings")
        lines.append("")
        
        if not self.report.findings:
            lines.append("*No issues detected.*")
        else:
            # Group by type
            by_type = {}
            for finding in self.report.findings:
                ftype = finding.finding_type
                if ftype not in by_type:
                    by_type[ftype] = []
                by_type[ftype].append(finding)
            
            # Output each type
            for ftype in [FindingType.SECRET, FindingType.SQLI, FindingType.DEPENDENCY, FindingType.TYPO]:
                if ftype in by_type:
                    icon = self.TYPE_ICONS.get(ftype, "")
                    lines.append(f"### {icon} {ftype.value.capitalize()} Issues")
                    lines.append("")
                    
                    for i, finding in enumerate(by_type[ftype], 1):
                        sev_icon = self.SEVERITY_ICONS.get(finding.severity, "")
                        lines.append(f"#### {i}. {finding.title}")
                        lines.append("")
                        lines.append(f"- **Severity:** {sev_icon} {finding.severity.value.capitalize()}")
                        lines.append(f"- **Detector:** `{finding.detector}`")
                        
                        if finding.file_path:
                            loc = finding.file_path
                            if finding.line_number:
                                loc += f":{finding.line_number}"
                            lines.append(f"- **Location:** `{loc}`")
                        
                        if finding.redacted_match and finding.finding_type != FindingType.TYPO:
                            lines.append(f"- **Match (redacted):** `{finding.redacted_match}`")
                        
                        lines.append("")
                        lines.append(f"**Description:** {finding.description}")
                        lines.append("")
                        
                        # Remediation (if present)
                        if finding.remediation:
                            lines.append("**Remediation:**")
                            lines.append("")
                            lines.append(finding.remediation)
                            lines.append("")
                        
                        # Prevention (if present)
                        if finding.prevention:
                            lines.append("**Prevention:**")
                            lines.append("")
                            lines.append(finding.prevention)
                            lines.append("")
                        
                        # Metadata for dependencies
                        if finding.finding_type == FindingType.DEPENDENCY:
                            meta = finding.metadata
                            if meta.get("vuln_id"):
                                lines.append(f"- **CVE/ID:** `{meta['vuln_id']}`")
                            if meta.get("installed_version"):
                                lines.append(f"- **Installed Version:** `{meta['installed_version']}`")
                            if meta.get("fix_versions"):
                                lines.append(f"- **Fix Versions:** {', '.join(meta['fix_versions'])}")
                            lines.append("")
                        
                        # Metadata for typos
                        if finding.finding_type == FindingType.TYPO:
                            meta = finding.metadata
                            if meta.get("suggestion"):
                                lines.append(f"- **Suggestion:** `{meta['suggestion']}`")
                            lines.append("")
                        
                        lines.append("---")
                        lines.append("")
        
        # Footer
        lines.append("## Notes")
        lines.append("")
        lines.append("- All secrets are **redacted** in this report for safety.")
        lines.append("- Remediation instructions are AI-generated and should be reviewed by a human.")
        lines.append("- This report is generated for educational purposes (MIT AI+X PBL).")
        lines.append("")
        lines.append(f"*Report generated on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC*")
        
        return "\n".join(lines)
    
    def save(self, output_path: Union[str, Path]) -> Path:
        """Save Markdown report to file."""
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        content = self.generate()
        path.write_text(content, encoding="utf-8")
        
        return path
