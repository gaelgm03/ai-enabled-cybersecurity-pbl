"""
Secret detector using gitleaks (with fallback to regex patterns).
"""

import subprocess
import json
import re
from pathlib import Path
from typing import List

from ..schema import Finding, FindingType, Severity
from ..redaction import Redactor


class SecretDetector:
    """Detects potential secrets and credentials in source code."""
    
    DETECTOR_NAME = "gitleaks"
    FALLBACK_DETECTOR_NAME = "regex-patterns"
    
    # Fallback regex patterns for common secrets (expanded for Week 4)
    SECRET_PATTERNS = [
        # Generic patterns
        (r'(?i)(api[_-]?key|apikey)\s*[=:]\s*["\']?([a-zA-Z0-9_\-]{20,})["\']?', "API Key", Severity.HIGH),
        (r'(?i)(secret|password|passwd|pwd)\s*[=:]\s*["\']?([^\s"\']{8,})["\']?', "Password/Secret", Severity.HIGH),
        (r'(?i)(auth[_-]?token|access[_-]?token)\s*[=:]\s*["\']?([a-zA-Z0-9_\-]{20,})["\']?', "Auth Token", Severity.HIGH),
        
        # OpenAI
        (r'sk-[a-zA-Z0-9]{20,}', "OpenAI API Key", Severity.CRITICAL),
        (r'sk-proj-[a-zA-Z0-9]{20,}', "OpenAI Project API Key", Severity.CRITICAL),
        
        # GitHub
        (r'ghp_[a-zA-Z0-9]{36,}', "GitHub PAT", Severity.CRITICAL),
        (r'github_pat_[a-zA-Z0-9_]{22,}', "GitHub Fine-grained PAT", Severity.CRITICAL),
        (r'gho_[a-zA-Z0-9]{36,}', "GitHub OAuth Token", Severity.CRITICAL),
        (r'ghu_[a-zA-Z0-9]{36,}', "GitHub User Token", Severity.CRITICAL),
        (r'ghs_[a-zA-Z0-9]{36,}', "GitHub Server Token", Severity.CRITICAL),
        
        # Slack
        (r'xox[baprs]-[a-zA-Z0-9\-]{10,}', "Slack Token", Severity.HIGH),
        (r'https://hooks\.slack\.com/services/T[a-zA-Z0-9_]+/B[a-zA-Z0-9_]+/[a-zA-Z0-9_]+', "Slack Webhook URL", Severity.HIGH),
        
        # AWS
        (r'AKIA[A-Z0-9]{16}', "AWS Access Key ID", Severity.CRITICAL),
        (r'ABIA[A-Z0-9]{16}', "AWS STS Access Key", Severity.CRITICAL),
        (r'ACCA[A-Z0-9]{16}', "AWS CloudFront Key", Severity.CRITICAL),
        (r'ASIA[A-Z0-9]{16}', "AWS Temporary Access Key", Severity.HIGH),
        (r'(?i)aws[_-]?secret[_-]?access[_-]?key\s*[=:]\s*["\']?([a-zA-Z0-9/+=]{40})["\']?', "AWS Secret Key", Severity.CRITICAL),
        
        # Google Cloud
        (r'AIza[a-zA-Z0-9_-]{35}', "Google API Key", Severity.HIGH),
        (r'(?i)google[_-]?api[_-]?key\s*[=:]\s*["\']?([a-zA-Z0-9_-]{39})["\']?', "Google API Key", Severity.HIGH),
        
        # Stripe
        (r'sk_live_[a-zA-Z0-9]{24,}', "Stripe Live Secret Key", Severity.CRITICAL),
        (r'sk_test_[a-zA-Z0-9]{24,}', "Stripe Test Secret Key", Severity.MEDIUM),
        (r'pk_live_[a-zA-Z0-9]{24,}', "Stripe Live Publishable Key", Severity.MEDIUM),
        (r'rk_live_[a-zA-Z0-9]{24,}', "Stripe Restricted Key", Severity.HIGH),
        
        # Twilio
        (r'SK[a-f0-9]{32}', "Twilio API Key", Severity.HIGH),
        (r'AC[a-f0-9]{32}', "Twilio Account SID", Severity.MEDIUM),
        
        # SendGrid
        (r'SG\.[a-zA-Z0-9_-]{22}\.[a-zA-Z0-9_-]{43}', "SendGrid API Key", Severity.HIGH),
        
        # Mailchimp
        (r'[a-f0-9]{32}-us[0-9]{1,2}', "Mailchimp API Key", Severity.HIGH),
        
        # Discord
        (r'[MN][a-zA-Z0-9_-]{23,}\.[a-zA-Z0-9_-]{6}\.[a-zA-Z0-9_-]{27}', "Discord Bot Token", Severity.HIGH),
        
        # Heroku
        (r'(?i)heroku[_-]?api[_-]?key\s*[=:]\s*["\']?([a-f0-9-]{36})["\']?', "Heroku API Key", Severity.HIGH),
        
        # Database connection strings
        (r'(?i)(mongodb|postgres|mysql|redis)://[^\s"\']+:[^\s"\']+@', "Database Connection String", Severity.CRITICAL),
        
        # Private keys
        (r'-----BEGIN (RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----', "Private Key", Severity.CRITICAL),
        (r'-----BEGIN CERTIFICATE-----', "Certificate", Severity.MEDIUM),
        
        # JWT
        (r'eyJ[a-zA-Z0-9_-]+\.eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+', "JWT Token", Severity.MEDIUM),
        
        # Generic high-entropy secrets in config files
        (r'(?i)(token|secret|key|credential)\s*[=:]\s*["\']([a-zA-Z0-9_/+=]{32,})["\']', "Generic Secret", Severity.MEDIUM),
    ]
    
    # Directories to skip
    SKIP_DIRS = ["node_modules", ".git", "__pycache__", "venv", ".venv", "dist", "build", "pipeline"]
    
    # Files to skip (to avoid false positives from our own detector code)
    SKIP_FILES = ["secret_detector.py", "redaction.py"]
    
    def __init__(self, target_path: str):
        self.target_path = Path(target_path)
    
    def scan(self) -> List[Finding]:
        """Run gitleaks or fallback to regex patterns."""
        if self.is_available():
            return self._scan_with_gitleaks()
        else:
            print("[INFO] gitleaks not found, using fallback regex patterns")
            return self._scan_with_regex()
    
    def _scan_with_gitleaks(self) -> List[Finding]:
        """Run gitleaks and parse results."""
        findings = []
        
        try:
            cmd = [
                "gitleaks",
                "detect",
                "--source", str(self.target_path),
                "--report-format", "json",
                "--report-path", "/dev/stdout",
                "--no-git",
                "--exit-code", "0"
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.stdout.strip():
                try:
                    leaks = json.loads(result.stdout)
                    for leak in leaks:
                        secret = leak.get("Secret", "")
                        redacted = Redactor.redact_secret(secret)
                        secret_type = Redactor.describe_secret_type(secret)
                        
                        finding = Finding(
                            finding_type=FindingType.SECRET,
                            severity=Severity.HIGH,
                            title=f"Potential {secret_type}",
                            description=f"Detected potential secret: {secret_type}",
                            file_path=leak.get("File", ""),
                            line_number=leak.get("StartLine", 0),
                            detector=self.DETECTOR_NAME,
                            raw_match="[REDACTED]",  # Never store raw secret
                            redacted_match=redacted,
                            metadata={
                                "rule_id": leak.get("RuleID", ""),
                                "secret_type": secret_type,
                                "entropy": leak.get("Entropy", 0),
                            }
                        )
                        findings.append(finding)
                except json.JSONDecodeError:
                    pass
                    
        except subprocess.TimeoutExpired:
            print("[WARN] gitleaks timed out")
        except Exception as e:
            print(f"[WARN] gitleaks error: {e}")
        
        return findings
    
    def _scan_with_regex(self) -> List[Finding]:
        """Fallback: scan using regex patterns."""
        findings = []
        
        for file_path in self._get_files():
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                lines = content.splitlines()
                
                for i, line in enumerate(lines, 1):
                    for pattern, secret_type, severity in self.SECRET_PATTERNS:
                        matches = re.findall(pattern, line)
                        for match in matches:
                            # Handle tuple matches from groups
                            secret = match[-1] if isinstance(match, tuple) else match
                            
                            # Skip if it looks like a placeholder
                            if self._is_placeholder(secret):
                                continue
                            
                            redacted = Redactor.redact_secret(secret)
                            
                            finding = Finding(
                                finding_type=FindingType.SECRET,
                                severity=severity,
                                title=f"Potential {secret_type}",
                                description=f"Detected potential secret matching {secret_type} pattern",
                                file_path=str(file_path),
                                line_number=i,
                                detector=self.FALLBACK_DETECTOR_NAME,
                                raw_match="[REDACTED]",  # Never store raw secret
                                redacted_match=redacted,
                                metadata={
                                    "pattern": pattern[:50] + "...",
                                    "secret_type": secret_type,
                                }
                            )
                            findings.append(finding)
                            
            except Exception as e:
                continue
        
        return findings
    
    def _get_files(self) -> List[Path]:
        """Get files to scan, excluding skip directories and files."""
        files = []
        
        for item in self.target_path.rglob("*"):
            if item.is_file():
                # Check if in skip directory
                skip = False
                for part in item.parts:
                    if part in self.SKIP_DIRS:
                        skip = True
                        break
                
                # Check if in skip files
                if item.name in self.SKIP_FILES:
                    skip = True
                
                if not skip:
                    files.append(item)
        
        return files
    
    def _is_placeholder(self, value: str) -> bool:
        """Check if a value looks like a placeholder rather than a real secret."""
        placeholders = [
            "your_api_key", "your-api-key", "xxx", "placeholder",
            "example", "test", "dummy", "fake", "sample", "changeme",
            "your_secret", "your-secret", "insert_here", "replace_me",
        ]
        
        lower = value.lower()
        return any(p in lower for p in placeholders)
    
    @staticmethod
    def is_available() -> bool:
        """Check if gitleaks is installed."""
        try:
            subprocess.run(
                ["gitleaks", "version"],
                capture_output=True,
                timeout=5
            )
            return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
