"""Out-of-Band SQL Injection Detector - DNS/HTTP exfiltration and XXE detection."""

import sys
from pathlib import Path
from typing import Dict, List, Any

from .base import BaseDetector, Finding


class OutOfBandDetector(BaseDetector):
    """Detector for out-of-band SQL injection patterns.

    Detects DNS exfiltration, HTTP exfiltration, and XML external entity
    patterns in source code. Supports Python and PHP.
    """

    # Relevant subtypes from unsafe_query.yaml for this detector
    LANGUAGE_SUBTYPES = ["http_exfiltration"]

    def __init__(self):
        """Initialize the detector with patterns for all supported languages."""
        # Load common patterns: oob.yaml
        self._common_patterns: List[Dict[str, Any]] = []
        patterns_dir = Path(__file__).parent.parent / "patterns" / "common"

        oob_file = patterns_dir / "oob.yaml"
        if oob_file.exists():
            self._common_patterns.extend(self._load_yaml_patterns(oob_file))

        # Load language-specific patterns
        self._python_patterns = self._load_language_patterns(
            "python", self.LANGUAGE_SUBTYPES
        )
        self._php_patterns = self._load_language_patterns(
            "php", self.LANGUAGE_SUBTYPES
        )

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "oob"

    def detect(self, file_path: str) -> List[Finding]:
        """Scan a file for out-of-band SQL injection vulnerabilities.

        Args:
            file_path: Path to the source file to scan.

        Returns:
            List of Finding objects (empty if no vulnerabilities or file error).
        """
        try:
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except (OSError, IOError) as e:
            print(f"Warning: Could not read file {file_path}: {e}", file=sys.stderr)
            return []

        language = self._get_language_from_extension(file_path)
        return self.detect_content(content, file_path, language)

    def detect_content(
        self, content: str, file_path: str, language: str = None
    ) -> List[Finding]:
        """Scan content for out-of-band SQL injection vulnerabilities.

        Args:
            content: The source code content to scan.
            file_path: The file path (for reporting purposes).
            language: Target language ('python', 'php', etc.) for pattern selection.

        Returns:
            List of Finding objects (empty if no vulnerabilities found).
        """
        # Always apply common patterns
        patterns = self._common_patterns.copy()

        # Add language-specific patterns
        if language == "python":
            patterns.extend(self._python_patterns)
        elif language == "php":
            patterns.extend(self._php_patterns)

        findings: List[Finding] = []
        lines = content.split("\n")

        for pattern in patterns:
            for match in pattern["regex"].finditer(content):
                line_num, column = self._get_position(content, match.start())
                code_snippet = self._get_snippet(lines, line_num)

                finding = Finding(
                    detector=self.name,
                    subtype=pattern["subtype"],
                    severity=pattern["severity"],
                    line=line_num,
                    column=column,
                    code_snippet=code_snippet,
                    matched_pattern=pattern["name"],
                    description=pattern["description"],
                )
                findings.append(finding)

        # Deduplicate findings by line and pattern
        findings = self._deduplicate_findings(findings)

        return findings
