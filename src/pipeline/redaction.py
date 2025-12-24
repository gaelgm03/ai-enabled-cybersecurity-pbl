"""
Redaction layer for sensitive data.

CRITICAL: Never store or display full secrets.
All matches are redacted before being added to findings.
"""

import re
from typing import Tuple


class Redactor:
    """Handles redaction of sensitive information."""
    
    # Minimum characters to show at start/end of redacted content
    VISIBLE_CHARS = 4
    REDACTION_CHAR = "*"
    
    @classmethod
    def redact_secret(cls, secret: str, visible_chars: int = None) -> str:
        """
        Redact a secret value, showing only first/last few characters.
        
        Examples:
            "sk-abc123xyz789" -> "sk-a***9789"
            "ghp_xxxxxxxxxxxx" -> "ghp_***xxxx"
        """
        if visible_chars is None:
            visible_chars = cls.VISIBLE_CHARS
        
        if not secret or len(secret) <= visible_chars * 2:
            return cls.REDACTION_CHAR * len(secret) if secret else ""
        
        start = secret[:visible_chars]
        end = secret[-visible_chars:]
        middle_len = len(secret) - (visible_chars * 2)
        
        return f"{start}{cls.REDACTION_CHAR * min(middle_len, 8)}{end}"
    
    @classmethod
    def redact_line(cls, line: str, secret: str) -> str:
        """
        Redact a secret within a line of code.
        Returns the line with the secret redacted.
        """
        if not secret or secret not in line:
            return line
        
        redacted = cls.redact_secret(secret)
        return line.replace(secret, redacted)
    
    @classmethod
    def redact_match(cls, match: str, match_type: str = "secret") -> Tuple[str, str]:
        """
        Redact a match based on its type.
        
        Returns:
            Tuple of (original_length_indicator, redacted_value)
        """
        if match_type == "secret":
            redacted = cls.redact_secret(match)
        elif match_type == "typo":
            # Typos don't need redaction, but we keep the interface consistent
            redacted = match
        else:
            # Default: full redaction
            redacted = cls.REDACTION_CHAR * min(len(match), 20)
        
        return f"[{len(match)} chars]", redacted
    
    @classmethod
    def safe_context(cls, context: str, secrets: list) -> str:
        """
        Create a safe version of context with all secrets redacted.
        Used for LLM prompts.
        """
        safe = context
        for secret in secrets:
            if secret and secret in safe:
                safe = safe.replace(secret, cls.redact_secret(secret))
        return safe
    
    @classmethod
    def describe_secret_type(cls, secret: str) -> str:
        """
        Describe the type of secret without revealing it.
        """
        patterns = [
            (r'^sk-[a-zA-Z0-9]+', "OpenAI API Key"),
            (r'^ghp_[a-zA-Z0-9]+', "GitHub Personal Access Token"),
            (r'^github_pat_[a-zA-Z0-9]+', "GitHub Fine-grained PAT"),
            (r'^xox[baprs]-[a-zA-Z0-9-]+', "Slack Token"),
            (r'^AKIA[A-Z0-9]{16}', "AWS Access Key ID"),
            (r'^eyJ[a-zA-Z0-9_-]+\.eyJ', "JWT Token"),
            (r'^pk_live_[a-zA-Z0-9]+', "Stripe Live Key"),
            (r'^sk_live_[a-zA-Z0-9]+', "Stripe Secret Key"),
            (r'^AIza[a-zA-Z0-9_-]{35}', "Google API Key"),
            (r'-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----', "Private Key"),
        ]
        
        for pattern, description in patterns:
            if re.match(pattern, secret):
                return description
        
        return "Potential Secret/Credential"
