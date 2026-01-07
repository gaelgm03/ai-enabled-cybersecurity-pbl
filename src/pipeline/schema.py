"""
Unified finding schema for all detector modules.
"""

from dataclasses import dataclass, field, asdict
from typing import Optional, List
from enum import Enum
from datetime import datetime
import json


class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class FindingType(Enum):
    TYPO = "typo"
    SECRET = "secret"
    DEPENDENCY = "dependency"
    SQLI = "sqli"


@dataclass
class Finding:
    """Unified schema for all security findings."""
    
    finding_type: FindingType
    severity: Severity
    title: str
    description: str
    file_path: Optional[str] = None
    line_number: Optional[int] = None
    detector: str = ""
    raw_match: str = ""  # Will be redacted before storage
    redacted_match: str = ""  # Safe to store/display
    remediation: str = ""  # LLM-generated fix instructions
    prevention: str = ""  # LLM-generated prevention guidance
    metadata: dict = field(default_factory=dict)
    
    def to_dict(self) -> dict:
        """Convert to dictionary with enum values as strings."""
        d = asdict(self)
        d["finding_type"] = self.finding_type.value
        d["severity"] = self.severity.value
        return d


@dataclass
class ScanReport:
    """Complete scan report containing all findings."""
    
    scan_id: str
    timestamp: str
    target_path: str
    findings: List[Finding] = field(default_factory=list)
    summary: dict = field(default_factory=dict)
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.utcnow().isoformat() + "Z"
    
    def add_finding(self, finding: Finding):
        self.findings.append(finding)
    
    def compute_summary(self):
        """Compute summary statistics."""
        self.summary = {
            "total_findings": len(self.findings),
            "by_type": {},
            "by_severity": {},
        }
        
        for finding in self.findings:
            ftype = finding.finding_type.value
            sev = finding.severity.value
            
            self.summary["by_type"][ftype] = self.summary["by_type"].get(ftype, 0) + 1
            self.summary["by_severity"][sev] = self.summary["by_severity"].get(sev, 0) + 1
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        self.compute_summary()
        return {
            "scan_id": self.scan_id,
            "timestamp": self.timestamp,
            "target_path": self.target_path,
            "summary": self.summary,
            "findings": [f.to_dict() for f in self.findings],
        }
    
    def to_json(self, indent: int = 2) -> str:
        """Serialize to JSON string."""
        return json.dumps(self.to_dict(), indent=indent)
