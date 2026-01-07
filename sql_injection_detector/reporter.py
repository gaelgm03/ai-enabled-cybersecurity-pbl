"""Reporter module for SQL Injection Detector output formatting."""

import json
from dataclasses import asdict
from datetime import datetime
from typing import Dict, List, Any

from .detectors.base import Finding, FileResult


class Reporter:
    """Reporter for generating scan results in various formats.

    Collects findings from multiple detectors and generates formatted
    reports in JSON or human-readable text format, aggregated by file.
    """

    def __init__(self):
        """Initialize the reporter."""
        self._file_findings: Dict[str, List[Finding]] = {}
        self._detectors_run: List[str] = []
        self._scan_start: datetime = datetime.now()

    def add_findings(self, file_path: str, findings: List[Finding]) -> None:
        """Add findings for a file.

        Args:
            file_path: Path to the scanned file.
            findings: List of findings from all detectors for this file.
        """
        if file_path not in self._file_findings:
            self._file_findings[file_path] = []
        self._file_findings[file_path].extend(findings)

    def add_detector_run(self, name: str) -> None:
        """Track that a detector was run.

        Args:
            name: Name of the detector that was run.
        """
        if name not in self._detectors_run:
            self._detectors_run.append(name)

    def _get_file_results(self) -> List[FileResult]:
        """Generate FileResult for each scanned file.

        Returns:
            List of FileResult objects, one per file.
        """
        results = []
        for file_path in sorted(self._file_findings.keys()):
            findings = self._file_findings[file_path]
            status = "VULNERABLE" if findings else "CLEAN"
            results.append(FileResult(
                file=file_path,
                status=status,
                findings=findings,
            ))
        return results

    def _get_summary(self) -> Dict[str, Any]:
        """Generate scan summary statistics.

        Returns:
            Dictionary with scan summary data.
        """
        all_findings = []
        for findings in self._file_findings.values():
            all_findings.extend(findings)

        total_findings = len(all_findings)

        severity_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
        for finding in all_findings:
            severity = finding.severity.upper()
            if severity in severity_counts:
                severity_counts[severity] += 1

        return {
            "timestamp": self._scan_start.isoformat(),
            "files_scanned": len(self._file_findings),
            "total_findings": total_findings,
            "severity_breakdown": severity_counts,
            "detectors_run": self._detectors_run,
        }

    def to_json(self) -> str:
        """Generate full structured JSON report.

        Returns:
            JSON string with complete scan results.
        """
        file_results = self._get_file_results()

        report = {
            "scan_summary": self._get_summary(),
            "results": [],
        }

        for result in file_results:
            result_dict = {
                "file": result.file,
                "status": result.status,
                "findings": [asdict(f) for f in result.findings],
            }
            report["results"].append(result_dict)

        return json.dumps(report, indent=2)

    def to_text(self) -> str:
        """Generate human-readable text report.

        Returns:
            Formatted text string with scan results.
        """
        lines = []
        summary = self._get_summary()
        file_results = self._get_file_results()

        # Header
        lines.append("=" * 60)
        lines.append("SQL INJECTION DETECTOR REPORT")

        # Summary
        lines.append("SCAN SUMMARY")
        lines.append(f"Timestamp:       {summary['timestamp']}")
        lines.append(f"Files Scanned:   {summary['files_scanned']}")
        lines.append(f"Total Findings:  {summary['total_findings']}")
        lines.append(f"Detectors Run:   {', '.join(summary['detectors_run'])}")
        lines.append("=" * 60)

        # Results by file
        lines.append("RESULTS BY FILE")

        for result in file_results:
            lines.append("")
            lines.append(f"[{result.status}] {result.file}")

            if not result.findings:
                lines.append("  No vulnerabilities detected.")
            else:
                for i, finding in enumerate(result.findings, 1):
                    lines.append(f"  Finding #{i}")
                    lines.append(f"    Detector:    {finding.detector}")
                    lines.append(f"    Type:        {finding.subtype}")
                    lines.append(f"    Severity:    {finding.severity}")
                    lines.append(f"    Location:    Line {finding.line}, Column {finding.column}")
                    lines.append(f"    Pattern:     {finding.matched_pattern}")
                    lines.append(f"    Description: {finding.description}")
                    lines.append(f"    Code:        {finding.code_snippet}")

        lines.append("=" * 60)
        lines.append("END OF REPORT")

        return "\n".join(lines)
