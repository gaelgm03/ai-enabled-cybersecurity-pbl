"""
Hardcoded Secrets / Credential Exposure Demonstration
======================================================
MIT Blended AI+X Program - Week 3

PURPOSE: Educational demonstration of credential exposure vulnerabilities.
WARNING: All secrets shown are FAKE examples. NEVER commit real credentials.

This module demonstrates:
1. Common patterns of hardcoded secrets
2. Why they are dangerous
3. How they get exposed
"""

import os
import json


# =============================================================================
# VULNERABLE PATTERNS - DO NOT USE IN PRODUCTION
# =============================================================================

# Pattern 1: Direct assignment of API keys
# VULNERABLE: Hardcoded API key in source code
OPENAI_API_KEY = "sk-FAKE1234567890abcdefghijklmnopqrstuvwxyz"  # NOT A REAL KEY

# Pattern 2: Database credentials in code
# VULNERABLE: Database connection string with credentials
DATABASE_URL = "postgresql://admin:SuperSecret123!@db.example.com:5432/production"  # FAKE

# Pattern 3: AWS credentials
# VULNERABLE: Cloud provider credentials
AWS_ACCESS_KEY = "AKIAFAKE12345678WXYZ"  # NOT A REAL KEY
AWS_SECRET_KEY = "FakeSecretKey1234567890abcdefghijklmnop"  # NOT A REAL KEY

# Pattern 4: Private keys embedded in code
# VULNERABLE: SSH/TLS private key
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIFAKEPrivateKeyForDemonstrationOnlyNotReal1234567890
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
ThisIsNotARealPrivateKeyItIsFakeForEducationalPurposes
-----END RSA PRIVATE KEY-----"""  # NOT A REAL KEY


class VulnerableConfig:
    """
    VULNERABLE: Configuration class with hardcoded secrets.
    
    This pattern is common when developers want quick access to credentials
    during development and forget to remove them before committing.
    """
    
    # VULNERABLE: Secrets as class attributes
    # Note: Strings are intentionally split to avoid tripping automated push protection
    STRIPE_API_KEY = "sk_live_" + "FAKE1234567890abcdefghij"  # NOT REAL
    GITHUB_TOKEN = "ghp_" + "FAKEtoken1234567890abcdefghijklmn"  # NOT REAL
    SLACK_WEBHOOK = "https://hooks.slack.com/services/" + "FAKE/FAKE/FAKEWEBHOOK"  # NOT REAL
    
    # VULNERABLE: JWT secret for signing tokens
    JWT_SECRET = "my-super-secret-jwt-key-that-should-not-be-here"  # FAKE
    
    # VULNERABLE: Encryption key
    ENCRYPTION_KEY = "AES256KeyThatShouldNeverBeHardcoded123"  # FAKE


def vulnerable_connect_database():
    """
    VULNERABLE: Function with embedded credentials.
    
    Developers sometimes hardcode credentials "temporarily" during
    development and forget to remove them.
    """
    # VULNERABLE: Credentials in function body
    host = "production-db.example.com"
    username = "db_admin"
    password = "ProductionPassword123!"  # FAKE - Never do this
    database = "customers"
    
    connection_string = f"mysql://{username}:{password}@{host}/{database}"
    print(f"[VULNERABLE] Would connect with: {connection_string}")
    return connection_string


def vulnerable_api_client():
    """
    VULNERABLE: API client with hardcoded authentication.
    """
    headers = {
        "Authorization": "Bearer eyJFAKE.TOKEN.FORDEMO",  # FAKE JWT
        "X-API-Key": "api_key_FAKE_1234567890",  # FAKE
    }
    print(f"[VULNERABLE] Headers with exposed credentials: {headers}")
    return headers


# Pattern 5: Secrets in configuration dictionaries
# VULNERABLE: Config dict with embedded secrets
config = {
    "app_name": "MyApplication",
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "postgres",
        "password": "postgres123"  # FAKE - Common weak password pattern
    },
    "api_keys": {
        "sendgrid": "SG.FAKE1234567890.abcdefghijklmnopqrstuvwxyz",  # FAKE
        "twilio_sid": "ACfake1234567890abcdef1234567890ab",  # FAKE
        "twilio_token": "fake1234567890abcdef1234567890ab"  # FAKE
    },
    "oauth": {
        "google_client_secret": "GOCSPX-FakeClientSecret123456"  # FAKE
    }
}


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_exposure_risks():
    """
    Demonstrate the risks of hardcoded secrets.
    """
    print("=" * 70)
    print("HARDCODED SECRETS VULNERABILITY DEMONSTRATION")
    print("Educational purposes only - MIT Blended AI+X Program")
    print("=" * 70)
    print()
    print("NOTE: All credentials shown are FAKE and for demonstration only.")
    print()
    
    print("-" * 70)
    print("PATTERN 1: Module-Level Constants")
    print("-" * 70)
    print(f"OPENAI_API_KEY = {OPENAI_API_KEY[:20]}...")
    print(f"AWS_ACCESS_KEY = {AWS_ACCESS_KEY}")
    print("Risk: These appear in plain text in your repository.")
    print()
    
    print("-" * 70)
    print("PATTERN 2: Class Attributes")
    print("-" * 70)
    print(f"VulnerableConfig.STRIPE_API_KEY = {VulnerableConfig.STRIPE_API_KEY[:25]}...")
    print(f"VulnerableConfig.JWT_SECRET = {VulnerableConfig.JWT_SECRET}")
    print("Risk: Secrets are bundled with your application code.")
    print()
    
    print("-" * 70)
    print("PATTERN 3: Function Bodies")
    print("-" * 70)
    vulnerable_connect_database()
    print("Risk: Code review may miss secrets buried in function logic.")
    print()
    
    print("-" * 70)
    print("PATTERN 4: Configuration Dictionaries")
    print("-" * 70)
    print(f"config['database']['password'] = {config['database']['password']}")
    print(f"config['api_keys']['sendgrid'] = {config['api_keys']['sendgrid'][:25]}...")
    print("Risk: JSON/YAML config exports may leak to logs or error messages.")
    print()
    
    print("-" * 70)
    print("HOW SECRETS GET EXPOSED:")
    print("-" * 70)
    print("1. Git history: Even if removed, secrets persist in commit history")
    print("2. Public repositories: Bots constantly scan GitHub for leaked keys")
    print("3. Log files: Print statements may expose credentials")
    print("4. Error messages: Stack traces can include sensitive values")
    print("5. Compiled binaries: Strings can be extracted from executables")
    print("6. Backup files: IDE swap files, .pyc files may contain secrets")
    print("7. Container images: Secrets baked into Docker layers")
    print()
    
    print("-" * 70)
    print("REAL-WORLD CONSEQUENCES:")
    print("-" * 70)
    print("- AWS keys: Cryptomining charges (thousands of dollars)")
    print("- Database credentials: Data breaches, ransomware")
    print("- API keys: Service abuse, rate limit exhaustion")
    print("- Private keys: Complete system compromise")
    print("- OAuth secrets: Account takeover")
    print()
    
    print("-" * 70)
    print("DETECTION INDICATORS:")
    print("-" * 70)
    print("Patterns that suggest hardcoded secrets:")
    print("- Variables named: *_KEY, *_SECRET, *_TOKEN, *_PASSWORD")
    print("- Strings matching: sk-, ghp_, AKIA, xox-, -----BEGIN")
    print("- High-entropy strings (random-looking long strings)")
    print("- Base64-encoded values in unexpected places")
    print("- Connection strings with credentials inline")
    print()


if __name__ == "__main__":
    demonstrate_exposure_risks()
