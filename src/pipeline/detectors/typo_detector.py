"""
Typo detector using codespell.
"""

import subprocess
import re
from pathlib import Path
from typing import List

from ..schema import Finding, FindingType, Severity


class TypoDetector:
    """Detects typos in source code using codespell."""
    
    DETECTOR_NAME = "codespell"
    
    # File extensions to scan
    EXTENSIONS = [".py", ".js", ".ts", ".md", ".txt", ".json", ".yaml", ".yml", ".html", ".css"]
    
    # Directories to skip
    SKIP_DIRS = ["node_modules", ".git", "__pycache__", "venv", ".venv", "dist", "build", "reports", "pipeline"]
    
    def __init__(self, target_path: str):
        self.target_path = Path(target_path)
    
    def scan(self) -> List[Finding]:
        """
        Run codespell and return findings.
        """
        findings = []
        
        try:
            # Build codespell command
            skip_pattern = ",".join(self.SKIP_DIRS)
            cmd = [
                "codespell",
                "--quiet-level", "2",
                "--skip", skip_pattern,
                str(self.target_path)
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            # Parse codespell output
            # Format: filename:line: word ==> suggestion
            pattern = r'^(.+):(\d+):\s*(.+?)\s*==>\s*(.+)$'
            
            for line in result.stdout.splitlines():
                match = re.match(pattern, line.strip())
                if match:
                    file_path, line_num, typo, suggestion = match.groups()
                    
                    finding = Finding(
                        finding_type=FindingType.TYPO,
                        severity=Severity.LOW,
                        title=f"Typo: '{typo}'",
                        description=f"Possible typo found: '{typo}' should be '{suggestion}'",
                        file_path=file_path,
                        line_number=int(line_num),
                        detector=self.DETECTOR_NAME,
                        raw_match=typo,
                        redacted_match=typo,  # Typos don't need redaction
                        metadata={
                            "typo": typo,
                            "suggestion": suggestion,
                        }
                    )
                    findings.append(finding)
            
            # Also check stderr for any issues
            if result.returncode != 0 and not findings:
                # codespell returns 1 when typos are found, which is expected
                pass
                
        except subprocess.TimeoutExpired:
            print("[WARN] codespell timed out")
        except FileNotFoundError:
            print("[WARN] codespell not installed. Install with: pip install codespell")
        except Exception as e:
            print(f"[WARN] codespell error: {e}")
        
        return findings
    
    @staticmethod
    def is_available() -> bool:
        """Check if codespell is installed."""
        try:
            subprocess.run(
                ["codespell", "--version"],
                capture_output=True,
                timeout=5
            )
            return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
