"""SQL Injection Detector - A framework for detecting SQL injection vulnerabilities.

This package provides tools for scanning Python source code to detect
potential SQL injection vulnerabilities using pattern-based detection.

Detectors:
- Classic: Error-based and Union-based SQL injection patterns
- Blind: Boolean-based and time-based blind SQL injection
- Out-of-band: DNS and HTTP exfiltration patterns
- Stacked: Multiple statement execution patterns
"""

from .detectors import (
    BaseDetector,
    BlindDetector,
    ClassicDetector,
    FileResult,
    Finding,
    OutOfBandDetector,
    StackedQueriesDetector,
)
from .reporter import Reporter
from .runner import DetectorRegistry, create_default_registry, run_scan

__version__ = "2.0.0"
__all__ = [
    "BaseDetector",
    "BlindDetector",
    "ClassicDetector",
    "FileResult",
    "Finding",
    "OutOfBandDetector",
    "StackedQueriesDetector",
    "Reporter",
    "DetectorRegistry",
    "create_default_registry",
    "run_scan",
]
