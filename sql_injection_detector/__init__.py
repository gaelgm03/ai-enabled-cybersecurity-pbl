"""SQL Injection Detector - A framework for detecting SQL injection vulnerabilities.

This package provides tools for scanning Python source code to detect
potential SQL injection vulnerabilities using pattern-based detection.

Phase 1 includes:
- Classic detector: Error-based and Union-based SQL injection patterns

Phase 2 will add:
- Blind detector: Boolean-based and time-based blind SQL injection
- Out-of-band detector: DNS and HTTP exfiltration patterns
- Stacked queries detector: Multiple statement execution patterns
"""

from .detectors import BaseDetector, ClassicDetector, FileResult, Finding
from .reporter import Reporter
from .runner import DetectorRegistry, create_default_registry, run_scan

__version__ = "1.0.0"
__all__ = [
    "BaseDetector",
    "ClassicDetector",
    "FileResult",
    "Finding",
    "Reporter",
    "DetectorRegistry",
    "create_default_registry",
    "run_scan",
]
