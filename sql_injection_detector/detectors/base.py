"""Base classes for SQL injection detectors."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


@dataclass
class Finding:
    """Represents a single SQL injection vulnerability finding."""

    detector: str  # Which detector found this
    subtype: str
    severity: str  # HIGH, MEDIUM, LOW
    line: int
    column: int
    code_snippet: str
    matched_pattern: str
    description: str


@dataclass
class FileResult:
    """Result for a single file scan (aggregated from all detectors)."""

    file: str
    status: str  # VULNERABLE, CLEAN
    findings: List[Finding] = field(default_factory=list)


class BaseDetector(ABC):
    """Abstract base class for SQL injection detectors.

    All detector implementations must inherit from this class and implement
    the required abstract methods. This design allows easy addition of new
    detector types (e.g., blind, out-of-band, stacked queries) in Phase 2.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the detector name identifier."""
        pass

    @abstractmethod
    def detect(self, file_path: str) -> List[Finding]:
        """Scan a file for SQL injection vulnerabilities.

        Args:
            file_path: Path to the file to scan.

        Returns:
            List of Finding objects (empty if no vulnerabilities found).
        """
        pass

    @abstractmethod
    def detect_content(self, content: str, file_path: str) -> List[Finding]:
        """Scan content string for SQL injection vulnerabilities.

        Args:
            content: The source code content to scan.
            file_path: The file path (for reporting purposes).

        Returns:
            List of Finding objects (empty if no vulnerabilities found).
        """
        pass

    def _get_position(self, content: str, match_start: int) -> tuple:
        """Get line number and column from character offset.

        Args:
            content: The full content string.
            match_start: Character offset of the match.

        Returns:
            Tuple of (line_number, column) - both 1-indexed.
        """
        lines_before = content[:match_start].split("\n")
        line_num = len(lines_before)
        column = len(lines_before[-1]) + 1 if lines_before else 1
        return line_num, column

    def _get_snippet(self, lines: List[str], line_num: int) -> str:
        """Extract code snippet for the given line.

        Args:
            lines: List of all lines in the file.
            line_num: 1-indexed line number.

        Returns:
            The code snippet (single line, trimmed).
        """
        if 1 <= line_num <= len(lines):
            return lines[line_num - 1].strip()
        return ""

    def _deduplicate_findings(self, findings: List[Finding]) -> List[Finding]:
        """Remove duplicate findings on the same line with same pattern.

        Args:
            findings: List of findings to deduplicate.

        Returns:
            Deduplicated list of findings.
        """
        seen = set()
        unique = []
        for finding in findings:
            key = (finding.line, finding.matched_pattern)
            if key not in seen:
                seen.add(key)
                unique.append(finding)
        return unique
