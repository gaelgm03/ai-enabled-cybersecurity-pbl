"""
Developer-friendly Security Report Generator (Week 4).

Generates comprehensive security_report.md with:
- Executive summary
- Findings grouped by category
- Intent, attack surface, risk analysis for each finding
- Redacted evidence and recommended fixes

MIT Blended AI+X PBL - AI-Enabled Cybersecurity
"""

from pathlib import Path
from typing import Optional, Dict, Any, List, Union
from datetime import datetime, timezone

from ..schema import ScanReport, Finding, FindingType, Severity


class SecurityReporter:
    """Generates developer-friendly security reports."""
    
    SEVERITY_LABELS = {
        Severity.CRITICAL: ("🔴 CRITICAL", "Requires immediate attention"),
        Severity.HIGH: ("🟠 HIGH", "Should be addressed soon"),
        Severity.MEDIUM: ("🟡 MEDIUM", "Address in normal development cycle"),
        Severity.LOW: ("🟢 LOW", "Consider addressing when convenient"),
    }
    
    CATEGORY_INFO = {
        FindingType.SECRET: {
            "icon": "🔐",
            "title": "Exposed Secrets & Credentials",
            "description": "Hardcoded credentials, API keys, or other sensitive data found in source code.",
            "general_risk": "Exposed secrets can lead to unauthorized access, data breaches, and account compromise.",
        },
        FindingType.SQLI: {
            "icon": "💉",
            "title": "SQL Injection Patterns",
            "description": "Code patterns that may be vulnerable to SQL injection attacks.",
            "general_risk": "SQL injection can allow attackers to read, modify, or delete database contents.",
        },
        FindingType.DEPENDENCY: {
            "icon": "📦",
            "title": "Vulnerable Dependencies",
            "description": "Third-party packages with known security vulnerabilities.",
            "general_risk": "Vulnerable dependencies can be exploited to compromise the application.",
        },
        FindingType.TYPO: {
            "icon": "📝",
            "title": "Typos & Code Quality",
            "description": "Spelling errors that may indicate code quality issues or cause bugs.",
            "general_risk": "Typos can cause subtle bugs and reduce code maintainability.",
        },
    }
    
    def __init__(
        self,
        report: ScanReport,
        target_name: str = "",
        metadata: Optional[Dict[str, Any]] = None,
        commit_hash: Optional[str] = None
    ):
        self.report = report
        self.target_name = target_name or report.target_path
        self.metadata = metadata or {}
        self.commit_hash = commit_hash
    
    def generate(self) -> str:
        """Generate the complete security report."""
        self.report.compute_summary()
        
        sections = [
            self._generate_header(),
            self._generate_executive_summary(),
            self._generate_severity_guide(),
            self._generate_findings_overview(),
            self._generate_detailed_findings(),
            self._generate_recommendations(),
            self._generate_footer(),
        ]
        
        return "\n".join(sections)
    
    def _generate_header(self) -> str:
        """Generate report header."""
        lines = [
            "# Security Analysis Report",
            "",
            f"**Target:** `{self.target_name}`  ",
            f"**Scan Date:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC  ",
            f"**Scan ID:** `{self.report.scan_id}`",
        ]
        
        if self.commit_hash:
            lines.append(f"**Commit:** `{self.commit_hash}`")
        
        if self.metadata:
            if self.metadata.get("language"):
                lines.append(f"**Primary Language:** {self.metadata['language']}")
            if self.metadata.get("stargazers_count"):
                lines.append(f"**GitHub Stars:** {self.metadata['stargazers_count']:,}")
        
        lines.extend(["", "---", ""])
        return "\n".join(lines)
    
    def _generate_executive_summary(self) -> str:
        """Generate executive summary section."""
        total = self.report.summary.get("total_findings", 0)
        by_severity = self.report.summary.get("by_severity", {})
        by_type = self.report.summary.get("by_type", {})
        
        critical = by_severity.get("critical", 0)
        high = by_severity.get("high", 0)
        medium = by_severity.get("medium", 0)
        low = by_severity.get("low", 0)
        
        # Determine overall risk level
        if critical > 0:
            risk_level = "🔴 **CRITICAL** - Immediate action required"
        elif high > 0:
            risk_level = "🟠 **HIGH** - Significant issues found"
        elif medium > 0:
            risk_level = "🟡 **MEDIUM** - Some issues to address"
        elif low > 0:
            risk_level = "🟢 **LOW** - Minor issues only"
        else:
            risk_level = "✅ **CLEAN** - No issues detected"
        
        lines = [
            "## Executive Summary",
            "",
            f"**Overall Risk Level:** {risk_level}",
            "",
            f"This security scan analyzed `{self.target_name}` and identified **{total} potential security issues**.",
            "",
        ]
        
        if total > 0:
            lines.extend([
                "### Findings by Severity",
                "",
                "| Severity | Count | Action Required |",
                "|----------|-------|-----------------|",
            ])
            
            if critical > 0:
                lines.append(f"| 🔴 Critical | {critical} | Immediate |")
            if high > 0:
                lines.append(f"| 🟠 High | {high} | Soon |")
            if medium > 0:
                lines.append(f"| 🟡 Medium | {medium} | Normal cycle |")
            if low > 0:
                lines.append(f"| 🟢 Low | {low} | When convenient |")
            
            lines.extend(["", "### Findings by Category", ""])
            
            for ftype_str, count in by_type.items():
                try:
                    ftype = FindingType(ftype_str)
                    info = self.CATEGORY_INFO.get(ftype, {})
                    icon = info.get("icon", "•")
                    title = info.get("title", ftype_str.capitalize())
                    lines.append(f"- {icon} **{title}**: {count} issue(s)")
                except ValueError:
                    lines.append(f"- **{ftype_str.capitalize()}**: {count} issue(s)")
        else:
            lines.append("*No security issues were detected in this scan.*")
        
        lines.extend(["", "---", ""])
        return "\n".join(lines)
    
    def _generate_severity_guide(self) -> str:
        """Generate severity rating guide."""
        lines = [
            "## Severity Rating Guide",
            "",
            "| Level | Meaning | Response Time |",
            "|-------|---------|---------------|",
            "| 🔴 Critical | Exploitable vulnerability with severe impact | Immediate (hours) |",
            "| 🟠 High | Serious issue requiring prompt attention | Days |",
            "| 🟡 Medium | Moderate risk, should be planned | Weeks |",
            "| 🟢 Low | Minor issue, low risk | When convenient |",
            "",
            "---",
            "",
        ]
        return "\n".join(lines)
    
    def _generate_findings_overview(self) -> str:
        """Generate findings overview table."""
        if not self.report.findings:
            return ""
        
        lines = [
            "## Findings Overview",
            "",
            "| # | Severity | Category | Title | Location |",
            "|---|----------|----------|-------|----------|",
        ]
        
        for i, finding in enumerate(self.report.findings, 1):
            sev_label = self._severity_icon(finding.severity)
            category = self._category_name(finding.finding_type)
            title = finding.title[:40] + "..." if len(finding.title) > 40 else finding.title
            location = self._format_location(finding)
            
            lines.append(f"| {i} | {sev_label} | {category} | {title} | `{location}` |")
        
        lines.extend(["", "---", ""])
        return "\n".join(lines)
    
    def _generate_detailed_findings(self) -> str:
        """Generate detailed findings by category."""
        if not self.report.findings:
            return ""
        
        # Group findings by type
        by_type: Dict[FindingType, List[Finding]] = {}
        for finding in self.report.findings:
            ftype = finding.finding_type
            if ftype not in by_type:
                by_type[ftype] = []
            by_type[ftype].append(finding)
        
        lines = ["## Detailed Findings", ""]
        
        # Process in priority order
        type_order = [FindingType.SECRET, FindingType.SQLI, FindingType.DEPENDENCY, FindingType.TYPO]
        
        for ftype in type_order:
            if ftype not in by_type:
                continue
            
            findings = by_type[ftype]
            info = self.CATEGORY_INFO.get(ftype, {})
            
            lines.extend([
                f"### {info.get('icon', '•')} {info.get('title', ftype.value.capitalize())}",
                "",
                f"*{info.get('description', '')}*",
                "",
            ])
            
            for i, finding in enumerate(findings, 1):
                lines.extend(self._format_finding(finding, i))
        
        return "\n".join(lines)
    
    def _format_finding(self, finding: Finding, index: int) -> List[str]:
        """Format a single finding with full details."""
        sev_label, sev_desc = self.SEVERITY_LABELS.get(
            finding.severity, 
            ("Unknown", "Review manually")
        )
        
        lines = [
            f"#### {index}. {finding.title}",
            "",
            f"**Severity:** {sev_label}  ",
            f"**Detector:** `{finding.detector}`",
            "",
        ]
        
        # Location / Evidence
        lines.append("**Evidence:**")
        lines.append("")
        location = self._format_location(finding)
        lines.append(f"- **File:** `{location}`")
        
        if finding.redacted_match and finding.finding_type != FindingType.TYPO:
            lines.append(f"- **Match (redacted):** `{finding.redacted_match}`")
        
        lines.append("")
        
        # Intent - what the code appears to be doing
        lines.append("**Intent:**")
        lines.append("")
        lines.append(self._infer_intent(finding))
        lines.append("")
        
        # Attack Surface - where user input enters
        lines.append("**Attack Surface:**")
        lines.append("")
        lines.append(self._analyze_attack_surface(finding))
        lines.append("")
        
        # Risk - impact and likelihood
        lines.append("**Risk Assessment:**")
        lines.append("")
        lines.append(self._assess_risk(finding))
        lines.append("")
        
        # Recommended Fix
        lines.append("**Recommended Fix:**")
        lines.append("")
        if finding.remediation:
            lines.append(finding.remediation)
        else:
            lines.append(self._suggest_fix(finding))
        lines.append("")
        
        # Verification
        lines.append("**Verification:**")
        lines.append("")
        lines.append(self._suggest_verification(finding))
        lines.append("")
        
        lines.extend(["---", ""])
        
        return lines
    
    def _severity_icon(self, severity: Severity) -> str:
        """Get icon for severity level."""
        icons = {
            Severity.CRITICAL: "🔴",
            Severity.HIGH: "🟠",
            Severity.MEDIUM: "🟡",
            Severity.LOW: "🟢",
        }
        return icons.get(severity, "•")
    
    def _category_name(self, ftype: FindingType) -> str:
        """Get display name for category."""
        names = {
            FindingType.SECRET: "Secret",
            FindingType.SQLI: "SQLi",
            FindingType.DEPENDENCY: "Dependency",
            FindingType.TYPO: "Typo",
        }
        return names.get(ftype, ftype.value)
    
    def _format_location(self, finding: Finding) -> str:
        """Format file location string."""
        if not finding.file_path:
            return "N/A"
        
        # Get relative path if possible
        path = finding.file_path
        if self.report.target_path and path.startswith(self.report.target_path):
            path = path[len(self.report.target_path):].lstrip("/\\")
        
        if finding.line_number:
            return f"{path}:{finding.line_number}"
        return path
    
    def _infer_intent(self, finding: Finding) -> str:
        """Infer the intent of the code that triggered the finding."""
        ftype = finding.finding_type
        meta = finding.metadata or {}
        
        if ftype == FindingType.SECRET:
            secret_type = meta.get("secret_type", "credential")
            return (f"The code appears to store a {secret_type} for authentication or API access. "
                    f"This is likely used to connect to an external service.")
        
        elif ftype == FindingType.SQLI:
            pattern_type = meta.get("pattern_type", "query construction")
            return (f"The code constructs a SQL query using {pattern_type}. "
                    f"This is used for database operations but may be unsafe.")
        
        elif ftype == FindingType.DEPENDENCY:
            pkg = meta.get("package", "package")
            return (f"The project depends on `{pkg}` for functionality. "
                    f"This dependency has known security vulnerabilities.")
        
        elif ftype == FindingType.TYPO:
            return (f"A spelling error was detected in the code. "
                    f"This may be in comments, strings, or identifiers.")
        
        return "Review the code context to understand its purpose."
    
    def _analyze_attack_surface(self, finding: Finding) -> str:
        """Analyze the attack surface for a finding."""
        ftype = finding.finding_type
        meta = finding.metadata or {}
        
        if ftype == FindingType.SECRET:
            return ("- **Entry Point:** Anyone with access to the source code repository\n"
                    "- **Exposure:** The secret value may be in version control history\n"
                    "- **Reach:** If leaked, attackers can use the credential to access external services")
        
        elif ftype == FindingType.SQLI:
            return ("- **Entry Point:** User-controlled input (form fields, URL parameters, API data)\n"
                    "- **Flow:** Input flows into SQL query without proper sanitization\n"
                    "- **Reach:** Database server - attackers may read, modify, or delete data")
        
        elif ftype == FindingType.DEPENDENCY:
            vuln_id = meta.get("vuln_id", "")
            return (f"- **Entry Point:** Varies by vulnerability (see {vuln_id})\n"
                    "- **Exposure:** Any functionality using the vulnerable package\n"
                    "- **Reach:** Depends on vulnerability type - may allow RCE, data access, or DoS")
        
        elif ftype == FindingType.TYPO:
            return ("- **Entry Point:** N/A (code quality issue)\n"
                    "- **Exposure:** May cause confusion or subtle bugs\n"
                    "- **Reach:** Limited security impact, mainly affects maintainability")
        
        return "- Review the specific code context to assess attack surface"
    
    def _assess_risk(self, finding: Finding) -> str:
        """Assess risk for a finding."""
        ftype = finding.finding_type
        sev = finding.severity
        meta = finding.metadata or {}
        
        impact = {
            Severity.CRITICAL: "Severe - Full system compromise possible",
            Severity.HIGH: "Significant - Data breach or service disruption",
            Severity.MEDIUM: "Moderate - Limited data exposure or functionality impact",
            Severity.LOW: "Minimal - Code quality or minor information disclosure",
        }.get(sev, "Unknown")
        
        likelihood = "Medium"  # Default
        
        if ftype == FindingType.SECRET:
            if sev in [Severity.CRITICAL, Severity.HIGH]:
                likelihood = "High - Secrets in code are easily discovered"
        elif ftype == FindingType.SQLI:
            likelihood = "High if user input reaches the query, Low if internal only"
        elif ftype == FindingType.DEPENDENCY:
            likelihood = "Varies - Check if vulnerable code path is reachable"
        elif ftype == FindingType.TYPO:
            likelihood = "Low - Unlikely to cause security issues"
        
        return f"- **Impact:** {impact}\n- **Likelihood:** {likelihood}"
    
    def _suggest_fix(self, finding: Finding) -> str:
        """Suggest a fix for the finding."""
        ftype = finding.finding_type
        meta = finding.metadata or {}
        
        if ftype == FindingType.SECRET:
            return ("1. **Remove** the hardcoded secret from the source code\n"
                    "2. **Rotate** the exposed credential immediately\n"
                    "3. **Use** environment variables or a secrets manager\n"
                    "4. **Audit** version control history for the exposed value")
        
        elif ftype == FindingType.SQLI:
            return ("1. **Use parameterized queries** instead of string concatenation\n"
                    "2. **Use ORM methods** that handle escaping automatically\n"
                    "3. **Validate** and sanitize all user input\n"
                    "4. **Apply** least-privilege database permissions")
        
        elif ftype == FindingType.DEPENDENCY:
            fix_versions = meta.get("fix_versions", [])
            if fix_versions:
                return (f"1. **Upgrade** to a fixed version: {', '.join(fix_versions)}\n"
                        "2. **Test** the application after upgrading\n"
                        "3. **Monitor** for future vulnerability disclosures")
            return ("1. **Check** for available patches or updates\n"
                    "2. **Consider** alternative packages if no fix available\n"
                    "3. **Assess** if the vulnerable functionality is used")
        
        elif ftype == FindingType.TYPO:
            suggestion = meta.get("suggestion", "")
            if suggestion:
                return f"Replace with the correct spelling: `{suggestion}`"
            return "Review and correct the spelling error"
        
        return "Review the finding and apply appropriate remediation"
    
    def _suggest_verification(self, finding: Finding) -> str:
        """Suggest how to verify the fix."""
        ftype = finding.finding_type
        
        if ftype == FindingType.SECRET:
            return ("- Re-run the security scanner to confirm removal\n"
                    "- Verify the old credential no longer provides access\n"
                    "- Check git history was cleaned if necessary")
        
        elif ftype == FindingType.SQLI:
            return ("- Write a unit test with malicious input (e.g., `' OR '1'='1`)\n"
                    "- Use a SQL injection scanner on the endpoint\n"
                    "- Code review the fix with security team")
        
        elif ftype == FindingType.DEPENDENCY:
            return ("- Run `pip-audit` or `npm audit` after updating\n"
                    "- Verify application functionality is intact\n"
                    "- Check dependency tree for transitive vulnerabilities")
        
        elif ftype == FindingType.TYPO:
            return ("- Run codespell or similar tool to verify fix\n"
                    "- Ensure no new typos were introduced")
        
        return "- Re-run scanner to verify the issue is resolved"
    
    def _generate_recommendations(self) -> str:
        """Generate general recommendations section."""
        lines = [
            "## General Recommendations",
            "",
            "### Immediate Actions",
            "",
        ]
        
        has_secrets = any(f.finding_type == FindingType.SECRET for f in self.report.findings)
        has_sqli = any(f.finding_type == FindingType.SQLI for f in self.report.findings)
        has_deps = any(f.finding_type == FindingType.DEPENDENCY for f in self.report.findings)
        
        actions = []
        if has_secrets:
            actions.append("1. **Rotate all exposed secrets** - Assume they are compromised")
        if has_sqli:
            actions.append("2. **Review SQL injection patterns** - Prioritize user-facing endpoints")
        if has_deps:
            actions.append("3. **Update vulnerable dependencies** - Apply security patches")
        
        if actions:
            lines.extend(actions)
        else:
            lines.append("*No critical immediate actions required.*")
        
        lines.extend([
            "",
            "### Preventive Measures",
            "",
            "- **Pre-commit hooks**: Use gitleaks or similar to prevent secret commits",
            "- **CI/CD scanning**: Integrate security scanning into the build pipeline",
            "- **Dependency monitoring**: Use Dependabot or Snyk for continuous monitoring",
            "- **Code review**: Include security review in the PR process",
            "- **Developer training**: Educate team on secure coding practices",
            "",
            "---",
            "",
        ])
        
        return "\n".join(lines)
    
    def _generate_footer(self) -> str:
        """Generate report footer."""
        lines = [
            "## About This Report",
            "",
            "This security report was generated by the **AI-Enabled Cybersecurity Scanner** "
            "developed as part of the MIT Blended AI+X Program (Track 3).",
            "",
            "### Limitations",
            "",
            "- This is a **static analysis** tool and may produce false positives",
            "- Not all vulnerabilities can be detected through pattern matching",
            "- Human review is essential for accurate risk assessment",
            "- This tool does **not** exploit or test vulnerabilities",
            "",
            "### Responsible Disclosure",
            "",
            "If this scan revealed potential vulnerabilities in third-party software:",
            "",
            "1. Do **NOT** publicly disclose specific vulnerability details",
            "2. Contact the maintainers privately through their security policy",
            "3. Allow reasonable time for patches before any disclosure",
            "4. Follow the project's responsible disclosure guidelines",
            "",
            "---",
            "",
            f"*Report generated on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC*  ",
            "*MIT Blended AI+X PBL - AI-Enabled Cybersecurity*",
        ]
        
        return "\n".join(lines)
    
    def save(self, output_path: Union[str, Path]) -> Path:
        """Save the security report to a file."""
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        content = self.generate()
        path.write_text(content, encoding="utf-8")
        
        return path
