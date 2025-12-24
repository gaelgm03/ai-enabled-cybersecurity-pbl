# Common Software Vulnerabilities

> **Week 1 Reference Document**  
> MIT Blended AI+X Program — Track 3: AI-Enabled Cybersecurity

This document provides an educational overview of common software vulnerability types. Understanding these vulnerabilities is foundational for exploring how AI can assist in defensive cybersecurity workflows.

---

## 1. Injection Vulnerabilities

### What It Is
Injection vulnerabilities occur when untrusted data is sent to an interpreter as part of a command or query. The attacker's hostile data can trick the interpreter into executing unintended commands or accessing unauthorized data.

### Common Types
- **SQL Injection (SQLi):** Malicious SQL statements inserted into entry fields
- **Command Injection:** OS commands injected through application inputs
- **LDAP Injection:** Manipulation of LDAP queries
- **XPath Injection:** Targeting XML data stores

### Example Scenario (SQL Injection)
```
// Vulnerable code pattern (pseudocode)
query = "SELECT * FROM users WHERE username = '" + userInput + "'"

// Malicious input: ' OR '1'='1
// Resulting query: SELECT * FROM users WHERE username = '' OR '1'='1'
```

### Defensive Measures
- Use parameterized queries / prepared statements
- Validate and sanitize all user inputs
- Apply least privilege to database accounts
- Use ORM frameworks with built-in protections

### AI Relevance
LLMs can help identify injection-prone code patterns during code review, explain vulnerabilities to developers, and suggest secure alternatives. However, AI-generated code may itself contain injection vulnerabilities if not carefully validated.

---

## 2. Broken Access Control

### What It Is
Access control enforces policies so that users cannot act outside their intended permissions. Broken access control occurs when these restrictions are improperly implemented, allowing unauthorized access to resources or functionality.

### Common Manifestations
- **Vertical privilege escalation:** Regular user accesses admin functionality
- **Horizontal privilege escalation:** User A accesses User B's data
- **Insecure Direct Object References (IDOR):** Manipulating IDs to access other records
- **Missing function-level access control:** Sensitive endpoints exposed without checks

### Example Scenario (IDOR)
```
// Vulnerable URL pattern
https://example.com/api/users/12345/profile

// Attacker changes ID to access another user's profile
https://example.com/api/users/12346/profile
```

### Defensive Measures
- Implement role-based access control (RBAC)
- Validate authorization on every request server-side
- Use indirect references (mapped IDs) instead of direct database keys
- Log and monitor access control failures

### AI Relevance
AI can assist in auditing access control logic by analyzing code paths and identifying missing authorization checks. However, LLMs may miss subtle context-dependent access control requirements that require domain knowledge.

---

## 3. Security Misconfiguration

### What It Is
Security misconfiguration is the most common vulnerability type. It occurs when security settings are not properly defined, implemented, or maintained. This includes default configurations, incomplete setups, open cloud storage, misconfigured HTTP headers, and verbose error messages.

### Common Examples
- Default credentials left unchanged
- Unnecessary features enabled (ports, services, pages)
- Error handling revealing stack traces or sensitive info
- Missing security headers (HSTS, CSP, X-Frame-Options)
- Cloud storage buckets with public access
- Outdated software with known vulnerabilities

### Example Scenario
```
// Verbose error message exposing internal details
Error: Connection failed to database server db-prod-01.internal:5432
Stack trace: 
  at DBConnection.connect (db.js:42)
  at AuthService.validateUser (auth.js:156)
  ...
```

### Defensive Measures
- Establish repeatable hardening processes
- Remove or disable unused features and frameworks
- Review and update configurations regularly
- Implement automated configuration audits
- Use security headers appropriately

### AI Relevance
LLMs can help review configuration files, identify deviations from security baselines, and suggest hardening steps. They can also explain the security implications of specific settings. However, AI may not be aware of the latest CVEs or organization-specific requirements.

---

## 4. Vulnerable and Outdated Components

### What It Is
Applications often rely on third-party libraries, frameworks, and components. When these dependencies have known vulnerabilities or are no longer maintained, the entire application becomes vulnerable.

### Risk Factors
- Using components with known CVEs
- Not knowing the versions of dependencies (direct and transitive)
- Using unmaintained or abandoned libraries
- Not testing compatibility of security patches

### Example Scenario
```
// package.json with outdated dependency
{
  "dependencies": {
    "lodash": "4.17.15"  // Known prototype pollution vulnerability
  }
}
```

### Defensive Measures
- Maintain an inventory of all components and versions
- Monitor for CVEs in dependencies (e.g., Dependabot, Snyk)
- Only obtain components from official sources
- Remove unused dependencies
- Establish a patch management process

### AI Relevance
AI can assist in analyzing dependency trees, explaining CVE impacts, and prioritizing remediation. However, LLMs may have outdated training data and miss recently disclosed vulnerabilities.

---

## Summary Table

| Vulnerability Type | Primary Risk | Key Defense |
|-------------------|--------------|-------------|
| Injection | Data theft, system compromise | Parameterized queries, input validation |
| Broken Access Control | Unauthorized data access | Server-side authorization checks |
| Security Misconfiguration | Exposure of sensitive data | Hardening processes, regular audits |
| Vulnerable Components | Inherited vulnerabilities | Dependency monitoring, patch management |

---

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [NIST Vulnerability Database](https://nvd.nist.gov/)

---

*This document is part of Week 1 learning materials for the AI-Enabled Cybersecurity PBL project.*
