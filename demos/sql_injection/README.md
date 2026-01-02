# SQL Injection Vulnerability Demonstration

**MIT Blended AI+X Program - Week 3**  
**Track 3: AI-Enabled Cybersecurity**

---

## Overview

This directory contains educational demonstrations of SQL injection vulnerabilities and their secure alternatives. All code operates on **local, in-memory databases** and does not interact with any external systems.

## Files

| File | Purpose |
|------|---------|
| `vulnerable_example.py` | Demonstrates vulnerable code patterns |
| `secure_example.py` | Demonstrates secure alternatives |

---

## What is SQL Injection?

SQL Injection (SQLi) is a code injection technique that exploits vulnerabilities in applications that construct SQL queries using unsanitized user input. When user input is directly concatenated into SQL strings, attackers can inject malicious SQL code that alters the query's logic.

### The Vulnerable Pattern

```python
# DANGEROUS - Never do this!
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)
```

When `username` is `' OR '1'='1' --`, the query becomes:
```sql
SELECT * FROM users WHERE username = '' OR '1'='1' --'
```

The condition `'1'='1'` is always true, returning all users.

### The Secure Pattern

```python
# SAFE - Always use parameterized queries
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

The `?` placeholder ensures user input is treated as data, not code.

---

## Running the Demonstrations

```bash
# Navigate to the demos directory
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

## Attack Types Demonstrated

### 1. Authentication Bypass
Injecting `' OR '1'='1' --` bypasses password checks by making the WHERE clause always true.

### 2. Union-Based Data Extraction
Injecting `' UNION SELECT username, password FROM users --` appends a second query that extracts data from other tables.

### 3. Boolean-Based Inference
Systematically testing conditions like `' AND (SELECT SUBSTR(password,1,1) FROM users)='a' --` to extract data character by character.

---

## Why Developers Make This Mistake

1. **Convenience**: String concatenation is simpler to write initially
2. **Lack of awareness**: Not understanding how SQL parsing works
3. **Copy-paste**: Using vulnerable code examples from outdated sources
4. **Dynamic queries**: Building complex queries programmatically
5. **Framework misuse**: Bypassing ORM protections for "flexibility"

---

## Secure Coding Guidelines

### Always Use Parameterized Queries

| Database | Syntax |
|----------|--------|
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

### Use ORMs When Possible

ORMs like SQLAlchemy, Django ORM, or Prisma provide built-in protection:

```python
# SQLAlchemy example - automatically parameterized
user = session.query(User).filter(User.username == username).first()
```

---

## Detection Patterns

Code reviewers and static analysis tools should flag:

- String concatenation with SQL keywords: `"SELECT" + var`, `f"SELECT ... {var}"`
- Format strings in SQL: `"SELECT ... %s" % var` (without tuple)
- Direct string interpolation: `query = f"... WHERE x = '{user_input}'"`

Regex pattern for detection:
```regex
(SELECT|INSERT|UPDATE|DELETE|FROM|WHERE).*(\+|\.format|f["']|%\s)
```

---

## References

- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [CWE-89: SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
- [PortSwigger SQL Injection Guide](https://portswigger.net/web-security/sql-injection)
- [CISA Practical Identification of SQL Injection](https://www.cisa.gov/sites/default/files/publications/Practical-SQLi-Identification.pdf)

---

## Ethical Notice

This demonstration is for **educational and defensive purposes only**. The techniques shown should only be used:

- In controlled lab environments
- With explicit authorization
- For improving security awareness
- For developing detection tools

Never attempt SQL injection attacks against systems you do not own or have explicit permission to test.

---

*Week 3 - MIT Blended AI+X PBL - AI-Enabled Cybersecurity*
