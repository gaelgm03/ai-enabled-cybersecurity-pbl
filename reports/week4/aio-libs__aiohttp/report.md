# Security Scan Report

**Scan ID:** `scan-20260107-070412-20780eea`  
**Timestamp:** 2026-01-07T07:04:12.611525Z  
**Target:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp`

---

## Summary

**Total Findings:** 39

### By Severity

| Severity | Count |
|----------|-------|
| 🔴 Critical | 1 |
| 🟠 High | 14 |
| 🟡 Medium | 1 |
| 🟢 Low | 23 |

### By Type

| Type | Count |
|------|-------|
| 📝 Typo | 23 |
| 🔐 Secret | 16 |

---

## Findings

### 🔐 Secret Issues

#### 1. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\helpers.py:161`
- **Match (redacted):** `deco******lit(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 2. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\helpers.py:257`
- **Match (redacted):** `auth*******etrc`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 3. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\docs\client_advanced.rst:75`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 4. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\docs\client_reference.rst:2285`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 5. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\docs\client_reference.rst:2325`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 6. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\examples\basic_auth_middleware.py:36`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 7. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\examples\basic_auth_middleware.py:82`
- **Match (redacted):** `deco******lit(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 8. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\examples\combined_middleware.py:71`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 9. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\examples\combined_middleware.py:181`
- **Match (redacted):** `deco******lit(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 10. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\examples\digest_auth_qop_auth.py:36`
- **Match (redacted):** `PASS*ORD)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 11. Potential Certificate

- **Severity:** 🟡 Medium
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\examples\server.crt:1`
- **Match (redacted):** `----********----`

**Description:** Detected potential secret matching Certificate pattern

---

#### 12. Potential Private Key

- **Severity:** 🔴 Critical
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\examples\server.key:1`
- **Match (redacted):** `****`

**Description:** Detected potential secret matching Private Key pattern

---

#### 13. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\tests\test_client_middleware_digest_auth.py:359`
- **Match (redacted):** `pass*ord,`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 14. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\tests\test_client_middleware_digest_auth.py:655`
- **Match (redacted):** `pass*ord,`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 15. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\tests\test_helpers.py:209`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 16. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\tests\test_helpers.py:213`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

### 📝 Typo Issues

#### 1. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\CONTRIBUTORS.txt:68`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 2. Typo: 'Mata'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\CONTRIBUTORS.txt:112`

**Description:** Possible typo found: 'Mata' should be 'Meta, Mater'

- **Suggestion:** `Meta, Mater`

---

#### 3. Typo: 'Collum'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\CONTRIBUTORS.txt:280`

**Description:** Possible typo found: 'Collum' should be 'Column'

- **Suggestion:** `Column`

---

#### 4. Typo: 'ALLS'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\Makefile:11`

**Description:** Possible typo found: 'ALLS' should be 'ALL, FALLS'

- **Suggestion:** `ALL, FALLS`

---

#### 5. Typo: 'ALLS'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\Makefile:25`

**Description:** Possible typo found: 'ALLS' should be 'ALL, FALLS'

- **Suggestion:** `ALL, FALLS`

---

#### 6. Typo: 'ALLS'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\Makefile:47`

**Description:** Possible typo found: 'ALLS' should be 'ALL, FALLS'

- **Suggestion:** `ALL, FALLS`

---

#### 7. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\client_reqrep.py:1120`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 8. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\client_reqrep.py:1122`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 9. Typo: 'TE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\hdrs.py:96`

**Description:** Possible typo found: 'TE' should be 'THE, BE, WE, TO'

- **Suggestion:** `THE, BE, WE, TO`

---

#### 10. Typo: 'TE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\hdrs.py:96`

**Description:** Possible typo found: 'TE' should be 'THE, BE, WE, TO'

- **Suggestion:** `THE, BE, WE, TO`

---

#### 11. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:269`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 12. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:534`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 13. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:535`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 14. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:536`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 15. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:647`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 16. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:648`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 17. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:648`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 18. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:650`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 19. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:650`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 20. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:740`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 21. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\http_parser.py:742`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 22. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\aiohttp\multipart.py:926`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 23. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_aio-libs__aiohttp_w0m6g1kn\aiohttp\tests\test_http_parser.py:1587`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

## Notes

- All secrets are **redacted** in this report for safety.
- Remediation instructions are AI-generated and should be reviewed by a human.
- This report is generated for educational purposes (MIT AI+X PBL).

*Report generated on 2026-01-07 07:04:28 UTC*