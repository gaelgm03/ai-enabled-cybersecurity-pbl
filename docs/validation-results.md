# Validation Results

**MIT Blended AI+X Program - Track 3: AI-Enabled Cybersecurity**  
**Scan Date:** January 2026

---

## Overview

This document summarizes the results of running the security scanner against 5 non-security-focused, real-world open-source repositories. The goal was to validate the scanner's effectiveness on production codebases rather than intentionally vulnerable training applications.

## Repositories Scanned

| Repository | Language | Stars | Why Chosen |
|------------|----------|-------|------------|
| [pallets/click](https://github.com/pallets/click) | Python | 17,099 | Popular CLI toolkit, well-maintained |
| [httpie/cli](https://github.com/httpie/cli) | Python | 37,306 | HTTP client, real-world utility |
| [encode/django-rest-framework](https://github.com/encode/django-rest-framework) | Python | 29,794 | Major Django extension, database patterns |
| [bottlepy/bottle](https://github.com/bottlepy/bottle) | Python | 8,725 | Micro web framework, SQL examples |
| [aio-libs/aiohttp](https://github.com/aio-libs/aiohttp) | Python | 16,182 | Async HTTP library |

**Total GitHub Stars:** 109,106  
**All repositories are actively maintained, non-security-focused projects.**

---

## Summary Statistics

### Total Findings by Repository

| Repository | Total | Critical | High | Medium | Low |
|------------|-------|----------|------|--------|-----|
| pallets/click | 48 | 0 | 1 | 0 | 47 |
| httpie/cli | 17 | 0 | 11 | 0 | 6 |
| encode/django-rest-framework | 493 | 0 | 41 | 0 | 452 |
| bottlepy/bottle | 311 | 0 | 11 | 0 | 300 |
| aio-libs/aiohttp | 39 | 0 | 16 | 0 | 23 |
| **Total** | **908** | **0** | **80** | **0** | **828** |

### Findings by Category

| Category | Count | Percentage |
|----------|-------|------------|
| 📝 Typos | 828 | 91.2% |
| 🔐 Secrets | 80 | 8.8% |
| 💉 SQL Injection | 0 | 0% |
| 📦 Dependencies | 0 | 0% |

---

## Analysis

### Key Observations

1. **No Critical Findings**: None of the scanned repositories contained critical vulnerabilities, which is expected for well-maintained popular projects.

2. **High Typo Count**: The majority of findings (91%) are typos. Many of these are:
   - Intentional naming (e.g., "inout" as a feature name in Click)
   - British/American spelling variations
   - Technical terms not in the dictionary
   - Test fixture strings

3. **Secret Pattern Matches**: The 80 "secret" findings are primarily false positives:
   - Test passwords/tokens in test files (e.g., `password="secret"` in test cases)
   - Example configuration values
   - Documentation examples
   - High-entropy strings that aren't actually secrets

4. **No SQL Injection Findings**: None of the scanned repositories showed SQL injection patterns. This makes sense because:
   - These are libraries, not database applications
   - Well-maintained projects use parameterized queries
   - ORM usage abstracts raw SQL

5. **No Dependency Vulnerabilities**: No known vulnerable dependencies were detected (pip-audit not installed in scan environment).

### False Positive Analysis

| Finding Type | Likely False Positives | Reason |
|--------------|------------------------|--------|
| Typos | ~70% | Intentional names, technical terms, test data |
| Secrets | ~95% | Test fixtures, documentation, example configs |
| SQLi | N/A | No findings |

### Example Findings

#### Example 1: Typo Finding (Low - Likely False Positive)

**Repository:** pallets/click  
**File:** `examples/inout/inout.py:14`  
**Finding:** Typo "inout"  
**Analysis:** This is the **name of the example**, not a typo. "inout" describes input/output handling and is intentional.

#### Example 2: Secret Finding (High - False Positive)

**Repository:** httpie/cli  
**File:** `tests/test_auth.py`  
**Finding:** Potential Password/Secret  
**Analysis:** This is a **test password** used in unit tests, not a real credential. Example: `password="test_password"` for authentication testing.

#### Example 3: Secret Finding (High - Needs Review)

**Repository:** encode/django-rest-framework  
**File:** Various test files  
**Finding:** Multiple Password/Secret patterns  
**Analysis:** Test authentication credentials. While not real secrets, the pattern detection is **working correctly** - it's flagging hardcoded credentials even in test contexts.

---

## Validation Conclusions

### Scanner Effectiveness

| Aspect | Assessment | Notes |
|--------|------------|-------|
| **Detection Coverage** | ✅ Good | Patterns detected across all repos |
| **False Positive Rate** | ⚠️ High | Expected for pattern-based detection |
| **Performance** | ✅ Good | Scans complete in <60s per repo |
| **Report Quality** | ✅ Good | Clear, actionable reports generated |
| **Real-World Usability** | ✅ Validated | Works on production codebases |

### Recommendations

1. **Add Allowlists**: Implement per-project allowlists to reduce false positives for:
   - Known intentional terms (e.g., "inout")
   - Test file patterns
   - Documentation directories

2. **Context-Aware Detection**: Enhance secret detection to:
   - Reduce severity for findings in test files
   - Check for placeholder patterns more aggressively
   - Consider file path context

3. **Human Review Required**: All findings should be reviewed by developers. The scanner is a **triage tool**, not a definitive verdict.

4. **SQL Injection Testing**: Test against repositories with known database code (e.g., Django apps, Flask apps with SQLAlchemy) to validate SQLi patterns.

---

## Report Outputs

Generated reports are available at:

```
docs/archive/reports/validation/
├── pallets__click/
│   ├── findings.json
│   ├── report.md
│   └── security_report.md
├── httpie__cli/
│   ├── findings.json
│   ├── report.md
│   └── security_report.md
├── encode__django-rest-framework/
│   ├── findings.json
│   ├── report.md
│   └── security_report.md
├── bottlepy__bottle/
│   ├── findings.json
│   ├── report.md
│   └── security_report.md
└── aio-libs__aiohttp/
    ├── findings.json
    ├── report.md
    └── security_report.md
```

---

## Ethical Notes

- All scanned repositories are **public open-source projects**
- Analysis was **read-only** (clone, scan, delete)
- No vulnerabilities were exploited or tested at runtime
- No PRs or issues were submitted to the projects
- Findings are for **educational purposes** within MIT AI+X PBL

---

## Limitations

1. **No gitleaks**: The scan environment did not have gitleaks installed, using regex fallback patterns instead.

2. **No pip-audit**: Dependency scanning was not performed due to missing pip-audit.

3. **Pattern-Based Only**: Detection is static pattern matching, not semantic analysis.

4. **Test Code Included**: Many findings are in test files, which inflates counts.

5. **Single Snapshot**: Scans represent a point-in-time snapshot, not continuous monitoring.

---

*MIT Blended AI+X PBL - AI-Enabled Cybersecurity*
