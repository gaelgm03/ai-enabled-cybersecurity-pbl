"""
JSON report generator.
"""

import json
from pathlib import Path
from typing import Union

from ..schema import ScanReport


class JSONReporter:
    """Generates JSON reports from scan results."""
    
    def __init__(self, report: ScanReport):
        self.report = report
    
    def generate(self) -> str:
        """Generate JSON string."""
        return self.report.to_json(indent=2)
    
    def save(self, output_path: Union[str, Path]) -> Path:
        """Save JSON report to file."""
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        content = self.generate()
        path.write_text(content, encoding="utf-8")
        
        return path
