---
layout: default
title: Background Knowledge
nav_order: 2
---

# Background Knowledge

This section covers the foundational research that informed our project, including common software vulnerabilities, the role of LLMs in cybersecurity, and deep-dive investigations into SQL injection techniques.

---

## 1. Common Software Vulnerabilities

Understanding vulnerability types is essential for building effective detection tools.

### 1.1 Injection Vulnerabilities

Injection vulnerabilities occur when untrusted data is sent to an interpreter as part of a command or query. The attacker's hostile data can trick the interpreter into executing unintended commands.

**Common Types:**
- **SQL Injection (SQLi):** Malicious SQL statements inserted into entry fields
- **Command Injection:** OS commands injected through application inputs
- **LDAP Injection:** Manipulation of LDAP queries
- **XPath Injection:** Targeting XML data stores

**Example - Vulnerable Pattern:**
```python
# DANGEROUS - Never do this!
query = f"SELECT * FROM users WHERE username = '{user_input}'"
```

**Defensive Measures:**
- Use parameterized queries / prepared statements
- Validate and sanitize all user inputs
- Apply least privilege to database accounts
- Use ORM frameworks with built-in protections

### 1.2 Broken Access Control

Access control enforces policies so users cannot act outside their intended permissions. Broken access control allows unauthorized access to resources or functionality.

**Common Manifestations:**
- Vertical privilege escalation (user → admin)
- Horizontal privilege escalation (User A → User B's data)
- Insecure Direct Object References (IDOR)
- Missing function-level access control

### 1.3 Security Misconfiguration

The most common vulnerability type. Occurs when security settings are improperly defined or maintained.

**Examples:**
- Default credentials left unchanged
- Unnecessary features enabled
- Error handling revealing stack traces
- Missing security headers (HSTS, CSP)
- Cloud storage buckets with public access

### 1.4 Vulnerable Components

Applications often rely on third-party libraries with known vulnerabilities.

**Risk Factors:**
- Using components with known CVEs
- Not tracking dependency versions
- Using unmaintained libraries
- Not testing security patch compatibility

### Summary Table

| Vulnerability Type | Primary Risk | Key Defense |
|-------------------|--------------|-------------|
| Injection | Data theft, system compromise | Parameterized queries, input validation |
| Broken Access Control | Unauthorized data access | Server-side authorization checks |
| Security Misconfiguration | Exposure of sensitive data | Hardening processes, regular audits |
| Vulnerable Components | Inherited vulnerabilities | Dependency monitoring, patch management |

---

## 2. LLMs in Cybersecurity

Large Language Models present both opportunities and risks for cybersecurity workflows.

### 2.1 How LLMs Can Assist

**Code Review and Vulnerability Detection:**
- Pattern recognition for common vulnerability types
- Translating technical findings into understandable explanations
- Proposing secure alternatives to vulnerable code

**Security Documentation and Training:**
- Generating security guidelines for specific tech stacks
- Creating training materials for development teams
- Explaining CVEs in plain language

**Threat Intelligence and Analysis:**
- Summarizing vulnerability reports
- Correlating threat indicators
- Drafting incident response documentation

**Security Automation Support:**
- Generating security-focused test cases
- Drafting security policies
- Creating regex patterns for log analysis

### 2.2 Risks and Limitations

| Risk | Cybersecurity Impact | Mitigation |
|------|---------------------|------------|
| **Hallucinations** | False positives/negatives, incorrect remediation | Verify against authoritative sources |
| **Outdated Training Data** | Missing recent CVEs, deprecated practices | Supplement with current databases |
| **Prompt Injection** | Attackers manipulating LLM behavior | Sanitize inputs, validate outputs |
| **Over-Reliance** | Reduced critical thinking | Position LLMs as assistants, not decision-makers |
| **Sensitive Data Exposure** | API keys, credentials in prompts | Scrub data before LLM analysis |

### 2.3 Responsible Use Principles

Based on these considerations, our project follows these principles:

1. **Human Oversight:** All AI-generated assessments require human validation
2. **Verification:** Cross-reference LLM outputs with authoritative sources
3. **Transparency:** Document when and how AI was used
4. **Defense-Only:** Use AI capabilities strictly for defensive purposes
5. **Data Hygiene:** Never expose real credentials to LLMs
6. **Continuous Learning:** Stay informed about evolving AI capabilities and risks

---

## 3. SQL Injection Deep Dive

A comprehensive investigation into SQL injection attack techniques.

### 3.1 What is SQL Injection?

SQL injection exploits applications that construct SQL queries using unsanitized user input. When user input is directly concatenated into SQL strings, attackers can inject malicious code that alters query logic.

### 3.2 Attack Types

#### In-Band SQLi

The attacker uses the same channel for attack and retrieval.

**Error-Based SQLi:**
```sql
-- Attacker input: ' AND 1 = CAST((SELECT database()) AS INT)--
-- Forces conversion error that reveals database name
```

**Union-Based SQLi:**
```sql
-- Attacker input: ' UNION SELECT username, password FROM users--
-- Appends query to extract data from other tables
```

#### Inferential (Blind) SQLi

No explicit data transfer; attacker observes response behavior.

**Boolean-Based:**
```sql
-- Tests conditions character by character
' AND (SELECT SUBSTR(password,1,1) FROM users)='a' --
```

**Time-Based:**
```sql
-- Uses delays to infer boolean conditions
' AND IF(LENGTH(database()) > 5, SLEEP(3), 0)--
```

### 3.3 Impact of Successful Attacks

- **Data Leakage:** Usernames, passwords, financial information
- **Database Access:** Complete control over database contents
- **Denial of Service:** Disruption of application availability
- **System Compromise:** In severe cases, OS-level access

### 3.4 Defense Strategies

| Strategy | Description |
|----------|-------------|
| **Parameterized Queries** | Primary defense; separates code from data |
| **Input Validation** | Reject malformed input early |
| **Allowlists** | For fields with known valid values |
| **Least Privilege** | Database accounts with minimal permissions |
| **Error Handling** | Never expose raw SQL errors to users |
| **ORM Usage** | Built-in protection through abstraction |

---

## 4. Credential Exposure

Understanding how secrets get exposed and how to prevent it.

### 4.1 Common Secret Types

| Type | Pattern | Risk Level |
|------|---------|------------|
| AWS Access Keys | `AKIA[A-Z0-9]{16}` | Critical |
| Private Keys | `-----BEGIN PRIVATE KEY-----` | Critical |
| OpenAI API Keys | `sk-[a-zA-Z0-9]{48}` | High |
| GitHub PATs | `ghp_[a-zA-Z0-9]{36}` | High |
| Database URLs | `protocol://user:password@host/db` | Critical |

### 4.2 Exposure Vectors

- **Git History:** Secrets persist even after deletion
- **Public Repos:** Automated bots scan for leaked credentials
- **Log Files:** Debug statements expose secrets
- **Container Images:** Secrets baked into Docker layers
- **CI/CD Logs:** Build logs may expose environment variables

### 4.3 Prevention Best Practices

- Use `.gitignore` for sensitive files
- Implement pre-commit hooks (git-secrets)
- Store secrets in environment variables
- Use `.env.example` templates
- Rotate secrets regularly
- Use secrets managers with automatic rotation

---

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [NIST Vulnerability Database](https://nvd.nist.gov/)
- [PortSwigger SQL Injection Guide](https://portswigger.net/web-security/sql-injection)
- [CISA Practical Identification of SQL Injection](https://www.cisa.gov/sites/default/files/publications/Practical-SQLi-Identification.pdf)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

---

*MIT Blended AI+X PBL - Track 3: AI-Enabled Cybersecurity*
