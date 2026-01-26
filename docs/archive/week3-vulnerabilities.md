# Week 3: Vulnerability Identification Guide

**MIT Blended AI+X Program - Track 3: AI-Enabled Cybersecurity**

---

## Overview

This guide describes how to identify two critical vulnerability classes:
1. **SQL Injection (SQLi)**
2. **Hardcoded Secrets / Credential Exposure**

For each vulnerability, we cover:
- Common patterns that indicate the vulnerability
- Why developers accidentally introduce it
- How tools and reviewers can identify it

---

## 1. SQL Injection (SQLi)

### CWE Reference
- **CWE-89**: Improper Neutralization of Special Elements used in an SQL Command

### What to Look For

#### Vulnerable Code Patterns

| Pattern | Language | Example |
|---------|----------|---------|
| String concatenation | Python | `"SELECT * FROM t WHERE x = '" + var + "'"` |
| F-string interpolation | Python | `f"SELECT * FROM t WHERE x = '{var}'"` |
| Format string | Python | `"SELECT * FROM t WHERE x = '%s'" % var` |
| String concatenation | JavaScript | `"SELECT * FROM t WHERE x = '" + var + "'"` |
| Template literals | JavaScript | `` `SELECT * FROM t WHERE x = '${var}'` `` |
| String concatenation | Java | `"SELECT * FROM t WHERE x = '" + var + "'"` |
| String concatenation | PHP | `"SELECT * FROM t WHERE x = '" . $var . "'"` |

#### Regex Patterns for Detection

```regex
# General SQL + string concat
(SELECT|INSERT|UPDATE|DELETE|FROM|WHERE|AND|OR).*['"]?\s*[\+\.]

# Python f-strings with SQL
f["'].*?(SELECT|INSERT|UPDATE|DELETE|WHERE).*?\{[^}]+\}

# Python format strings
["'].*?(SELECT|INSERT|UPDATE|DELETE).*?%[sd]

# JavaScript template literals
`.*?(SELECT|INSERT|UPDATE|DELETE).*?\$\{

# Direct user input in queries
(execute|query|cursor\.execute)\s*\(\s*["'].*?\+
```

#### Contextual Indicators

- **Database operations** near user input handling (form data, query params, API bodies)
- **Dynamic query building** based on runtime values
- **Raw SQL execution** instead of ORM methods
- **String manipulation functions** (concat, format, replace) applied to SQL strings
- **Variables named** `query`, `sql`, `stmt` being built from parts

### Why Developers Introduce This

1. **Quick prototyping**: String concatenation is faster to write initially
2. **Complex queries**: Dynamic WHERE clauses with variable conditions
3. **Legacy code**: Older codebases before parameterized queries were standard
4. **ORM bypass**: "I need raw SQL for performance"
5. **Lack of training**: Not understanding how SQL parsing works
6. **Copy-paste**: Using vulnerable examples from outdated tutorials

### How to Identify (Manual Review)

1. **Search for SQL keywords** near string operations
2. **Trace data flow** from user input to database calls
3. **Check for parameterization** in all database calls
4. **Review ORM usage** for raw query methods
5. **Examine dynamic query builders** for proper escaping

### How to Identify (Automated Tools)

| Tool | Type | SQLi Detection |
|------|------|----------------|
| **Semgrep** | SAST | Strong rules for SQL injection patterns |
| **Bandit** | SAST (Python) | Detects SQL injection in Python |
| **SonarQube** | SAST | Comprehensive SQLi detection |
| **CodeQL** | SAST | GitHub's semantic code analysis |
| **SQLMap** | DAST | Runtime SQL injection testing |

#### Example Semgrep Rule

```yaml
rules:
  - id: sql-injection-python
    patterns:
      - pattern-either:
          - pattern: cursor.execute("..." + $VAR + "...")
          - pattern: cursor.execute(f"...{$VAR}...")
          - pattern: cursor.execute("...%s..." % $VAR)
    message: "Possible SQL injection vulnerability"
    severity: ERROR
    languages: [python]
```

### Secure Alternative

```python
# VULNERABLE
cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")

# SECURE - Parameterized query
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

---

## 2. Hardcoded Secrets / Credential Exposure

### CWE References
- **CWE-798**: Use of Hard-coded Credentials
- **CWE-259**: Use of Hard-coded Password
- **CWE-321**: Use of Hard-coded Cryptographic Key

### What to Look For

#### High-Entropy String Patterns

| Secret Type | Pattern | Example |
|-------------|---------|---------|
| AWS Access Key | `AKIA[A-Z0-9]{16}` | `AKIAIOSFODNN7EXAMPLE` |
| AWS Secret Key | `[A-Za-z0-9/+=]{40}` | 40-char base64-like string |
| OpenAI API Key | `sk-[a-zA-Z0-9]{48}` | `sk-abc123...` |
| GitHub PAT | `ghp_[a-zA-Z0-9]{36}` | `ghp_xxxx...` |
| GitHub Fine-grained | `github_pat_[a-zA-Z0-9_]{22,}` | `github_pat_xxxx...` |
| Slack Token | `xox[baprs]-[0-9]{10,}` | `xoxb-123456-789...` |
| Private Key | `-----BEGIN.*PRIVATE KEY-----` | PEM format key |
| JWT | `eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.` | Base64 encoded JWT |

#### Variable Name Patterns

```regex
(?i)(api[_-]?key|apikey|secret|password|passwd|pwd|token|credential|auth)
(?i)(aws[_-]?secret|private[_-]?key|encryption[_-]?key)
(?i)(database[_-]?password|db[_-]?pass|mysql[_-]?pwd)
```

#### Assignment Patterns

```regex
# Direct assignment with suspicious names
(?i)(api_key|secret|password|token)\s*[=:]\s*["'][^"']{8,}["']

# Connection strings with credentials
(mysql|postgresql|mongodb|redis):\/\/[^:]+:[^@]+@

# Environment-like but hardcoded
(?i)os\.environ\[['"](API_KEY|SECRET)['"]\]\s*=
```

### Why Developers Introduce This

1. **Development convenience**: Quick local testing without setup
2. **Forgotten cleanup**: "I'll remove this before committing"
3. **Copied examples**: Tutorial code with placeholder secrets
4. **Configuration confusion**: Not understanding .env vs source code
5. **CI/CD shortcuts**: Embedding secrets for automated testing
6. **Lack of infrastructure**: No secrets manager available

### How to Identify (Manual Review)

1. **Search for high-entropy strings** (random-looking sequences > 20 chars)
2. **Check variable names** for keywords: key, secret, password, token
3. **Review configuration files** for embedded credentials
4. **Examine connection strings** for inline credentials
5. **Check git history** for removed secrets (they persist!)
6. **Look for base64-encoded values** in unexpected places

### How to Identify (Automated Tools)

| Tool | Type | Description |
|------|------|-------------|
| **gitleaks** | Scanner | Fast, configurable secret scanner |
| **truffleHog** | Scanner | Searches git history for high entropy |
| **detect-secrets** | Scanner | Yelp's baseline scanner |
| **git-secrets** | Pre-commit | Prevents committing secrets |
| **GitHub Secret Scanning** | Platform | Automatic scanning on push |
| **GitGuardian** | Platform | Real-time secret detection |

#### Example Gitleaks Configuration

```toml
[[rules]]
id = "aws-access-key"
description = "AWS Access Key"
regex = '''AKIA[0-9A-Z]{16}'''
tags = ["aws", "credentials"]

[[rules]]
id = "generic-api-key"
description = "Generic API Key"
regex = '''(?i)(api[_-]?key|apikey)\s*[=:]\s*['\"][0-9a-zA-Z]{20,}['\"]'''
tags = ["api", "credentials"]
```

### Secure Alternative

```python
# VULNERABLE
API_KEY = "sk-abc123xyz..."

# SECURE - Environment variable
API_KEY = os.environ.get("API_KEY")

# SECURE - With validation
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise EnvironmentError("API_KEY environment variable required")
```

---

## Detection Strategy Summary

### For Code Review

| Step | Action |
|------|--------|
| 1 | Search for SQL keywords near string operations |
| 2 | Search for high-entropy strings (>20 chars, random-looking) |
| 3 | Search for variable names containing: key, secret, password, token |
| 4 | Trace user input to database queries |
| 5 | Check for parameterization in all DB calls |
| 6 | Review .gitignore for secret file exclusions |

### For Automated Scanning

| Phase | Tools |
|-------|-------|
| Pre-commit | git-secrets, pre-commit hooks with detect-secrets |
| CI/CD | gitleaks, Semgrep, Bandit (Python), CodeQL |
| Continuous | GitHub Secret Scanning, GitGuardian, SonarQube |

---

## Connection to Week 2 Pipeline

The Week 2 security scanning pipeline already includes:
- **SecretDetector**: Uses gitleaks or regex fallback to detect hardcoded secrets
- **Redaction Layer**: Ensures secrets are never stored or displayed in full

### Future Improvements Informed by Week 3

1. **SQL Injection Detection**: Add a SQLi detector module using:
   - Semgrep rules for language-specific patterns
   - AST analysis for data flow tracing
   - Integration with existing Finding schema

2. **Enhanced Secret Detection**: Improve regex patterns based on:
   - Common false positive patterns to exclude
   - New secret formats discovered in OSS analysis
   - Context-aware detection (variable names + values)

3. **Contextual Analysis**: Leverage LLM to:
   - Explain why detected patterns are vulnerable
   - Suggest specific remediation based on code context
   - Identify edge cases that regex might miss

---

## References

### SQL Injection
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [CWE-89](https://cwe.mitre.org/data/definitions/89.html)
- [PortSwigger SQL Injection](https://portswigger.net/web-security/sql-injection)

### Hardcoded Secrets
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [CWE-798](https://cwe.mitre.org/data/definitions/798.html)
- [gitleaks](https://github.com/gitleaks/gitleaks)
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)

### Detection Tools
- [Semgrep](https://semgrep.dev/)
- [Bandit](https://bandit.readthedocs.io/)
- [CodeQL](https://codeql.github.com/)
- [detect-secrets](https://github.com/Yelp/detect-secrets)

---

*Week 3 - MIT Blended AI+X PBL - AI-Enabled Cybersecurity*
