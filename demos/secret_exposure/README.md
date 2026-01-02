# Hardcoded Secrets / Credential Exposure Demonstration

**MIT Blended AI+X Program - Week 3**  
**Track 3: AI-Enabled Cybersecurity**

---

## Overview

This directory contains educational demonstrations of credential exposure vulnerabilities and secure alternatives. All secrets shown in examples are **FAKE** and for illustration only.

## Files

| File | Purpose |
|------|---------|
| `vulnerable_example.py` | Demonstrates common hardcoding patterns |
| `secure_example.py` | Demonstrates secure secrets management |

---

## What is Credential Exposure?

Credential exposure (also called "hardcoded secrets" or "secret leakage") occurs when sensitive information such as API keys, passwords, tokens, or private keys are embedded directly in source code, configuration files, or other artifacts that may be shared or version-controlled.

### Common Secret Types

| Type | Pattern | Risk Level |
|------|---------|------------|
| AWS Access Keys | `AKIA[A-Z0-9]{16}` | Critical |
| AWS Secret Keys | 40-character alphanumeric | Critical |
| Private Keys | `-----BEGIN (RSA\|EC\|OPENSSH) PRIVATE KEY-----` | Critical |
| OpenAI API Keys | `sk-[a-zA-Z0-9]{48}` | High |
| GitHub PATs | `ghp_[a-zA-Z0-9]{36}` | High |
| Slack Tokens | `xox[baprs]-...` | High |
| JWT Tokens | `eyJ...` (Base64 encoded) | Medium-High |
| Database URLs | `protocol://user:password@host/db` | Critical |

---

## Running the Demonstrations

```bash
# Navigate to the demos directory
cd demos/secret_exposure

# Run the vulnerable example (shows anti-patterns)
python vulnerable_example.py

# Run the secure example (shows best practices)
python secure_example.py
```

---

## Vulnerable Patterns Demonstrated

### 1. Module-Level Constants
```python
# VULNERABLE - Secret in source code
API_KEY = "sk-abc123..."
```

### 2. Class Attributes
```python
# VULNERABLE - Secret bundled with code
class Config:
    STRIPE_KEY = "sk_live_..."
```

### 3. Function Bodies
```python
# VULNERABLE - Secret hidden in logic
def connect():
    password = "ProductionPassword123!"
```

### 4. Configuration Dictionaries
```python
# VULNERABLE - Secrets in data structures
config = {"api_key": "..."}
```

### 5. Connection Strings
```python
# VULNERABLE - Credentials inline
DATABASE_URL = "postgresql://admin:secret@host/db"
```

---

## Secure Patterns Demonstrated

### 1. Environment Variables
```python
# SECURE - Load from environment
api_key = os.environ.get("API_KEY")
```

### 2. Configuration Classes
```python
# SECURE - Explicit loading from environment
@dataclass
class Config:
    api_key: str = field(default_factory=lambda: os.environ.get("API_KEY"))
```

### 3. External Configuration Files
```python
# SECURE - Config outside repository
config = load_config("/etc/myapp/config.json")
```

### 4. Secrets Managers
```python
# SECURE - Centralized secret storage
secret = secrets_manager.get_secret("api-key")
```

---

## Why Developers Make This Mistake

1. **Convenience**: Hardcoding is faster during initial development
2. **Lack of setup**: No secrets management infrastructure
3. **Copy-paste**: Using example code that includes placeholder secrets
4. **Testing shortcuts**: Embedding test credentials for quick iteration
5. **Ignorance**: Not understanding git history persistence
6. **Time pressure**: Deadline-driven commits without review

---

## How Secrets Get Exposed

| Vector | Description |
|--------|-------------|
| **Git History** | Secrets persist in commit history even after deletion |
| **Public Repos** | Automated bots scan GitHub for leaked credentials |
| **Log Files** | Print/debug statements expose secrets to logs |
| **Error Messages** | Stack traces may include sensitive values |
| **Backups** | Database dumps, file backups contain secrets |
| **Container Images** | Secrets baked into Docker layers |
| **CI/CD Logs** | Build logs may expose environment variables |
| **Screenshots** | Terminal screenshots shared in issues/docs |

---

## Real-World Consequences

- **AWS Keys**: Cryptomining charges (thousands to millions of dollars)
- **Database Credentials**: Data breaches, ransomware attacks
- **API Keys**: Service abuse, financial charges
- **Private Keys**: Complete system compromise
- **OAuth Secrets**: Account takeovers across services

---

## Detection Methods

### Manual Code Review
Look for patterns:
- Variable names: `*_KEY`, `*_SECRET`, `*_TOKEN`, `*_PASSWORD`, `*_CREDENTIAL`
- String patterns: `sk-`, `ghp_`, `AKIA`, `-----BEGIN`
- High-entropy strings (random-looking sequences)

### Automated Tools
| Tool | Purpose |
|------|---------|
| **gitleaks** | Scans git repos for secrets |
| **truffleHog** | Searches git history for high-entropy strings |
| **git-secrets** | Pre-commit hook to prevent secret commits |
| **detect-secrets** | Yelp's baseline secret scanner |

### Regex Patterns for Detection
```regex
# AWS Access Key
AKIA[A-Z0-9]{16}

# OpenAI Key
sk-[a-zA-Z0-9]{20,}

# GitHub PAT
ghp_[a-zA-Z0-9]{36,}

# Private Key
-----BEGIN\s+(RSA\s+|EC\s+|OPENSSH\s+)?PRIVATE KEY-----

# Generic password assignment
(password|passwd|pwd|secret)\s*[=:]\s*['"][^'"]{8,}['"]
```

---

## Prevention Best Practices

### 1. Use .gitignore
```gitignore
# Secrets and credentials
.env
.env.*
*.pem
*.key
config.json
secrets.json
```

### 2. Pre-commit Hooks
```bash
# Install git-secrets
brew install git-secrets

# Configure for repository
git secrets --install
git secrets --register-aws
```

### 3. Environment Variables
```bash
# Set via shell
export API_KEY="your-key"

# Or via .env file (gitignored)
echo "API_KEY=your-key" >> .env
```

### 4. .env.example Template
```bash
# .env.example (committed to repo)
API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:password@host/db

# Instructions: Copy to .env and fill in real values
```

### 5. Secrets Rotation
- Rotate secrets regularly (30-90 days)
- Rotate immediately if exposure suspected
- Use secrets managers with automatic rotation

---

## Connection to Week 2 Pipeline

The Week 2 security scanning pipeline includes a **SecretDetector** that uses:
- **gitleaks** (if installed) for comprehensive scanning
- **Regex fallback** patterns for common secret types
- **Redaction layer** to never store/display full secrets

This Week 3 understanding informs how we:
- Recognize vulnerable patterns
- Understand why detection matters
- Appreciate the importance of redaction

---

## References

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html)
- [CWE-259: Use of Hard-coded Password](https://cwe.mitre.org/data/definitions/259.html)
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [gitleaks Documentation](https://github.com/gitleaks/gitleaks)
- [12-Factor App: Config](https://12factor.net/config)

---

## Ethical Notice

This demonstration is for **educational and defensive purposes only**. All credentials shown are fake. Never:

- Commit real credentials to version control
- Use leaked credentials found in public repositories
- Exploit exposed credentials without authorization

If you discover exposed credentials in a public repository, follow responsible disclosure practices.

---

*Week 3 - MIT Blended AI+X PBL - AI-Enabled Cybersecurity*
