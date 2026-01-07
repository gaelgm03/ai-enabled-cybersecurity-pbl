# Security Scan Report

**Scan ID:** `scan-20260107-070254-b88725d6`  
**Timestamp:** 2026-01-07T07:02:54.793035Z  
**Target:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli`

---

## Summary

**Total Findings:** 17

### By Severity

| Severity | Count |
|----------|-------|
| 🔴 Critical | 3 |
| 🟠 High | 5 |
| 🟡 Medium | 3 |
| 🟢 Low | 6 |

### By Type

| Type | Count |
|------|-------|
| 📝 Typo | 6 |
| 🔐 Secret | 11 |

---

## Findings

### 🔐 Secret Issues

#### 1. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\httpie\ssl_.py:32`
- **Match (redacted):** `Opti*****str]`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 2. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\httpie\ssl_.py:65`
- **Match (redacted):** `cert********word`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 3. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\tests\test_auth_plugins.py:12`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 4. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\httpie\cli\argparser.py:293`
- **Match (redacted):** `url.****word`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 5. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\httpie\cli\argparser.py:350`
- **Match (redacted):** `cred********lue,`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 6. Potential Certificate

- **Severity:** 🟡 Medium
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\tests\client_certs\client.crt:1`
- **Match (redacted):** `----********----`

**Description:** Detected potential secret matching Certificate pattern

---

#### 7. Potential Private Key

- **Severity:** 🔴 Critical
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\tests\client_certs\client.key:1`
- **Match (redacted):** `****`

**Description:** Detected potential secret matching Private Key pattern

---

#### 8. Potential Certificate

- **Severity:** 🟡 Medium
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\tests\client_certs\client.pem:1`
- **Match (redacted):** `----********----`

**Description:** Detected potential secret matching Certificate pattern

---

#### 9. Potential Private Key

- **Severity:** 🔴 Critical
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\tests\client_certs\client.pem:32`
- **Match (redacted):** `****`

**Description:** Detected potential secret matching Private Key pattern

---

#### 10. Potential Private Key

- **Severity:** 🔴 Critical
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\tests\client_certs\password_protected\client.key:1`
- **Match (redacted):** `****`

**Description:** Detected potential secret matching Private Key pattern

---

#### 11. Potential Certificate

- **Severity:** 🟡 Medium
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\tests\client_certs\password_protected\client.pem:1`
- **Match (redacted):** `----********----`

**Description:** Detected potential secret matching Certificate pattern

---

### 📝 Typo Issues

#### 1. Typo: 'Re-use'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\docs\README.md:2106`

**Description:** Possible typo found: 'Re-use' should be 'Reuse'

- **Suggestion:** `Reuse`

---

#### 2. Typo: 're-used'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\docs\README.md:2146`

**Description:** Possible typo found: 're-used' should be 'reused'

- **Suggestion:** `reused`

---

#### 3. Typo: 'convertors'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\docs\README.md:2413`

**Description:** Possible typo found: 'convertors' should be 'converters'

- **Suggestion:** `converters`

---

#### 4. Typo: 'datas'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\extras\packaging\linux\scripts\hooks\hook-pip.py:11`

**Description:** Possible typo found: 'datas' should be 'data'

- **Suggestion:** `data`

---

#### 5. Typo: 'datas'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\extras\packaging\linux\scripts\hooks\hook-pip.py:12`

**Description:** Possible typo found: 'datas' should be 'data'

- **Suggestion:** `data`

---

#### 6. Typo: 'resuls'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_httpie__cli_m991w987\cli\extras\profiling\benchmarks.py:24`

**Description:** Possible typo found: 'resuls' should be 'results'

- **Suggestion:** `results`

---

## Notes

- All secrets are **redacted** in this report for safety.
- Remediation instructions are AI-generated and should be reviewed by a human.
- This report is generated for educational purposes (MIT AI+X PBL).

*Report generated on 2026-01-07 07:03:04 UTC*