"""Stacked Queries SQL Injection Detector - Multiple statement execution detection."""

import re
import sys
from pathlib import Path
from typing import Dict, List, Any

import yaml

from .base import BaseDetector, Finding


class StackedQueriesDetector(BaseDetector):
    """Detector for stacked queries SQL injection patterns.

    Detects multiple statement execution, batch execution, and dangerous
    command patterns in Python source code.
    """

    def __init__(self, patterns_path: str = None):
        """Initialize the detector with patterns from YAML file.

        Args:
            patterns_path: Optional path to patterns YAML file.
                          Defaults to patterns/stacked.yaml relative to this module.
        """
        if patterns_path is None:
            module_dir = Path(__file__).parent.parent
            patterns_path = module_dir / "patterns" / "stacked.yaml"

        self._patterns = self._load_patterns(patterns_path)

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "stacked"

    def _load_patterns(self, patterns_path: str) -> List[Dict[str, Any]]:
        """Load patterns from YAML file.

        Args:
            patterns_path: Path to the patterns YAML file.

        Returns:
            List of pattern dictionaries with compiled regex.
        """
        patterns_path = Path(patterns_path)

        if not patterns_path.exists():
            raise FileNotFoundError(f"Patterns file not found: {patterns_path}")

        with open(patterns_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        patterns = []
        for pattern in data.get("patterns", []):
            compiled = {
                "name": pattern["name"],
                "subtype": pattern["subtype"],
                "regex": re.compile(pattern["regex"], re.IGNORECASE),
                "severity": pattern["severity"],
                "description": pattern["description"],
            }
            patterns.append(compiled)

        return patterns

    def detect(self, file_path: str) -> List[Finding]:
        """Scan a file for stacked queries SQL injection vulnerabilities.

        Args:
            file_path: Path to the Python file to scan.

        Returns:
            List of Finding objects (empty if no vulnerabilities or file error).
        """
        try:
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except (OSError, IOError) as e:
            print(f"Warning: Could not read file {file_path}: {e}", file=sys.stderr)
            return []

        return self.detect_content(content, file_path)

    def detect_content(self, content: str, file_path: str) -> List[Finding]:
        """Scan content for stacked queries SQL injection vulnerabilities.

        Args:
            content: The source code content to scan.
            file_path: The file path (for reporting purposes).

        Returns:
            List of Finding objects (empty if no vulnerabilities found).
        """
        findings: List[Finding] = []
        lines = content.split("\n")

        for pattern in self._patterns:
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
