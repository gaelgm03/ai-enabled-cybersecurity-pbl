"""
Baseline adapter using deterministic detectors only.

MIT Blended AI+X PBL - AI-Enabled Cybersecurity
"""

import re
from .base_adapter import BaseAdapter, ClassificationResult


class BaselineAdapter(BaseAdapter):
    """
    Baseline detector using regex patterns only (no AI).
    
    This represents our Week 2-4 deterministic detectors.
    Always flags pattern matches as vulnerable.
    """
    
    TYPO_PATTERNS = [
        (r'\bteh\b', "teh -> the"),
        (r'\brecieve\b', "recieve -> receive"),
        (r'\boccured\b', "occured -> occurred"),
        (r'\bseperately\b', "seperately -> separately"),
        (r'\buntill\b', "untill -> until"),
        (r'\baccidently\b', "accidently -> accidentally"),
        (r'\boccur\b', "occur (check context)"),
        (r'\bdefinately\b', "definately -> definitely"),
        (r'\bneccessary\b', "neccessary -> necessary"),
        (r'\bprograming\b', "programing -> programming"),
    ]
    
    SECRET_PATTERNS = [
        (r'sk-[a-zA-Z0-9]{20,}', "OpenAI API key pattern"),
        (r'ghp_[a-zA-Z0-9]{36,}', "GitHub PAT pattern"),
        (r'AKIA[A-Z0-9]{16}', "AWS Access Key ID"),
        (r'api[_-]?key\s*[=:]\s*["\']?[a-zA-Z0-9_\-]{20,}', "Generic API key"),
        (r'password\s*[=:]\s*["\'][^"\']{8,}["\']', "Hardcoded password"),
        (r'secret\s*[=:]\s*["\'][^"\']{8,}["\']', "Hardcoded secret"),
        (r'token\s*[=:]\s*["\'][a-zA-Z0-9_\-]{20,}["\']', "Hardcoded token"),
        (r'-----BEGIN\s+(RSA\s+)?PRIVATE\s+KEY-----', "Private key"),
    ]
    
    SQLI_PATTERNS = [
        (r'execute\s*\(\s*f["\']', "f-string in execute()"),
        (r'execute\s*\([^)]*\+', "String concatenation in execute()"),
        (r'\.format\s*\([^)]*\)\s*\)', ".format() in SQL"),
        (r'query\s*\(\s*`[^`]*\$\{', "Template literal SQL (JS)"),
        (r'query\s*\([^)]*\+', "String concatenation in query()"),
        (r'%s.*%\s*\(', "% formatting in SQL"),
        (r'\.raw\s*\(\s*f["\']', "Raw query with f-string"),
    ]
    
    @property
    def name(self) -> str:
        return "baseline"
    
    def is_available(self) -> bool:
        return True
    
    def classify(
        self,
        snippet: str,
        category: str,
        language: str,
        context: str = ""
    ) -> ClassificationResult:
        """
        Classify using regex patterns only.
        
        The baseline always flags matches as vulnerable - it cannot distinguish
        between real vulnerabilities and false positives.
        """
        patterns = self._get_patterns(category)
        
        for pattern, description in patterns:
            if re.search(pattern, snippet, re.IGNORECASE):
                return ClassificationResult(
                    is_vulnerable=True,
                    confidence=1.0,
                    rationale=f"Pattern matched: {description}",
                    raw_response=f"MATCH: {pattern}"
                )
        
        return ClassificationResult(
            is_vulnerable=False,
            confidence=1.0,
            rationale="No vulnerability pattern matched",
            raw_response="NO_MATCH"
        )
    
    def _get_patterns(self, category: str) -> list:
        """Get patterns for a category."""
        if category == "typo":
            return self.TYPO_PATTERNS
        elif category == "secret":
            return self.SECRET_PATTERNS
        elif category == "sqli":
            return self.SQLI_PATTERNS
        return []
