"""
Dependency vulnerability detector using pip-audit and npm audit.
"""

import subprocess
import json
from pathlib import Path
from typing import List, Optional

from ..schema import Finding, FindingType, Severity


class DependencyDetector:
    """Detects vulnerable dependencies in Python and Node.js projects."""
    
    def __init__(self, target_path: str):
        self.target_path = Path(target_path)
    
    def scan(self) -> List[Finding]:
        """Scan for vulnerable dependencies in both Python and Node.js."""
        findings = []
        
        # Check for Python dependencies
        if self._has_python_deps():
            findings.extend(self._scan_python())
        
        # Check for Node.js dependencies
        if self._has_node_deps():
            findings.extend(self._scan_node())
        
        return findings
    
    def _has_python_deps(self) -> bool:
        """Check if project has Python dependency files."""
        patterns = ["requirements.txt", "requirements*.txt", "setup.py", "pyproject.toml"]
        for pattern in patterns:
            if list(self.target_path.glob(pattern)):
                return True
        return False
    
    def _has_node_deps(self) -> bool:
        """Check if project has Node.js dependency files."""
        return (self.target_path / "package.json").exists()
    
    def _scan_python(self) -> List[Finding]:
        """Scan Python dependencies using pip-audit."""
        findings = []
        
        # Find requirements files
        req_files = list(self.target_path.glob("requirements*.txt"))
        
        for req_file in req_files:
            try:
                cmd = [
                    "pip-audit",
                    "-r", str(req_file),
                    "--format", "json",
                    "--progress-spinner", "off"
                ]
                
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=120,
                    cwd=str(self.target_path)
                )
                
                if result.stdout.strip():
                    try:
                        vulns = json.loads(result.stdout)
                        # pip-audit returns {"dependencies": [...]}
                        deps = vulns if isinstance(vulns, list) else vulns.get("dependencies", [])
                        
                        for dep in deps:
                            for vuln in dep.get("vulns", []):
                                severity = self._map_severity(vuln.get("fix_versions", []))
                                
                                finding = Finding(
                                    finding_type=FindingType.DEPENDENCY,
                                    severity=severity,
                                    title=f"Vulnerable package: {dep.get('name', 'unknown')}",
                                    description=f"Package {dep.get('name')}@{dep.get('version')} has known vulnerability",
                                    file_path=str(req_file),
                                    detector="pip-audit",
                                    raw_match=dep.get("name", ""),
                                    redacted_match=dep.get("name", ""),
                                    metadata={
                                        "package": dep.get("name", ""),
                                        "installed_version": dep.get("version", ""),
                                        "vuln_id": vuln.get("id", ""),
                                        "description": vuln.get("description", "")[:200],
                                        "fix_versions": vuln.get("fix_versions", []),
                                    }
                                )
                                findings.append(finding)
                                
                    except json.JSONDecodeError:
                        pass
                        
            except subprocess.TimeoutExpired:
                print(f"[WARN] pip-audit timed out for {req_file}")
            except FileNotFoundError:
                print("[WARN] pip-audit not installed. Install with: pip install pip-audit")
                break
            except Exception as e:
                print(f"[WARN] pip-audit error: {e}")
        
        return findings
    
    def _scan_node(self) -> List[Finding]:
        """Scan Node.js dependencies using npm audit."""
        findings = []
        
        package_json = self.target_path / "package.json"
        if not package_json.exists():
            return findings
        
        # Check if node_modules exists (npm audit needs it)
        node_modules = self.target_path / "node_modules"
        
        try:
            cmd = ["npm", "audit", "--json"]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120,
                cwd=str(self.target_path)
            )
            
            if result.stdout.strip():
                try:
                    audit_result = json.loads(result.stdout)
                    vulnerabilities = audit_result.get("vulnerabilities", {})
                    
                    for pkg_name, vuln_info in vulnerabilities.items():
                        severity = self._map_npm_severity(vuln_info.get("severity", "low"))
                        
                        finding = Finding(
                            finding_type=FindingType.DEPENDENCY,
                            severity=severity,
                            title=f"Vulnerable package: {pkg_name}",
                            description=f"Package {pkg_name} has known vulnerability: {vuln_info.get('severity', 'unknown')} severity",
                            file_path=str(package_json),
                            detector="npm-audit",
                            raw_match=pkg_name,
                            redacted_match=pkg_name,
                            metadata={
                                "package": pkg_name,
                                "severity": vuln_info.get("severity", ""),
                                "via": [str(v) if isinstance(v, str) else v.get("title", "") 
                                       for v in vuln_info.get("via", [])][:3],
                                "range": vuln_info.get("range", ""),
                                "fix_available": vuln_info.get("fixAvailable", False),
                            }
                        )
                        findings.append(finding)
                        
                except json.JSONDecodeError:
                    pass
                    
        except subprocess.TimeoutExpired:
            print("[WARN] npm audit timed out")
        except FileNotFoundError:
            print("[WARN] npm not installed")
        except Exception as e:
            print(f"[WARN] npm audit error: {e}")
        
        return findings
    
    def _map_severity(self, fix_versions: list) -> Severity:
        """Map pip-audit results to severity (heuristic)."""
        # If there's no fix available, it's more severe
        if not fix_versions:
            return Severity.HIGH
        return Severity.MEDIUM
    
    def _map_npm_severity(self, npm_severity: str) -> Severity:
        """Map npm severity to our Severity enum."""
        mapping = {
            "info": Severity.LOW,
            "low": Severity.LOW,
            "moderate": Severity.MEDIUM,
            "high": Severity.HIGH,
            "critical": Severity.CRITICAL,
        }
        return mapping.get(npm_severity.lower(), Severity.MEDIUM)
    
    @staticmethod
    def is_pip_audit_available() -> bool:
        """Check if pip-audit is installed."""
        try:
            subprocess.run(["pip-audit", "--version"], capture_output=True, timeout=5)
            return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
    
    @staticmethod
    def is_npm_available() -> bool:
        """Check if npm is installed."""
        try:
            subprocess.run(["npm", "--version"], capture_output=True, timeout=5)
            return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
