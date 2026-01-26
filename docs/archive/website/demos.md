---
layout: default
title: Educational Demos
nav_order: 5
---

# Educational Demos

Hands-on demonstrations of common security vulnerabilities and their secure alternatives. All code operates on **local, in-memory databases** and all secrets shown are **fake**.

---

## 1. SQL Injection Demonstration

### Overview

This demonstration shows how SQL injection vulnerabilities work and how to prevent them using parameterized queries.

### The Vulnerable Pattern

```python
# DANGEROUS - Never do this!
def get_user_vulnerable(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()
```

When `username` is `' OR '1'='1' --`, the query becomes:
```sql
SELECT * FROM users WHERE username = '' OR '1'='1' --' AND password = 'anything'
```

The condition `'1'='1'` is always true, bypassing authentication entirely.

### The Secure Pattern

```python
# SAFE - Always use parameterized queries
def get_user_secure(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    return cursor.fetchone()
```

The `?` placeholder ensures user input is treated as data, not code.

### Attack Types Demonstrated

#### 1. Authentication Bypass

```python
# Malicious input
username = "' OR '1'='1' --"
password = "anything"

# Vulnerable: Returns first user (usually admin)
# Secure: Returns None (attack blocked)
```

#### 2. Union-Based Data Extraction

```python
# Malicious input
search = "' UNION SELECT username, password FROM users --"

# Vulnerable: Leaks all usernames and passwords
# Secure: Treats input as literal search term
```

#### 3. Boolean-Based Inference

```python
# Malicious input (testing if first character of password is 'a')
username = "admin' AND (SELECT SUBSTR(password,1,1))='a' --"

# Vulnerable: Different response reveals character
# Secure: Attack blocked
```

### Running the Demo

```bash
cd demos/sql_injection

# Run the vulnerable example (educational only)
python vulnerable_example.py

# Run the secure example
python secure_example.py
```

### Expected Output - Vulnerable Example

```
ATTACK 1: Authentication Bypass
Normal login attempt:
[VULNERABLE] Executing query: SELECT * FROM users WHERE username = 'alice' AND password = 'wrong_password'
Result: None

Malicious input - bypassing authentication:
[VULNERABLE] Executing query: SELECT * FROM users WHERE username = '' OR '1'='1' --' AND password = 'anything'
Result: {'id': 1, 'username': 'alice', 'email': 'alice@example.com', 'role': 'admin'}
```

### Expected Output - Secure Example

```
TEST 2: Attempted SQL Injection (Blocked)
[SECURE] Executing parameterized query
[SECURE] Parameters: username="' OR '1'='1' --", password=***
Result: None
Attack blocked! The malicious string was treated as a literal username.
```

---

## 2. Credential Exposure Demonstration

### Overview

This demonstration shows how secrets get accidentally exposed in source code and how to manage them securely.

### Vulnerable Patterns

#### Module-Level Constants

```python
# VULNERABLE - Secret in source code
API_KEY = "sk-abc123xyz789abcdef"
```

#### Class Attributes

```python
# VULNERABLE - Secret bundled with code
class Config:
    STRIPE_KEY = "sk_live_abc123"
```

#### Function Bodies

```python
# VULNERABLE - Secret hidden in logic
def connect():
    password = "ProductionPassword123!"
    return db.connect(password=password)
```

#### Connection Strings

```python
# VULNERABLE - Credentials inline
DATABASE_URL = "postgresql://admin:secretpassword@host/db"
```

### Secure Patterns

#### Environment Variables

```python
# SECURE - Load from environment
import os
api_key = os.environ.get("API_KEY")
```

#### Configuration Classes

```python
# SECURE - Explicit loading from environment
from dataclasses import dataclass, field
import os

@dataclass
class Config:
    api_key: str = field(
        default_factory=lambda: os.environ.get("API_KEY")
    )
```

#### External Configuration Files

```python
# SECURE - Config outside repository
config = load_config("/etc/myapp/config.json")
```

#### Secrets Managers

```python
# SECURE - Centralized secret storage
secret = secrets_manager.get_secret("api-key")
```

### Running the Demo

```bash
cd demos/secret_exposure

# Run the vulnerable example (shows anti-patterns)
python vulnerable_example.py

# Run the secure example (shows best practices)
python secure_example.py
```

---

## Why Developers Make These Mistakes

| Reason | Description |
|--------|-------------|
| **Convenience** | Hardcoding is faster during initial development |
| **Lack of Setup** | No secrets management infrastructure |
| **Copy-Paste** | Using example code with placeholder secrets |
| **Time Pressure** | Deadline-driven commits without review |
| **Ignorance** | Not understanding git history persistence |

---

## How Secrets Get Exposed

| Vector | Description |
|--------|-------------|
| **Git History** | Secrets persist even after deletion |
| **Public Repos** | Automated bots scan GitHub for credentials |
| **Log Files** | Print/debug statements expose secrets |
| **Error Messages** | Stack traces may include sensitive values |
| **Container Images** | Secrets baked into Docker layers |
| **CI/CD Logs** | Build logs may expose environment variables |

---

## Real-World Consequences

- **AWS Keys:** Cryptomining charges (thousands to millions of dollars)
- **Database Credentials:** Data breaches, ransomware attacks
- **API Keys:** Service abuse, financial charges
- **Private Keys:** Complete system compromise
- **OAuth Secrets:** Account takeovers across services

---

## Detection Tools

| Tool | Purpose |
|------|---------|
| **gitleaks** | Scans git repos for secrets |
| **truffleHog** | Searches git history for high-entropy strings |
| **git-secrets** | Pre-commit hook to prevent secret commits |
| **detect-secrets** | Yelp's baseline secret scanner |

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

---

## Secure Coding Guidelines Summary

### SQL Injection Prevention

| Database | Parameterized Syntax |
|----------|---------------------|
| SQLite (Python) | `cursor.execute("SELECT * FROM t WHERE x = ?", (value,))` |
| PostgreSQL (psycopg2) | `cursor.execute("SELECT * FROM t WHERE x = %s", (value,))` |
| MySQL (mysql-connector) | `cursor.execute("SELECT * FROM t WHERE x = %s", (value,))` |
| SQL Server (pyodbc) | `cursor.execute("SELECT * FROM t WHERE x = ?", value)` |

### Defense in Depth

1. **Parameterized queries** - Primary defense
2. **Input validation** - Reject malformed input early
3. **Allowlists** - For fields with known valid values
4. **Least privilege** - Database accounts with minimal permissions
5. **Error handling** - Never expose raw SQL errors to users

---

## Ethical Notice

These demonstrations are for **educational and defensive purposes only**. The techniques shown should only be used:

- In controlled lab environments
- With explicit authorization
- For improving security awareness
- For developing detection tools

**Never** attempt these attacks against systems you do not own or have explicit permission to test.

---

## Source Code

- **SQL Injection Demo:** [`demos/sql_injection/`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/tree/main/demos/sql_injection)
- **Secret Exposure Demo:** [`demos/secret_exposure/`](https://github.com/YOUR_USERNAME/ai-enabled-cybersecurity-pbl/tree/main/demos/secret_exposure)

---

*MIT Blended AI+X PBL - Track 3: AI-Enabled Cybersecurity*
