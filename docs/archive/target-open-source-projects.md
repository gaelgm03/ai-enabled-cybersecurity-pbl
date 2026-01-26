# Target Open-Source Projects for Security Analysis

**MIT Blended AI+X Program - Track 3: AI-Enabled Cybersecurity**  
**Living Document - Last Updated: Week 4**

---

## Overview

This document tracks open-source projects selected for security vulnerability analysis as part of the AI-Enabled Cybersecurity PBL. Projects are categorized by their purpose and analysis status.

### Selection Criteria

Projects are selected based on:
- **Educational value**: Clear examples of vulnerability patterns
- **Active maintenance**: Regularly updated and supported
- **Non-malicious purpose**: Legitimate software or training platforms
- **Public availability**: Open-source with accessible code
- **Relevance**: Contains patterns matching our focus areas

### Analysis Scope

- ✅ Static code analysis
- ✅ Pattern identification
- ✅ Documentation review
- ❌ Runtime exploitation
- ❌ Automated PR submissions
- ❌ Disclosure without coordination

---

## Category 1: Intentionally Vulnerable Applications (Training)

These projects are **designed for security education** and intentionally contain vulnerabilities.

### 1.1 DVWA (Damn Vulnerable Web Application)

| Field | Value |
|-------|-------|
| **URL** | https://github.com/digininja/DVWA |
| **Language** | PHP |
| **Stars** | 10,000+ |
| **Vulnerabilities** | SQLi, XSS, CSRF, File Upload, Command Injection |
| **Analysis Status** | ✅ **Analyzed (Week 3)** |

**Why Important**: Industry-standard training application used in security certifications. Demonstrates vulnerability progression from "low" to "high" security.

**Findings**: SQL injection patterns in `vulnerabilities/sqli/source/low.php` match our demonstration patterns exactly.

---

### 1.2 WebGoat (OWASP)

| Field | Value |
|-------|-------|
| **URL** | https://github.com/WebGoat/WebGoat |
| **Language** | Java |
| **Stars** | 7,000+ |
| **Vulnerabilities** | OWASP Top 10 complete coverage |
| **Analysis Status** | ✅ **Analyzed (Week 3)** |

**Why Important**: OWASP's official educational platform. Used globally in universities and corporate training. Includes both vulnerable and secure code examples.

**Findings**: SQL injection lessons demonstrate string concatenation patterns identical to our Python demonstrations.

---

### 1.3 OWASP Juice Shop

| Field | Value |
|-------|-------|
| **URL** | https://github.com/juice-shop/juice-shop |
| **Language** | JavaScript/TypeScript (Node.js) |
| **Stars** | 10,000+ |
| **Vulnerabilities** | 100+ challenges covering OWASP Top 10 |
| **Analysis Status** | 📋 **Candidate** |

**Why Important**: Modern full-stack vulnerable application. Covers contemporary vulnerabilities including NoSQL injection, JWT issues, and API security.

**Potential Focus Areas**:
- NoSQL injection patterns (MongoDB)
- JWT secret exposure
- Broken authentication
- API security issues

---

## Category 2: Security Scanning Tools (Reference)

These projects **detect vulnerabilities** and provide reference implementations.

### 2.1 Gitleaks

| Field | Value |
|-------|-------|
| **URL** | https://github.com/gitleaks/gitleaks |
| **Language** | Go |
| **Stars** | 17,000+ |
| **Purpose** | Secret detection in git repositories |
| **Analysis Status** | 📋 **Reference Implementation** |

**Why Important**: Our Week 2 pipeline uses gitleaks. Understanding its detection patterns informs our own regex fallback and future improvements.

**Potential Focus Areas**:
- Detection rule patterns (`config/gitleaks.toml`)
- False positive handling
- Performance optimization strategies

---

### 2.2 Semgrep

| Field | Value |
|-------|-------|
| **URL** | https://github.com/semgrep/semgrep |
| **Language** | OCaml, Python |
| **Stars** | 10,000+ |
| **Purpose** | Static analysis for security and code quality |
| **Analysis Status** | 📋 **Candidate** |

**Why Important**: Leading open-source SAST tool with extensive rule libraries. SQL injection and secret detection rules can inform our pipeline enhancements.

**Potential Focus Areas**:
- SQL injection detection rules
- Secret pattern definitions
- Rule writing methodology

---

### 2.3 Bandit

| Field | Value |
|-------|-------|
| **URL** | https://github.com/PyCQA/bandit |
| **Language** | Python |
| **Stars** | 6,000+ |
| **Purpose** | Python security linter |
| **Analysis Status** | 📋 **Candidate** |

**Why Important**: Python-specific security scanner. Directly relevant to our Python-focused demonstrations and pipeline.

**Potential Focus Areas**:
- SQL injection plugin implementation
- Hardcoded password detection
- Integration patterns for CI/CD

---

## Category 3: Real-World Applications (Historical Vulnerabilities)

These are **production applications** where vulnerabilities were discovered and fixed. Analysis focuses on the **fix commits** and CVE documentation.

### 3.1 Django (Historical CVEs)

| Field | Value |
|-------|-------|
| **URL** | https://github.com/django/django |
| **Language** | Python |
| **Stars** | 80,000+ |
| **CVE Examples** | CVE-2020-9402 (SQL injection in GIS) |
| **Analysis Status** | 📋 **Candidate (Historical)** |

**Why Important**: Major Python web framework. Historical SQL injection CVEs demonstrate how vulnerabilities appear even in well-maintained projects.

**Potential Focus Areas**:
- CVE-2020-9402: SQL injection in `django.contrib.gis`
- Fix commit analysis
- Testing patterns for regression prevention

---

### 3.2 WordPress Plugins (Ecosystem)

| Field | Value |
|-------|-------|
| **URL** | https://github.com/developer-developer/developer-developer (example pattern) |
| **Language** | PHP |
| **CVE Database** | WPScan Vulnerability Database |
| **Analysis Status** | 📋 **Candidate (Pattern Study)** |

**Why Important**: WordPress plugin ecosystem has extensive documented SQL injection and authentication vulnerabilities. WPScan database provides searchable CVE information.

**Potential Focus Areas**:
- Common vulnerable patterns in PHP
- Authentication bypass examples
- Plugin security review methodology

---

## Category 4: Week 4 Validation Targets (Non-Security-Focused)

These are **real-world production projects** used to validate the Week 4 scanner against non-intentionally-vulnerable codebases.

### 4.1 pallets/click

| Field | Value |
|-------|-------|
| **URL** | https://github.com/pallets/click |
| **Language** | Python |
| **Stars** | 17,000+ |
| **Purpose** | Command line interface toolkit |
| **Analysis Status** | ✅ **Analyzed (Week 4)** |

**Why Chosen**: Popular, well-maintained CLI library. Good for testing Python patterns without database code.

**Findings**: 48 total (47 typos, 1 secret pattern). Mostly false positives from intentional naming and test fixtures.

---

### 4.2 httpie/cli

| Field | Value |
|-------|-------|
| **URL** | https://github.com/httpie/cli |
| **Language** | Python |
| **Stars** | 37,000+ |
| **Purpose** | Modern HTTP client |
| **Analysis Status** | ✅ **Analyzed (Week 4)** |

**Why Chosen**: Real-world utility application with authentication handling code.

**Findings**: 17 total (6 typos, 11 secret patterns). Secret patterns are test authentication fixtures.

---

### 4.3 encode/django-rest-framework

| Field | Value |
|-------|-------|
| **URL** | https://github.com/encode/django-rest-framework |
| **Language** | Python |
| **Stars** | 29,000+ |
| **Purpose** | Django REST API framework |
| **Analysis Status** | ✅ **Analyzed (Week 4)** |

**Why Chosen**: Major framework with authentication and database patterns.

**Findings**: 493 total (452 typos, 41 secret patterns). High count due to extensive documentation and test suite.

---

### 4.4 bottlepy/bottle

| Field | Value |
|-------|-------|
| **URL** | https://github.com/bottlepy/bottle |
| **Language** | Python |
| **Stars** | 8,700+ |
| **Purpose** | Micro web framework |
| **Analysis Status** | ✅ **Analyzed (Week 4)** |

**Why Chosen**: Single-file web framework with examples, good for testing pattern detection.

**Findings**: 311 total (300 typos, 11 secret patterns). Most findings in documentation examples.

---

### 4.5 aio-libs/aiohttp

| Field | Value |
|-------|-------|
| **URL** | https://github.com/aio-libs/aiohttp |
| **Language** | Python |
| **Stars** | 16,000+ |
| **Purpose** | Async HTTP client/server |
| **Analysis Status** | ✅ **Analyzed (Week 4)** |

**Why Chosen**: Modern async library with server-side patterns.

**Findings**: 39 total (23 typos, 16 secret patterns). Reasonable false positive rate.

---

## Category 5: Additional Candidates

Projects identified for potential future analysis.

### 5.1 VAmPI (Vulnerable API)

| Field | Value |
|-------|-------|
| **URL** | https://github.com/erev0s/VAmPI |
| **Language** | Python (Flask) |
| **Purpose** | Vulnerable REST API for testing |
| **Analysis Status** | 📋 **Candidate** |

**Why Important**: Focuses on API-specific vulnerabilities including injection, broken authentication, and data exposure.

---

### 5.2 NodeGoat

| Field | Value |
|-------|-------|
| **URL** | https://github.com/OWASP/NodeGoat |
| **Language** | JavaScript (Node.js) |
| **Purpose** | OWASP vulnerable Node.js application |
| **Analysis Status** | 📋 **Candidate** |

**Why Important**: Node.js-specific vulnerabilities including NoSQL injection and server-side JavaScript issues.

---

### 5.3 RailsGoat

| Field | Value |
|-------|-------|
| **URL** | https://github.com/OWASP/railsgoat |
| **Language** | Ruby |
| **Purpose** | OWASP vulnerable Rails application |
| **Analysis Status** | 📋 **Candidate** |

**Why Important**: Ruby on Rails-specific vulnerabilities, demonstrating how even convention-over-configuration frameworks have security pitfalls.

---

## Analysis Status Legend

| Status | Meaning |
|--------|---------|
| ✅ **Analyzed** | Full analysis completed, documented in `week3-open-source-analysis.md` |
| 🔄 **In Progress** | Currently being analyzed |
| 📋 **Candidate** | Identified for future analysis |
| ⏸️ **On Hold** | Deprioritized or blocked |
| ❌ **Rejected** | Not suitable for analysis |

---

## Analysis Workflow

### For Each Project

1. **Identify**: Select project matching criteria
2. **Document**: Add entry to this file with metadata
3. **Analyze**: Review code for target vulnerability patterns
4. **Record**: Document findings in `week3-open-source-analysis.md`
5. **Connect**: Link findings to pipeline improvements
6. **Update**: Mark status as analyzed

### Ethical Checklist

Before analyzing any project:
- [ ] Is this an educational/training application OR a historical CVE?
- [ ] Will analysis remain read-only (no exploitation)?
- [ ] Are findings documented responsibly?
- [ ] Is the project publicly available?
- [ ] Does analysis serve educational purposes?

---

## Connection to Pipeline Development

Insights from these projects inform:

| Analysis Finding | Pipeline Enhancement |
|------------------|---------------------|
| SQL injection patterns | Add SQLi detector module |
| Secret detection rules | Improve regex patterns |
| False positive handling | Add allowlist support |
| Multi-language patterns | Language-specific detectors |

---

## References

### Intentionally Vulnerable Applications
- [OWASP Vulnerable Web Applications Directory](https://owasp.org/www-project-vulnerable-web-applications-directory/)
- [VulnHub](https://www.vulnhub.com/)
- [HackTheBox](https://www.hackthebox.com/)

### Vulnerability Databases
- [NVD](https://nvd.nist.gov/)
- [Snyk Vulnerability DB](https://snyk.io/vuln/)
- [WPScan](https://wpscan.com/vulnerability-database)
- [GitHub Advisory Database](https://github.com/advisories)

### Security Research
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [GitGuardian Reports](https://www.gitguardian.com/state-of-secrets-sprawl-report-2023)

---

*Living Document - MIT Blended AI+X PBL - AI-Enabled Cybersecurity*
