#!/usr/bin/env python3
"""CLI runner for SQL Injection Detector.

Provides command-line interface for scanning source files for SQL injection
vulnerabilities. Supports Python and PHP, with multiple detector types and
output formats.
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Type

from .detectors.base import BaseDetector
from .detectors.blind import BlindDetector
from .detectors.classic import ClassicDetector
from .detectors.oob import OutOfBandDetector
from .detectors.stacked import StackedQueriesDetector
from .reporter import Reporter


class DetectorRegistry:
    """Registry for dynamically managing available detectors.

    Provides easy registration and retrieval of detector classes,
    designed for simple addition of new detector types in Phase 2.
    """

    def __init__(self):
        """Initialize the registry with empty detector map."""
        self._detectors: Dict[str, Type[BaseDetector]] = {}

    def register(self, name: str, detector_class: Type[BaseDetector]) -> None:
        """Register a detector class.

        Args:
            name: Unique identifier for the detector.
            detector_class: The detector class to register.
        """
        self._detectors[name] = detector_class

    def get(self, name: str) -> Type[BaseDetector]:
        """Get a detector class by name.

        Args:
            name: The detector name.

        Returns:
            The detector class.

        Raises:
            KeyError: If detector name is not registered.
        """
        if name not in self._detectors:
            raise KeyError(f"Unknown detector: {name}")
        return self._detectors[name]

    def get_all(self) -> Dict[str, Type[BaseDetector]]:
        """Get all registered detectors.

        Returns:
            Dictionary of detector names to classes.
        """
        return self._detectors.copy()

    def list_names(self) -> List[str]:
        """List all registered detector names.

        Returns:
            List of detector names.
        """
        return list(self._detectors.keys())


def create_default_registry() -> DetectorRegistry:
    """Create registry with default detectors.

    Returns:
        DetectorRegistry with all built-in detectors registered.
    """
    registry = DetectorRegistry()

    # Phase 1 detectors
    registry.register("classic", ClassicDetector)

    # Phase 2 detectors
    registry.register("blind", BlindDetector)
    registry.register("oob", OutOfBandDetector)
    registry.register("stacked", StackedQueriesDetector)

    return registry


# Supported source file extensions
SUPPORTED_EXTENSIONS = {".py", ".php"}


def find_source_files(path: Path) -> List[Path]:
    """Find all supported source files in path.

    Args:
        path: File or directory path.

    Returns:
        List of source file paths (Python and PHP).
    """
    if path.is_file():
        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            return [path]
        return []

    if path.is_dir():
        files = []
        for ext in SUPPORTED_EXTENSIONS:
            files.extend(path.rglob(f"*{ext}"))
        return files

    return []


def run_scan(
    path: str,
    detector_types: List[str],
    registry: DetectorRegistry,
) -> Reporter:
    """Run SQL injection scan on target path.

    Args:
        path: Target file or directory path.
        detector_types: List of detector types to run.
        registry: DetectorRegistry with available detectors.

    Returns:
        Reporter with scan results.
    """
    reporter = Reporter()
    target_path = Path(path)

    if not target_path.exists():
        print(f"Error: Path does not exist: {path}", file=sys.stderr)
        sys.exit(1)

    # Find source files
    source_files = find_source_files(target_path)

    if not source_files:
        print(f"Warning: No supported source files found in: {path}", file=sys.stderr)

    # Initialize detectors
    detectors = []
    for dtype in detector_types:
        try:
            detector_class = registry.get(dtype)
            detector = detector_class()
            detectors.append(detector)
            reporter.add_detector_run(detector.name)
        except KeyError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    # Scan each file with all detectors
    for file_path in source_files:
        all_findings = []
        for detector in detectors:
            findings = detector.detect(str(file_path))
            all_findings.extend(findings)
        reporter.add_findings(str(file_path), all_findings)

    return reporter


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed arguments namespace.
    """
    parser = argparse.ArgumentParser(
        description="SQL Injection Detector - Scan Python and PHP code for SQL injection vulnerabilities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --path ./src
  %(prog)s --path app.py --format json --output report.json
  %(prog)s --path ./project --type classic --format text
  %(prog)s --path index.php --format text
  %(prog)s --path ./src --output-dir ./reports

Supported file types: .py, .php
        """,
    )

    parser.add_argument(
        "--path",
        required=True,
        help="Target file or directory to scan",
    )

    parser.add_argument(
        "--type",
        nargs="+",
        default=["all"],
        help="Detector types to run (default: all). Available: classic, blind, oob, stacked",
    )

    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="text",
        help="Output format (default: text)",
    )

    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )

    parser.add_argument(
        "--output-dir",
        help="Directory to auto-save report with timestamped filename",
    )

    return parser.parse_args()


def main() -> None:
    """Main entry point for CLI."""
    args = parse_args()

    # Initialize registry
    registry = create_default_registry()

    # Determine detector types
    if "all" in args.type:
        detector_types = registry.list_names()
    else:
        detector_types = args.type

    # Run scan
    reporter = run_scan(args.path, detector_types, registry)

    # Generate output
    if args.format == "json":
        output = reporter.to_json()
        ext = "json"
    else:
        output = reporter.to_text()
        ext = "txt"

    # Write output
    if args.output_dir:
        # Auto-generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sqli_report_{timestamp}.{ext}"
        output_path = Path(args.output_dir) / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Report saved to: {output_path}")
        print(output)  # Also print to stdout
    elif args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Report written to: {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
