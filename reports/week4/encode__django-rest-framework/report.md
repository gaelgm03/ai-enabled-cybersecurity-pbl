# Security Scan Report

**Scan ID:** `scan-20260107-070321-62ebe95c`  
**Timestamp:** 2026-01-07T07:03:21.464181Z  
**Target:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework`

---

## Summary

**Total Findings:** 493

### By Severity

| Severity | Count |
|----------|-------|
| 🟠 High | 41 |
| 🟢 Low | 452 |

### By Type

| Type | Count |
|------|-------|
| 📝 Typo | 452 |
| 🔐 Secret | 41 |

---

## Findings

### 🔐 Secret Issues

#### 1. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\authentication.py:82`
- **Match (redacted):** `auth********lit(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 2. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_fields.py:2735`
- **Match (redacted):** `seri********ld()`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 3. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_fields.py:2754`
- **Match (redacted):** `seri********ld()`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 4. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_filters.py:854`
- **Match (redacted):** `mode********100)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 5. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_filters.py:869`
- **Match (redacted):** `seri********rue)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 6. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_filters.py:889`
- **Match (redacted):** `pass********ve()`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 7. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_permissions.py:550`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 8. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_permissions.py:556`
- **Match (redacted):** `self******ord)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 9. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_request.py:204`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 10. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_requests_client.py:84`
- **Match (redacted):** `requ*****ata[`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 11. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_requests_client.py:85`
- **Match (redacted):** `pass*ord)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 12. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_testing.py:167`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 13. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_testing.py:177`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 14. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_write_only_fields.py:10`
- **Match (redacted):** `seri********rue)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 15. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs\api-guide\fields.md:124`
- **Match (redacted):** `seri********eld(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 16. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs\topics\html-and-forms.md:113`
- **Match (redacted):** `seri********eld(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 17. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\authtoken\serializers.py:12`
- **Match (redacted):** `seri********eld(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 18. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\authtoken\serializers.py:25`
- **Match (redacted):** `attr**get(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 19. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\authtoken\serializers.py:29`
- **Match (redacted):** `pass*ord)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 20. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\coreapi-0.1.1.js:15`
- **Match (redacted):** `opti********ord;`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 21. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\coreapi-0.1.1.js:1191`
- **Match (redacted):** `inst******n[1]`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 22. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`
- **Match (redacted):** `!0,i********or(e`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 23. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\api.js:206`
- **Match (redacted):** `wind********word`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 24. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\api.js:292`
- **Match (redacted):** `$for***ind(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 25. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\templates\rest_framework\docs\auth\basic.html:22`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 26. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\authentication\test_authentication.py:89`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 27. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\authentication\test_authentication.py:182`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 28. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\authentication\test_authentication.py:208`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 29. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\authentication\test_authentication.py:230`
- **Match (redacted):** `self******ord)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 30. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\authentication\test_authentication.py:239`
- **Match (redacted):** `self******ord)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 31. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\authentication\test_authentication.py:261`
- **Match (redacted):** `self*****word`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 32. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\authentication\test_authentication.py:274`
- **Match (redacted):** `self*****word`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 33. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\authentication\test_authentication.py:299`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 34. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\authentication\test_authentication.py:630`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 35. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\browsable_api\test_browsable_api.py:41`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 36. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\browsable_api\test_browsable_api.py:52`
- **Match (redacted):** `self******ord)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 37. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\browsable_api\test_browsable_api.py:58`
- **Match (redacted):** `self******ord)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 38. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\browsable_api\test_browsable_api.py:69`
- **Match (redacted):** `self******ord)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 39. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\browsable_api\test_browsable_api.py:82`
- **Match (redacted):** `********`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 40. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\browsable_api\test_browsable_api.py:93`
- **Match (redacted):** `self******ord)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 41. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\browsable_api\test_browsable_api.py:99`
- **Match (redacted):** `self******ord)`

**Description:** Detected potential secret matching Password/Secret pattern

---

### 📝 Typo Issues

#### 1. Typo: 'fo'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\codespell-ignore-words.txt:8`

**Description:** Possible typo found: 'fo' should be 'of, for, to, do, go'

- **Suggestion:** `of, for, to, do, go`

---

#### 2. Typo: 'malcom'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\codespell-ignore-words.txt:9`

**Description:** Possible typo found: 'malcom' should be 'malcolm'

- **Suggestion:** `malcolm`

---

#### 3. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\codespell-ignore-words.txt:10`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 4. Typo: 'Malcom'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs\api-guide\parsers.md:12`

**Description:** Possible typo found: 'Malcom' should be 'Malcolm'

- **Suggestion:** `Malcolm`

---

#### 5. Typo: 'Malcom'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs\api-guide\requests.md:10`

**Description:** Possible typo found: 'Malcom' should be 'Malcolm'

- **Suggestion:** `Malcolm`

---

#### 6. Typo: 'koordinates'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs\community\kickstarter-announcement.md:83`

**Description:** Possible typo found: 'koordinates' should be 'coordinates'

- **Suggestion:** `coordinates`

---

#### 7. Typo: 'Koordinates'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs\community\kickstarter-announcement.md:83`

**Description:** Possible typo found: 'Koordinates' should be 'Coordinates'

- **Suggestion:** `Coordinates`

---

#### 8. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs\topics\internationalization.md:46`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 9. Typo: 'bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs_theme\js\jquery-1.8.1-min.js:2`

**Description:** Possible typo found: 'bu' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 10. Typo: 'bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs_theme\js\jquery-1.8.1-min.js:2`

**Description:** Possible typo found: 'bu' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 11. Typo: 'bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs_theme\js\jquery-1.8.1-min.js:2`

**Description:** Possible typo found: 'bu' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 12. Typo: 'bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs_theme\js\jquery-1.8.1-min.js:2`

**Description:** Possible typo found: 'bu' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 13. Typo: 'bU'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs_theme\js\jquery-1.8.1-min.js:2`

**Description:** Possible typo found: 'bU' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 14. Typo: 'bU'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs_theme\js\jquery-1.8.1-min.js:2`

**Description:** Possible typo found: 'bU' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 15. Typo: 'bU'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs_theme\js\jquery-1.8.1-min.js:2`

**Description:** Possible typo found: 'bU' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 16. Typo: 'isnt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\docs_theme\js\prettify-1.0.js:24`

**Description:** Possible typo found: 'isnt' should be 'isn't'

- **Suggestion:** `isn't`

---

#### 17. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:120`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 18. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:157`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 19. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:161`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 20. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:173`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 21. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:178`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 22. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:183`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 23. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:191`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 24. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:224`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 25. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:229`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 26. Typo: 'bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:260`

**Description:** Possible typo found: 'bu' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 27. Typo: 'bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:278`

**Description:** Possible typo found: 'bu' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 28. Typo: 'bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:287`

**Description:** Possible typo found: 'bu' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 29. Typo: 'bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:292`

**Description:** Possible typo found: 'bu' should be 'by, be, but, bug, bun, bud, buy, bum'

- **Suggestion:** `by, be, but, bug, bun, bud, buy, bum`

---

#### 30. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:311`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 31. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:349`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 32. Typo: 'obyekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:425`

**Description:** Possible typo found: 'obyekt' should be 'object'

- **Suggestion:** `object`

---

#### 33. Typo: 'Obyekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:442`

**Description:** Possible typo found: 'Obyekt' should be 'Object'

- **Suggestion:** `Object`

---

#### 34. Typo: 'obyekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:452`

**Description:** Possible typo found: 'obyekt' should be 'object'

- **Suggestion:** `object`

---

#### 35. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:528`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 36. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:543`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 37. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:548`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 38. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\az\LC_MESSAGES\django.po:553`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 39. Typo: 'indicat'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ca\LC_MESSAGES\django.po:42`

**Description:** Possible typo found: 'indicat' should be 'indicate'

- **Suggestion:** `indicate`

---

#### 40. Typo: 'definit'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ca\LC_MESSAGES\django.po:141`

**Description:** Possible typo found: 'definit' should be 'definite'

- **Suggestion:** `definite`

---

#### 41. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ca\LC_MESSAGES\django.po:160`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 42. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ca\LC_MESSAGES\django.po:223`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 43. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ca\LC_MESSAGES\django.po:228`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 44. Typo: 'buit'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ca\LC_MESSAGES\django.po:332`

**Description:** Possible typo found: 'buit' should be 'built'

- **Suggestion:** `built`

---

#### 45. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ca\LC_MESSAGES\django.po:527`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 46. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ca\LC_MESSAGES\django.po:542`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 47. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ca\LC_MESSAGES\django.po:547`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 48. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ca\LC_MESSAGES\django.po:552`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 49. Typo: 'objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\cs\LC_MESSAGES\django.po:426`

**Description:** Possible typo found: 'objekt' should be 'object'

- **Suggestion:** `object`

---

#### 50. Typo: 'objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\cs\LC_MESSAGES\django.po:443`

**Description:** Possible typo found: 'objekt' should be 'object'

- **Suggestion:** `object`

---

#### 51. Typo: 'Objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\cs\LC_MESSAGES\django.po:453`

**Description:** Possible typo found: 'Objekt' should be 'Object'

- **Suggestion:** `Object`

---

#### 52. Typo: 'adresse'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\da\LC_MESSAGES\django.po:216`

**Description:** Possible typo found: 'adresse' should be 'address'

- **Suggestion:** `address`

---

#### 53. Typo: 'formater'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\da\LC_MESSAGES\django.po:261`

**Description:** Possible typo found: 'formater' should be 'formatter'

- **Suggestion:** `formatter`

---

#### 54. Typo: 'formater'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\da\LC_MESSAGES\django.po:279`

**Description:** Possible typo found: 'formater' should be 'formatter'

- **Suggestion:** `formatter`

---

#### 55. Typo: 'formater'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\da\LC_MESSAGES\django.po:288`

**Description:** Possible typo found: 'formater' should be 'formatter'

- **Suggestion:** `formatter`

---

#### 56. Typo: 'formater'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\da\LC_MESSAGES\django.po:293`

**Description:** Possible typo found: 'formater' should be 'formatter'

- **Suggestion:** `formatter`

---

#### 57. Typo: 'adresse'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\da\LC_MESSAGES\django.po:317`

**Description:** Possible typo found: 'adresse' should be 'address'

- **Suggestion:** `address`

---

#### 58. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:47`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 59. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:108`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 60. Typo: 'Sie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:128`

**Description:** Possible typo found: 'Sie' should be 'Size, Sigh, Side'

- **Suggestion:** `Size, Sigh, Side`

---

#### 61. Typo: 'Aktion'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:128`

**Description:** Possible typo found: 'Aktion' should be 'Action'

- **Suggestion:** `Action`

---

#### 62. Typo: 'Methode'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:137`

**Description:** Possible typo found: 'Methode' should be 'Method'

- **Suggestion:** `Method`

---

#### 63. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:165`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 64. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:165`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 65. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:169`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 66. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:181`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 67. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:186`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 68. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:186`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 69. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:186`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 70. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:191`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 71. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:191`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 72. Typo: 'Adresse'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:195`

**Description:** Possible typo found: 'Adresse' should be 'Address'

- **Suggestion:** `Address`

---

#### 73. Typo: 'passt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:199`

**Description:** Possible typo found: 'passt' should be 'past, passed'

- **Suggestion:** `past, passed`

---

#### 74. Typo: 'Sie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:223`

**Description:** Possible typo found: 'Sie' should be 'Size, Sigh, Side'

- **Suggestion:** `Size, Sigh, Side`

---

#### 75. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:223`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 76. Typo: 'Adresse'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:223`

**Description:** Possible typo found: 'Adresse' should be 'Address'

- **Suggestion:** `Address`

---

#### 77. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:227`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 78. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:232`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 79. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:232`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 80. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:237`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 81. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:237`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 82. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:245`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 83. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:250`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 84. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:250`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 85. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:256`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 86. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:256`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 87. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:263`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 88. Typo: 'vor'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:263`

**Description:** Possible typo found: 'vor' should be 'for'

- **Suggestion:** `for`

---

#### 89. Typo: 'Komma'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:263`

**Description:** Possible typo found: 'Komma' should be 'Comma, Coma'

- **Suggestion:** `Comma, Coma`

---

#### 90. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:263`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 91. Typo: 'Formate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:268`

**Description:** Possible typo found: 'Formate' should be 'Format'

- **Suggestion:** `Format`

---

#### 92. Typo: 'Formate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:286`

**Description:** Possible typo found: 'Formate' should be 'Format'

- **Suggestion:** `Format`

---

#### 93. Typo: 'Formate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:295`

**Description:** Possible typo found: 'Formate' should be 'Format'

- **Suggestion:** `Format`

---

#### 94. Typo: 'Formate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:300`

**Description:** Possible typo found: 'Formate' should be 'Format'

- **Suggestion:** `Format`

---

#### 95. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:305`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 96. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:310`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 97. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:324`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 98. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:341`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 99. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:347`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 100. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:353`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 101. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:353`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 102. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:362`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 103. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:367`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 104. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:367`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 105. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:396`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 106. Typo: 'Objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:450`

**Description:** Possible typo found: 'Objekt' should be 'Object'

- **Suggestion:** `Object`

---

#### 107. Typo: 'Objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:460`

**Description:** Possible typo found: 'Objekt' should be 'Object'

- **Suggestion:** `Object`

---

#### 108. Typo: 'Elemente'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:532`

**Description:** Possible typo found: 'Elemente' should be 'Element, Elements'

- **Suggestion:** `Element, Elements`

---

#### 109. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:536`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 110. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:551`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 111. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:556`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 112. Typo: 'Feld'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\de\LC_MESSAGES\django.po:561`

**Description:** Possible typo found: 'Feld' should be 'Field'

- **Suggestion:** `Field`

---

#### 113. Typo: 'contener'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:34`

**Description:** Possible typo found: 'contener' should be 'container'

- **Suggestion:** `container`

---

#### 114. Typo: 'contener'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:54`

**Description:** Possible typo found: 'contener' should be 'container'

- **Suggestion:** `container`

---

#### 115. Typo: 'contener'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:59`

**Description:** Possible typo found: 'contener' should be 'container'

- **Suggestion:** `container`

---

#### 116. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:59`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 117. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:168`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 118. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:172`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 119. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:185`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 120. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:190`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 121. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:217`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 122. Typo: 'requiere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:243`

**Description:** Possible typo found: 'requiere' should be 'require'

- **Suggestion:** `require`

---

#### 123. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:345`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 124. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:378`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 125. Typo: 'inicial'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:418`

**Description:** Possible typo found: 'inicial' should be 'initial, indicial'

- **Suggestion:** `initial, indicial`

---

#### 126. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:534`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 127. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:549`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 128. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:554`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 129. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\es\LC_MESSAGES\django.po:559`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 130. Typo: 'mis'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\et\LC_MESSAGES\django.po:198`

**Description:** Possible typo found: 'mis' should be 'miss, mist'

- **Suggestion:** `miss, mist`

---

#### 131. Typo: 'versioon'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\et\LC_MESSAGES\django.po:558`

**Description:** Possible typo found: 'versioon' should be 'version'

- **Suggestion:** `version`

---

#### 132. Typo: 'versioon'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\et\LC_MESSAGES\django.po:562`

**Description:** Possible typo found: 'versioon' should be 'version'

- **Suggestion:** `version`

---

#### 133. Typo: 'versioon'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\et\LC_MESSAGES\django.po:566`

**Description:** Possible typo found: 'versioon' should be 'version'

- **Suggestion:** `version`

---

#### 134. Typo: 'versioon'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\et\LC_MESSAGES\django.po:570`

**Description:** Possible typo found: 'versioon' should be 'version'

- **Suggestion:** `version`

---

#### 135. Typo: 'versioon'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\et\LC_MESSAGES\django.po:574`

**Description:** Possible typo found: 'versioon' should be 'version'

- **Suggestion:** `version`

---

#### 136. Typo: 'versio'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fi\LC_MESSAGES\django.po:559`

**Description:** Possible typo found: 'versio' should be 'version'

- **Suggestion:** `version`

---

#### 137. Typo: 'versio'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fi\LC_MESSAGES\django.po:563`

**Description:** Possible typo found: 'versio' should be 'version'

- **Suggestion:** `version`

---

#### 138. Typo: 'versio'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fi\LC_MESSAGES\django.po:567`

**Description:** Possible typo found: 'versio' should be 'version'

- **Suggestion:** `version`

---

#### 139. Typo: 'versio'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fi\LC_MESSAGES\django.po:571`

**Description:** Possible typo found: 'versio' should be 'version'

- **Suggestion:** `version`

---

#### 140. Typo: 'versio'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fi\LC_MESSAGES\django.po:575`

**Description:** Possible typo found: 'versio' should be 'version'

- **Suggestion:** `version`

---

#### 141. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:28`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 142. Typo: 'Informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:28`

**Description:** Possible typo found: 'Informations' should be 'Information'

- **Suggestion:** `Information`

---

#### 143. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:32`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 144. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:32`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 145. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:36`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 146. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:36`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 147. Typo: 'mot'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:40`

**Description:** Possible typo found: 'mot' should be 'not'

- **Suggestion:** `not`

---

#### 148. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:40`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 149. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:48`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 150. Typo: 'Informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:48`

**Description:** Possible typo found: 'Informations' should be 'Information'

- **Suggestion:** `Information`

---

#### 151. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:52`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 152. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:56`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 153. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:60`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 154. Typo: 'Mot'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:92`

**Description:** Possible typo found: 'Mot' should be 'Not'

- **Suggestion:** `Not`

---

#### 155. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:96`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 156. Typo: 'invalide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:108`

**Description:** Possible typo found: 'invalide' should be 'invalid'

- **Suggestion:** `invalid`

---

#### 157. Typo: 'Informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:116`

**Description:** Possible typo found: 'Informations' should be 'Information'

- **Suggestion:** `Information`

---

#### 158. Typo: 'Informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:120`

**Description:** Possible typo found: 'Informations' should be 'Information'

- **Suggestion:** `Information`

---

#### 159. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:169`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 160. Typo: 'invalide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:173`

**Description:** Possible typo found: 'invalide' should be 'invalid'

- **Suggestion:** `invalid`

---

#### 161. Typo: 'adresse'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:191`

**Description:** Possible typo found: 'adresse' should be 'address'

- **Suggestion:** `address`

---

#### 162. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:191`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 163. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:207`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 164. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:211`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 165. Typo: 'adresse'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:215`

**Description:** Possible typo found: 'adresse' should be 'address'

- **Suggestion:** `address`

---

#### 166. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:215`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 167. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:219`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 168. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:237`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 169. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:294`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 170. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:313`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 171. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:338`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 172. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:365`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 173. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:401`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 174. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:413`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 175. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:418`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 176. Typo: 'Lien'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:427`

**Description:** Possible typo found: 'Lien' should be 'Line'

- **Suggestion:** `Line`

---

#### 177. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:427`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 178. Typo: 'Lien'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:431`

**Description:** Possible typo found: 'Lien' should be 'Line'

- **Suggestion:** `Line`

---

#### 179. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:431`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 180. Typo: 'Lien'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:435`

**Description:** Possible typo found: 'Lien' should be 'Line'

- **Suggestion:** `Line`

---

#### 181. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:435`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 182. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:449`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 183. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:471`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 184. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:550`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 185. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:554`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 186. Typo: 'invalide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:558`

**Description:** Possible typo found: 'invalide' should be 'invalid'

- **Suggestion:** `invalid`

---

#### 187. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:562`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 188. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\fr\LC_MESSAGES\django.po:566`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 189. Typo: 'elemet'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\hu\LC_MESSAGES\django.po:311`

**Description:** Possible typo found: 'elemet' should be 'element'

- **Suggestion:** `element`

---

#### 190. Typo: 'Nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\it\LC_MESSAGES\django.po:40`

**Description:** Possible typo found: 'Nome' should be 'Gnome'

- **Suggestion:** `Gnome`

---

#### 191. Typo: 'Impossibile'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\it\LC_MESSAGES\django.po:97`

**Description:** Possible typo found: 'Impossibile' should be 'Impossible'

- **Suggestion:** `Impossible`

---

#### 192. Typo: 'nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\it\LC_MESSAGES\django.po:101`

**Description:** Possible typo found: 'nome' should be 'gnome'

- **Suggestion:** `gnome`

---

#### 193. Typo: 'Impossibile'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\it\LC_MESSAGES\django.po:138`

**Description:** Possible typo found: 'Impossibile' should be 'Impossible'

- **Suggestion:** `Impossible`

---

#### 194. Typo: 'nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\it\LC_MESSAGES\django.po:334`

**Description:** Possible typo found: 'nome' should be 'gnome'

- **Suggestion:** `gnome`

---

#### 195. Typo: 'nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\it\LC_MESSAGES\django.po:344`

**Description:** Possible typo found: 'nome' should be 'gnome'

- **Suggestion:** `gnome`

---

#### 196. Typo: 'nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\it\LC_MESSAGES\django.po:574`

**Description:** Possible typo found: 'nome' should be 'gnome'

- **Suggestion:** `gnome`

---

#### 197. Typo: 'vai'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\lv\LC_MESSAGES\django.po:39`

**Description:** Possible typo found: 'vai' should be 'via, vie'

- **Suggestion:** `via, vie`

---

#### 198. Typo: 'vai'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\lv\LC_MESSAGES\django.po:197`

**Description:** Possible typo found: 'vai' should be 'via, vie'

- **Suggestion:** `via, vie`

---

#### 199. Typo: 'vai'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\lv\LC_MESSAGES\django.po:215`

**Description:** Possible typo found: 'vai' should be 'via, vie'

- **Suggestion:** `via, vie`

---

#### 200. Typo: 'vai'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\lv\LC_MESSAGES\django.po:224`

**Description:** Possible typo found: 'vai' should be 'via, vie'

- **Suggestion:** `via, vie`

---

#### 201. Typo: 'vai'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\lv\LC_MESSAGES\django.po:229`

**Description:** Possible typo found: 'vai' should be 'via, vie'

- **Suggestion:** `via, vie`

---

#### 202. Typo: 'vai'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\lv\LC_MESSAGES\django.po:345`

**Description:** Possible typo found: 'vai' should be 'via, vie'

- **Suggestion:** `via, vie`

---

#### 203. Typo: 'teksts'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\lv\LC_MESSAGES\django.po:447`

**Description:** Possible typo found: 'teksts' should be 'texts'

- **Suggestion:** `texts`

---

#### 204. Typo: 'passord'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nb\LC_MESSAGES\django.po:37`

**Description:** Possible typo found: 'passord' should be 'password'

- **Suggestion:** `password`

---

#### 205. Typo: 'Passord'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nb\LC_MESSAGES\django.po:90`

**Description:** Possible typo found: 'Passord' should be 'Password'

- **Suggestion:** `Password`

---

#### 206. Typo: 'som'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nb\LC_MESSAGES\django.po:199`

**Description:** Possible typo found: 'som' should be 'some'

- **Suggestion:** `some`

---

#### 207. Typo: 'lik'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nb\LC_MESSAGES\django.po:226`

**Description:** Possible typo found: 'lik' should be 'like, lick, link'

- **Suggestion:** `like, lick, link`

---

#### 208. Typo: 'lik'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nb\LC_MESSAGES\django.po:231`

**Description:** Possible typo found: 'lik' should be 'like, lick, link'

- **Suggestion:** `like, lick, link`

---

#### 209. Typo: 'komma'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nb\LC_MESSAGES\django.po:257`

**Description:** Possible typo found: 'komma' should be 'comma, coma'

- **Suggestion:** `comma, coma`

---

#### 210. Typo: 'Objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nb\LC_MESSAGES\django.po:454`

**Description:** Possible typo found: 'Objekt' should be 'Object'

- **Suggestion:** `Object`

---

#### 211. Typo: 'noen'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nb\LC_MESSAGES\django.po:567`

**Description:** Possible typo found: 'noen' should be 'none, neon'

- **Suggestion:** `none, neon`

---

#### 212. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:125`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 213. Typo: 'Methode'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:134`

**Description:** Possible typo found: 'Methode' should be 'Method'

- **Suggestion:** `Method`

---

#### 214. Typo: 'leeg'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:166`

**Description:** Possible typo found: 'leeg' should be 'league'

- **Suggestion:** `league`

---

#### 215. Typo: 'leeg'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:178`

**Description:** Possible typo found: 'leeg' should be 'league'

- **Suggestion:** `league`

---

#### 216. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:238`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 217. Typo: 'komma'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:253`

**Description:** Possible typo found: 'komma' should be 'comma, coma'

- **Suggestion:** `comma, coma`

---

#### 218. Typo: 'komma'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:260`

**Description:** Possible typo found: 'komma' should be 'comma, coma'

- **Suggestion:** `comma, coma`

---

#### 219. Typo: 'leeg'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:316`

**Description:** Possible typo found: 'leeg' should be 'league'

- **Suggestion:** `league`

---

#### 220. Typo: 'leeg'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:338`

**Description:** Possible typo found: 'leeg' should be 'league'

- **Suggestion:** `league`

---

#### 221. Typo: 'leeg'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:354`

**Description:** Possible typo found: 'leeg' should be 'league'

- **Suggestion:** `league`

---

#### 222. Typo: 'valide'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\nl\LC_MESSAGES\django.po:377`

**Description:** Possible typo found: 'valide' should be 'valid'

- **Suggestion:** `valid`

---

#### 223. Typo: 'adres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pl\LC_MESSAGES\django.po:190`

**Description:** Possible typo found: 'adres' should be 'address'

- **Suggestion:** `address`

---

#### 224. Typo: 'adres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pl\LC_MESSAGES\django.po:210`

**Description:** Possible typo found: 'adres' should be 'address'

- **Suggestion:** `address`

---

#### 225. Typo: 'adres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pl\LC_MESSAGES\django.po:218`

**Description:** Possible typo found: 'adres' should be 'address'

- **Suggestion:** `address`

---

#### 226. Typo: 'daty'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pl\LC_MESSAGES\django.po:263`

**Description:** Possible typo found: 'daty' should be 'data, date'

- **Suggestion:** `data, date`

---

#### 227. Typo: 'daty'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pl\LC_MESSAGES\django.po:285`

**Description:** Possible typo found: 'daty' should be 'data, date'

- **Suggestion:** `data, date`

---

#### 228. Typo: 'daty'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pl\LC_MESSAGES\django.po:546`

**Description:** Possible typo found: 'daty' should be 'data, date'

- **Suggestion:** `data, date`

---

#### 229. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:56`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 230. Typo: 'Nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:88`

**Description:** Possible typo found: 'Nome' should be 'Gnome'

- **Suggestion:** `Gnome`

---

#### 231. Typo: 'erro'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:104`

**Description:** Possible typo found: 'erro' should be 'error'

- **Suggestion:** `error`

---

#### 232. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:165`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 233. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:177`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 234. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:182`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 235. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:187`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 236. Typo: 'itens'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:306`

**Description:** Possible typo found: 'itens' should be 'items'

- **Suggestion:** `items`

---

#### 237. Typo: 'itens'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:311`

**Description:** Possible typo found: 'itens' should be 'items'

- **Suggestion:** `items`

---

#### 238. Typo: 'Nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:333`

**Description:** Possible typo found: 'Nome' should be 'Gnome'

- **Suggestion:** `Gnome`

---

#### 239. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:333`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 240. Typo: 'nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:343`

**Description:** Possible typo found: 'nome' should be 'gnome'

- **Suggestion:** `gnome`

---

#### 241. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:343`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 242. Typo: 'itens'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:368`

**Description:** Possible typo found: 'itens' should be 'items'

- **Suggestion:** `items`

---

#### 243. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:376`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 244. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:532`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 245. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:547`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 246. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:552`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 247. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt\LC_MESSAGES\django.po:557`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 248. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:60`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 249. Typo: 'Nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:92`

**Description:** Possible typo found: 'Nome' should be 'Gnome'

- **Suggestion:** `Gnome`

---

#### 250. Typo: 'erro'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:108`

**Description:** Possible typo found: 'erro' should be 'error'

- **Suggestion:** `error`

---

#### 251. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:169`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 252. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:173`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 253. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:186`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 254. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:191`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 255. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:219`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 256. Typo: 'itens'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:310`

**Description:** Possible typo found: 'itens' should be 'items'

- **Suggestion:** `items`

---

#### 257. Typo: 'itens'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:315`

**Description:** Possible typo found: 'itens' should be 'items'

- **Suggestion:** `items`

---

#### 258. Typo: 'Nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:337`

**Description:** Possible typo found: 'Nome' should be 'Gnome'

- **Suggestion:** `Gnome`

---

#### 259. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:337`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 260. Typo: 'nome'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:347`

**Description:** Possible typo found: 'nome' should be 'gnome'

- **Suggestion:** `gnome`

---

#### 261. Typo: 'caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:347`

**Description:** Possible typo found: 'caracteres' should be 'characters'

- **Suggestion:** `characters`

---

#### 262. Typo: 'itens'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:372`

**Description:** Possible typo found: 'itens' should be 'items'

- **Suggestion:** `items`

---

#### 263. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:380`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 264. Typo: 'termo'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:388`

**Description:** Possible typo found: 'termo' should be 'thermo'

- **Suggestion:** `thermo`

---

#### 265. Typo: 'inicial'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:420`

**Description:** Possible typo found: 'inicial' should be 'initial, indicial'

- **Suggestion:** `initial, indicial`

---

#### 266. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:536`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 267. Typo: 'Caracteres'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:546`

**Description:** Possible typo found: 'Caracteres' should be 'Characters'

- **Suggestion:** `Characters`

---

#### 268. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:551`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 269. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:556`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 270. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\pt_BR\LC_MESSAGES\django.po:561`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 271. Typo: 'caractere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:28`

**Description:** Possible typo found: 'caractere' should be 'character'

- **Suggestion:** `character`

---

#### 272. Typo: 'corect'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:32`

**Description:** Possible typo found: 'corect' should be 'correct'

- **Suggestion:** `correct`

---

#### 273. Typo: 'caractere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:48`

**Description:** Possible typo found: 'caractere' should be 'character'

- **Suggestion:** `character`

---

#### 274. Typo: 'caractere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:53`

**Description:** Possible typo found: 'caractere' should be 'character'

- **Suggestion:** `character`

---

#### 275. Typo: 'caractere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:53`

**Description:** Possible typo found: 'caractere' should be 'character'

- **Suggestion:** `character`

---

#### 276. Typo: 'caractere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:179`

**Description:** Possible typo found: 'caractere' should be 'character'

- **Suggestion:** `character`

---

#### 277. Typo: 'caractere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:184`

**Description:** Possible typo found: 'caractere' should be 'character'

- **Suggestion:** `character`

---

#### 278. Typo: 'caractere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:198`

**Description:** Possible typo found: 'caractere' should be 'character'

- **Suggestion:** `character`

---

#### 279. Typo: 'caractere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:234`

**Description:** Possible typo found: 'caractere' should be 'character'

- **Suggestion:** `character`

---

#### 280. Typo: 'formate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:261`

**Description:** Possible typo found: 'formate' should be 'format'

- **Suggestion:** `format`

---

#### 281. Typo: 'formate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:279`

**Description:** Possible typo found: 'formate' should be 'format'

- **Suggestion:** `format`

---

#### 282. Typo: 'formate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:288`

**Description:** Possible typo found: 'formate' should be 'format'

- **Suggestion:** `format`

---

#### 283. Typo: 'formate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:293`

**Description:** Possible typo found: 'formate' should be 'format'

- **Suggestion:** `format`

---

#### 284. Typo: 'elemente'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:308`

**Description:** Possible typo found: 'elemente' should be 'element, elements'

- **Suggestion:** `element, elements`

---

#### 285. Typo: 'caractere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:340`

**Description:** Possible typo found: 'caractere' should be 'character'

- **Suggestion:** `character`

---

#### 286. Typo: 'incorect'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:431`

**Description:** Possible typo found: 'incorect' should be 'incorrect'

- **Suggestion:** `incorrect`

---

#### 287. Typo: 'incorect'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:448`

**Description:** Possible typo found: 'incorect' should be 'incorrect'

- **Suggestion:** `incorrect`

---

#### 288. Typo: 'elemente'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\ro\LC_MESSAGES\django.po:525`

**Description:** Possible typo found: 'elemente' should be 'element, elements'

- **Suggestion:** `element, elements`

---

#### 289. Typo: 'parametre'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sk\LC_MESSAGES\django.po:96`

**Description:** Possible typo found: 'parametre' should be 'parameter'

- **Suggestion:** `parameter`

---

#### 290. Typo: 'objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sk\LC_MESSAGES\django.po:425`

**Description:** Possible typo found: 'objekt' should be 'object'

- **Suggestion:** `object`

---

#### 291. Typo: 'objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sk\LC_MESSAGES\django.po:442`

**Description:** Possible typo found: 'objekt' should be 'object'

- **Suggestion:** `object`

---

#### 292. Typo: 'Objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sk\LC_MESSAGES\django.po:452`

**Description:** Possible typo found: 'Objekt' should be 'Object'

- **Suggestion:** `Object`

---

#### 293. Typo: 'sme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:27`

**Description:** Possible typo found: 'sme' should be 'same, seme, some, sms'

- **Suggestion:** `same, seme, some, sms`

---

#### 294. Typo: 'sme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:47`

**Description:** Possible typo found: 'sme' should be 'same, seme, some, sms'

- **Suggestion:** `same, seme, some, sms`

---

#### 295. Typo: 'sme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:52`

**Description:** Possible typo found: 'sme' should be 'same, seme, some, sms'

- **Suggestion:** `same, seme, some, sms`

---

#### 296. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:120`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 297. Typo: 'sme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:161`

**Description:** Possible typo found: 'sme' should be 'same, seme, some, sms'

- **Suggestion:** `same, seme, some, sms`

---

#### 298. Typo: 'sme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:173`

**Description:** Possible typo found: 'sme' should be 'same, seme, some, sms'

- **Suggestion:** `same, seme, some, sms`

---

#### 299. Typo: 'sme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:178`

**Description:** Possible typo found: 'sme' should be 'same, seme, some, sms'

- **Suggestion:** `same, seme, some, sms`

---

#### 300. Typo: 'sme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:311`

**Description:** Possible typo found: 'sme' should be 'same, seme, some, sms'

- **Suggestion:** `same, seme, some, sms`

---

#### 301. Typo: 'sme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:349`

**Description:** Possible typo found: 'sme' should be 'same, seme, some, sms'

- **Suggestion:** `same, seme, some, sms`

---

#### 302. Typo: 'stran'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:408`

**Description:** Possible typo found: 'stran' should be 'strand, strain'

- **Suggestion:** `strand, strain`

---

#### 303. Typo: 'objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:425`

**Description:** Possible typo found: 'objekt' should be 'object'

- **Suggestion:** `object`

---

#### 304. Typo: 'Objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:442`

**Description:** Possible typo found: 'Objekt' should be 'Object'

- **Suggestion:** `Object`

---

#### 305. Typo: 'Objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sl\LC_MESSAGES\django.po:452`

**Description:** Possible typo found: 'Objekt' should be 'Object'

- **Suggestion:** `Object`

---

#### 306. Typo: 'objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sv\LC_MESSAGES\django.po:303`

**Description:** Possible typo found: 'objekt' should be 'object'

- **Suggestion:** `object`

---

#### 307. Typo: 'Objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sv\LC_MESSAGES\django.po:453`

**Description:** Possible typo found: 'Objekt' should be 'Object'

- **Suggestion:** `Object`

---

#### 308. Typo: 'objekt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\sv\LC_MESSAGES\django.po:525`

**Description:** Possible typo found: 'objekt' should be 'object'

- **Suggestion:** `object`

---

#### 309. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:128`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 310. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:165`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 311. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:169`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 312. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:181`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 313. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:186`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 314. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:191`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 315. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:199`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 316. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:319`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 317. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:347`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 318. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:357`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 319. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:362`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 320. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:367`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 321. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:376`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 322. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:536`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 323. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:551`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 324. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:556`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 325. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr\LC_MESSAGES\django.po:561`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 326. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:121`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 327. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:158`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 328. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:162`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 329. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:174`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 330. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:179`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 331. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:184`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 332. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:192`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 333. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:312`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 334. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:340`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 335. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:350`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 336. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:529`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 337. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:544`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 338. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:549`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 339. Typo: 'Bu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\tr_TR\LC_MESSAGES\django.po:554`

**Description:** Possible typo found: 'Bu' should be 'By, Be, But, Bug, Bun, Bud, Buy, Bum'

- **Suggestion:** `By, Be, But, Bug, Bun, Bud, Buy, Bum`

---

#### 340. Typo: 'thay'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\locale\vi\LC_MESSAGES\django.po:279`

**Description:** Possible typo found: 'thay' should be 'they, that'

- **Suggestion:** `they, that`

---

#### 341. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 342. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 343. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 344. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 345. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 346. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 347. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 348. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 349. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 350. Typo: 'eACG'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'eACG' should be 'each'

- **Suggestion:** `each`

---

#### 351. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 352. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 353. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 354. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 355. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 356. Typo: 'cACE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'cACE' should be 'cache'

- **Suggestion:** `cache`

---

#### 357. Typo: 'actived'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Description:** Possible typo found: 'actived' should be 'activated'

- **Suggestion:** `activated`

---

#### 358. Typo: 'tE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'tE' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 359. Typo: 'tE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'tE' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 360. Typo: 'tE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'tE' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 361. Typo: 'tE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'tE' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 362. Typo: 'tE'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'tE' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 363. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 364. Typo: 'iif'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'iif' should be 'if'

- **Suggestion:** `if`

---

#### 365. Typo: 'lenght'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'lenght' should be 'length'

- **Suggestion:** `length`

---

#### 366. Typo: 'filetest'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'filetest' should be 'file test'

- **Suggestion:** `file test`

---

#### 367. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 368. Typo: 'isnt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'isnt' should be 'isn't'

- **Suggestion:** `isn't`

---

#### 369. Typo: 'tring'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'tring' should be 'trying, string, ring'

- **Suggestion:** `trying, string, ring`

---

#### 370. Typo: 'ans'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'ans' should be 'and'

- **Suggestion:** `and`

---

#### 371. Typo: 'alog'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'alog' should be 'along'

- **Suggestion:** `along`

---

#### 372. Typo: 'iput'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'iput' should be 'input'

- **Suggestion:** `input`

---

#### 373. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 374. Typo: 'appen'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'appen' should be 'append, happen, aspen'

- **Suggestion:** `append, happen, aspen`

---

#### 375. Typo: 'asser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'asser' should be 'assert'

- **Suggestion:** `assert`

---

#### 376. Typo: 'describ'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'describ' should be 'describe'

- **Suggestion:** `describe`

---

#### 377. Typo: 'displa'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'displa' should be 'display'

- **Suggestion:** `display`

---

#### 378. Typo: 'doed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'doed' should be 'does'

- **Suggestion:** `does`

---

#### 379. Typo: 'erro'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'erro' should be 'error'

- **Suggestion:** `error`

---

#### 380. Typo: 'fillin'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'fillin' should be 'filling, fill in'

- **Suggestion:** `filling, fill in`

---

#### 381. Typo: 'generat'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'generat' should be 'generate, general'

- **Suggestion:** `generate, general`

---

#### 382. Typo: 'globa'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'globa' should be 'global'

- **Suggestion:** `global`

---

#### 383. Typo: 'hel'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'hel' should be 'help, hell, heal'

- **Suggestion:** `help, hell, heal`

---

#### 384. Typo: 'inpu'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'inpu' should be 'input'

- **Suggestion:** `input`

---

#### 385. Typo: 'mata'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'mata' should be 'meta, mater'

- **Suggestion:** `meta, mater`

---

#### 386. Typo: 'mor'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'mor' should be 'more'

- **Suggestion:** `more`

---

#### 387. Typo: 'retur'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'retur' should be 'return'

- **Suggestion:** `return`

---

#### 388. Typo: 'rotat'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'rotat' should be 'rotate'

- **Suggestion:** `rotate`

---

#### 389. Typo: 'sav'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'sav' should be 'save'

- **Suggestion:** `save`

---

#### 390. Typo: 'seperate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'seperate' should be 'separate'

- **Suggestion:** `separate`

---

#### 391. Typo: 'summar'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'summar' should be 'summary, summer'

- **Suggestion:** `summary, summer`

---

#### 392. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 393. Typo: 'versio'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'versio' should be 'version'

- **Suggestion:** `version`

---

#### 394. Typo: 'windo'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'windo' should be 'window'

- **Suggestion:** `window`

---

#### 395. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 396. Typo: 'checkt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'checkt' should be 'checked'

- **Suggestion:** `checked`

---

#### 397. Typo: 'debugg'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'debugg' should be 'debug'

- **Suggestion:** `debug`

---

#### 398. Typo: 'fo'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'fo' should be 'of, for, to, do, go'

- **Suggestion:** `of, for, to, do, go`

---

#### 399. Typo: 'sav'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'sav' should be 'save'

- **Suggestion:** `save`

---

#### 400. Typo: 'scrip'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'scrip' should be 'script'

- **Suggestion:** `script`

---

#### 401. Typo: 'scripte'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'scripte' should be 'script, scripted'

- **Suggestion:** `script, scripted`

---

#### 402. Typo: 'sme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'sme' should be 'same, seme, some, sms'

- **Suggestion:** `same, seme, some, sms`

---

#### 403. Typo: 'tabe'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'tabe' should be 'table, tab'

- **Suggestion:** `table, tab`

---

#### 404. Typo: 'tabl'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'tabl' should be 'table'

- **Suggestion:** `table`

---

#### 405. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 406. Typo: 'vie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'vie' should be 'via'

- **Suggestion:** `via`

---

#### 407. Typo: 'windo'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'windo' should be 'window'

- **Suggestion:** `window`

---

#### 408. Typo: 'enew'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'enew' should be 'new'

- **Suggestion:** `new`

---

#### 409. Typo: 'assymetry'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'assymetry' should be 'asymmetry'

- **Suggestion:** `asymmetry`

---

#### 410. Typo: 'iif'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'iif' should be 'if'

- **Suggestion:** `if`

---

#### 411. Typo: 'isnt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'isnt' should be 'isn't'

- **Suggestion:** `isn't`

---

#### 412. Typo: 'notin'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'notin' should be 'noting, not in, notion'

- **Suggestion:** `noting, not in, notion`

---

#### 413. Typo: 'aas'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'aas' should be 'ass, as'

- **Suggestion:** `ass, as`

---

#### 414. Typo: 'daa'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'daa' should be 'data'

- **Suggestion:** `data`

---

#### 415. Typo: 'struc'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'struc' should be 'struct'

- **Suggestion:** `struct`

---

#### 416. Typo: 'juxt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'juxt' should be 'just'

- **Suggestion:** `just`

---

#### 417. Typo: 'rcall'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'rcall' should be 'recall'

- **Suggestion:** `recall`

---

#### 418. Typo: 'seh'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'seh' should be 'she'

- **Suggestion:** `she`

---

#### 419. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 420. Typo: 'dispaly'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'dispaly' should be 'display'

- **Suggestion:** `display`

---

#### 421. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 422. Typo: 'BraKet'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'BraKet' should be 'bracket, brake'

- **Suggestion:** `bracket, brake`

---

#### 423. Typo: 'Ket'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Description:** Possible typo found: 'Ket' should be 'Key, Kept'

- **Suggestion:** `Key, Kept`

---

#### 424. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:2`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 425. Typo: 'promt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:2`

**Description:** Possible typo found: 'promt' should be 'prompt'

- **Suggestion:** `prompt`

---

#### 426. Typo: 'SectionIn'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\docs\js\highlight.pack.js:2`

**Description:** Possible typo found: 'SectionIn' should be 'sectioning, section in'

- **Suggestion:** `sectioning, section in`

---

#### 427. Typo: 'build-in'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\coreapi-0.1.1.js:1157`

**Description:** Possible typo found: 'build-in' should be 'built-in'

- **Suggestion:** `built-in`

---

#### 428. Typo: 'ue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'ue' should be 'use, due'

- **Suggestion:** `use, due`

---

#### 429. Typo: 'ue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'ue' should be 'use, due'

- **Suggestion:** `use, due`

---

#### 430. Typo: 'ue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'ue' should be 'use, due'

- **Suggestion:** `use, due`

---

#### 431. Typo: 'ue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'ue' should be 'use, due'

- **Suggestion:** `use, due`

---

#### 432. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 433. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 434. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 435. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 436. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 437. Typo: 'Te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'Te' should be 'The, Be, We, To'

- **Suggestion:** `The, Be, We, To`

---

#### 438. Typo: 'Te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'Te' should be 'The, Be, We, To'

- **Suggestion:** `The, Be, We, To`

---

#### 439. Typo: 'Te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'Te' should be 'The, Be, We, To'

- **Suggestion:** `The, Be, We, To`

---

#### 440. Typo: 'Ue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'Ue' should be 'Use, Due'

- **Suggestion:** `Use, Due`

---

#### 441. Typo: 'ot'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'ot' should be 'to, of, or, not, it'

- **Suggestion:** `to, of, or, not, it`

---

#### 442. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 443. Typo: 'ot'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'ot' should be 'to, of, or, not, it'

- **Suggestion:** `to, of, or, not, it`

---

#### 444. Typo: 'Ue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'Ue' should be 'Use, Due'

- **Suggestion:** `Use, Due`

---

#### 445. Typo: 'ot'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'ot' should be 'to, of, or, not, it'

- **Suggestion:** `to, of, or, not, it`

---

#### 446. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 447. Typo: 'ue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'ue' should be 'use, due'

- **Suggestion:** `use, due`

---

#### 448. Typo: 'ue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'ue' should be 'use, due'

- **Suggestion:** `use, due`

---

#### 449. Typo: 'Ot'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'Ot' should be 'To, Of, Or, Not, It'

- **Suggestion:** `To, Of, Or, Not, It`

---

#### 450. Typo: 'Ot'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Description:** Possible typo found: 'Ot' should be 'To, Of, Or, Not, It'

- **Suggestion:** `To, Of, Or, Not, It`

---

#### 451. Typo: 'isnt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\rest_framework\static\rest_framework\js\prettify-min.js:24`

**Description:** Possible typo found: 'isnt' should be 'isn't'

- **Suggestion:** `isn't`

---

#### 452. Typo: 'fo'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_encode__django-rest-framework_fsudw3ny\django-rest-framework\tests\test_routers.py:293`

**Description:** Possible typo found: 'fo' should be 'of, for, to, do, go'

- **Suggestion:** `of, for, to, do, go`

---

## Notes

- All secrets are **redacted** in this report for safety.
- Remediation instructions are AI-generated and should be reviewed by a human.
- This report is generated for educational purposes (MIT AI+X PBL).

*Report generated on 2026-01-07 07:03:46 UTC*