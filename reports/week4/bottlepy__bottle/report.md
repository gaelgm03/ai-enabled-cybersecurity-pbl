# Security Scan Report

**Scan ID:** `scan-20260107-070355-89f02b34`  
**Timestamp:** 2026-01-07T07:03:55.199868Z  
**Target:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle`

---

## Summary

**Total Findings:** 311

### By Severity

| Severity | Count |
|----------|-------|
| 🟠 High | 11 |
| 🟢 Low | 300 |

### By Type

| Type | Count |
|------|-------|
| 📝 Typo | 300 |
| 🔐 Secret | 11 |

---

## Findings

### 🔐 Secret Issues

#### 1. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\bottle.py:2894`
- **Match (redacted):** `toun********lit(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 2. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\bottle.py:3079`
- **Match (redacted):** `requ****auth`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 3. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial.rst:246`
- **Match (redacted):** `requ********word`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 4. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial.rst:459`
- **Match (redacted):** `requ********get(`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 5. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial.rst:461`
- **Match (redacted):** `some*******-key`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 6. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial.rst:468`
- **Match (redacted):** `some*******-key`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 7. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial.rst:615`
- **Match (redacted):** `requ********word`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 8. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_securecookies.py:30`
- **Match (redacted):** `self****ret)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 9. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_securecookies.py:33`
- **Match (redacted):** `self****ret)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 10. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_securecookies.py:37`
- **Match (redacted):** `self****ret)`

**Description:** Detected potential secret matching Password/Secret pattern

---

#### 11. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_securecookies.py:40`
- **Match (redacted):** `self****ret)`

**Description:** Detected potential secret matching Password/Secret pattern

---

### 📝 Typo Issues

#### 1. Typo: 'childs'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\bottle.py:752`

**Description:** Possible typo found: 'childs' should be 'children, child's'

- **Suggestion:** `children, child's`

---

#### 2. Typo: 'build-in'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\bottle.py:2475`

**Description:** Possible typo found: 'build-in' should be 'built-in'

- **Suggestion:** `built-in`

---

#### 3. Typo: 'clen'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\bottle.py:2814`

**Description:** Possible typo found: 'clen' should be 'clean, clan'

- **Suggestion:** `clean, clan`

---

#### 4. Typo: 'clen'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\bottle.py:2820`

**Description:** Possible typo found: 'clen' should be 'clean, clan'

- **Suggestion:** `clean, clan`

---

#### 5. Typo: 'clen'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\bottle.py:2840`

**Description:** Possible typo found: 'clen' should be 'clean, clan'

- **Suggestion:** `clean, clan`

---

#### 6. Typo: 'clen'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\bottle.py:2845`

**Description:** Possible typo found: 'clen' should be 'clean, clan'

- **Suggestion:** `clean, clan`

---

#### 7. Typo: 'cutted'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\bottle.py:3201`

**Description:** Possible typo found: 'cutted' should be 'cutter, gutted, cut'

- **Suggestion:** `cutter, gutted, cut`

---

#### 8. Typo: 're-use'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\bottle.py:4212`

**Description:** Possible typo found: 're-use' should be 'reuse'

- **Suggestion:** `reuse`

---

#### 9. Typo: 'loosly'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\changelog.rst:8`

**Description:** Possible typo found: 'loosly' should be 'loosely'

- **Suggestion:** `loosely`

---

#### 10. Typo: 'Whats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\changelog.rst:211`

**Description:** Possible typo found: 'Whats' should be 'What's'

- **Suggestion:** `What's`

---

#### 11. Typo: 'deprectated'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\deployment.rst:77`

**Description:** Possible typo found: 'deprectated' should be 'deprecated'

- **Suggestion:** `deprecated`

---

#### 12. Typo: 'absolut'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\faq.rst:41`

**Description:** Possible typo found: 'absolut' should be 'absolute'

- **Suggestion:** `absolute`

---

#### 13. Typo: 'appropiate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\faq.rst:271`

**Description:** Possible typo found: 'appropiate' should be 'appropriate'

- **Suggestion:** `appropriate`

---

#### 14. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial.rst:156`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 15. Typo: 'absolut'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial.rst:277`

**Description:** Possible typo found: 'absolut' should be 'absolute'

- **Suggestion:** `absolute`

---

#### 16. Typo: 'appropiate'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial.rst:659`

**Description:** Possible typo found: 'appropiate' should be 'appropriate'

- **Suggestion:** `appropriate`

---

#### 17. Typo: 'publically'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:33`

**Description:** Possible typo found: 'publically' should be 'publicly'

- **Suggestion:** `publicly`

---

#### 18. Typo: 'validtion'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:33`

**Description:** Possible typo found: 'validtion' should be 'validation'

- **Suggestion:** `validation`

---

#### 19. Typo: 'formated'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:52`

**Description:** Possible typo found: 'formated' should be 'formatted'

- **Suggestion:** `formatted`

---

#### 20. Typo: 'build-in'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:149`

**Description:** Possible typo found: 'build-in' should be 'built-in'

- **Suggestion:** `built-in`

---

#### 21. Typo: 'formated'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:200`

**Description:** Possible typo found: 'formated' should be 'formatted'

- **Suggestion:** `formatted`

---

#### 22. Typo: 'build-in'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:238`

**Description:** Possible typo found: 'build-in' should be 'built-in'

- **Suggestion:** `built-in`

---

#### 23. Typo: 'couse'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:317`

**Description:** Possible typo found: 'couse' should be 'course, cause'

- **Suggestion:** `course, cause`

---

#### 24. Typo: 'similat'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:473`

**Description:** Possible typo found: 'similat' should be 'similar'

- **Suggestion:** `similar`

---

#### 25. Typo: 'relativ'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:532`

**Description:** Possible typo found: 'relativ' should be 'relative'

- **Suggestion:** `relative`

---

#### 26. Typo: 'build-in'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:551`

**Description:** Possible typo found: 'build-in' should be 'built-in'

- **Suggestion:** `built-in`

---

#### 27. Typo: 'modifiying'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:579`

**Description:** Possible typo found: 'modifiying' should be 'modifying'

- **Suggestion:** `modifying`

---

#### 28. Typo: 'build-in'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:605`

**Description:** Possible typo found: 'build-in' should be 'built-in'

- **Suggestion:** `built-in`

---

#### 29. Typo: 'excuted'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:616`

**Description:** Possible typo found: 'excuted' should be 'executed'

- **Suggestion:** `executed`

---

#### 30. Typo: 'build-in'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:621`

**Description:** Possible typo found: 'build-in' should be 'built-in'

- **Suggestion:** `built-in`

---

#### 31. Typo: 'build-in'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:623`

**Description:** Possible typo found: 'build-in' should be 'built-in'

- **Suggestion:** `built-in`

---

#### 32. Typo: 'build-in'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:627`

**Description:** Possible typo found: 'build-in' should be 'built-in'

- **Suggestion:** `built-in`

---

#### 33. Typo: 'utilizin'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\tutorial_app.rst:669`

**Description:** Possible typo found: 'utilizin' should be 'utilizing'

- **Suggestion:** `utilizing`

---

#### 34. Typo: 're-usable'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\plugins\index.rst:13`

**Description:** Possible typo found: 're-usable' should be 'reusable'

- **Suggestion:** `reusable`

---

#### 35. Typo: 'Referenz'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\api.po:24`

**Description:** Possible typo found: 'Referenz' should be 'Reference'

- **Suggestion:** `Reference`

---

#### 36. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\api.po:30`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 37. Typo: 'childs'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\api.po:624`

**Description:** Possible typo found: 'childs' should be 'children, child's'

- **Suggestion:** `children, child's`

---

#### 38. Typo: 'accpets'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\changelog.po:498`

**Description:** Possible typo found: 'accpets' should be 'accepts'

- **Suggestion:** `accepts`

---

#### 39. Typo: 'Whats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\changelog.po:521`

**Description:** Possible typo found: 'Whats' should be 'What's'

- **Suggestion:** `What's`

---

#### 40. Typo: 'modue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\configuration.po:226`

**Description:** Possible typo found: 'modue' should be 'module'

- **Suggestion:** `module`

---

#### 41. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\contact.po:50`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 42. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\contact.po:64`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 43. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\contact.po:66`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 44. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\contact.po:66`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 45. Typo: 'Dokument'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:30`

**Description:** Possible typo found: 'Dokument' should be 'Document'

- **Suggestion:** `Document`

---

#### 46. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:30`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 47. Typo: 'Wege'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:40`

**Description:** Possible typo found: 'Wege' should be 'Wedge'

- **Suggestion:** `Wedge`

---

#### 48. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:53`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 49. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:60`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 50. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:99`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 51. Typo: 'Archiv'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:99`

**Description:** Possible typo found: 'Archiv' should be 'Archive'

- **Suggestion:** `Archive`

---

#### 52. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:99`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 53. Typo: 'Paket'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:118`

**Description:** Possible typo found: 'Paket' should be 'Packet'

- **Suggestion:** `Packet`

---

#### 54. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:128`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 55. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:128`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 56. Typo: 'alle'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:128`

**Description:** Possible typo found: 'alle' should be 'all, alley'

- **Suggestion:** `all, alley`

---

#### 57. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:128`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 58. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:140`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 59. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:140`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 60. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:155`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 61. Typo: 'hart'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:155`

**Description:** Possible typo found: 'hart' should be 'heart, harm'

- **Suggestion:** `heart, harm`

---

#### 62. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:155`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 63. Typo: 'Applikation'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:167`

**Description:** Possible typo found: 'Applikation' should be 'Application'

- **Suggestion:** `Application`

---

#### 64. Typo: 'offen'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:178`

**Description:** Possible typo found: 'offen' should be 'often'

- **Suggestion:** `often`

---

#### 65. Typo: 'sie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:178`

**Description:** Possible typo found: 'sie' should be 'size, sigh, side'

- **Suggestion:** `size, sigh, side`

---

#### 66. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:186`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 67. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:196`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 68. Typo: 'Alle'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:196`

**Description:** Possible typo found: 'Alle' should be 'All, Alley'

- **Suggestion:** `All, Alley`

---

#### 69. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:211`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 70. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:211`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 71. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:211`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 72. Typo: 'Alle'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:222`

**Description:** Possible typo found: 'Alle' should be 'All, Alley'

- **Suggestion:** `All, Alley`

---

#### 73. Typo: 'sie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:222`

**Description:** Possible typo found: 'sie' should be 'size, sigh, side'

- **Suggestion:** `size, sigh, side`

---

#### 74. Typo: 'Thats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:233`

**Description:** Possible typo found: 'Thats' should be 'That's'

- **Suggestion:** `That's`

---

#### 75. Typo: 'branche'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:235`

**Description:** Possible typo found: 'branche' should be 'branch, branches, branched'

- **Suggestion:** `branch, branches, branched`

---

#### 76. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:235`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 77. Typo: 'Ende'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:235`

**Description:** Possible typo found: 'Ende' should be 'End'

- **Suggestion:** `End`

---

#### 78. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:267`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 79. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:267`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 80. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:267`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 81. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:267`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 82. Typo: 'alle'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:281`

**Description:** Possible typo found: 'alle' should be 'all, alley'

- **Suggestion:** `all, alley`

---

#### 83. Typo: 'applyed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:286`

**Description:** Possible typo found: 'applyed' should be 'applied'

- **Suggestion:** `applied`

---

#### 84. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:288`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 85. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:288`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 86. Typo: 'sie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:288`

**Description:** Possible typo found: 'sie' should be 'size, sigh, side'

- **Suggestion:** `size, sigh, side`

---

#### 87. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:288`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 88. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:288`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 89. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:295`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 90. Typo: 'passt'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:295`

**Description:** Possible typo found: 'passt' should be 'past, passed'

- **Suggestion:** `past, passed`

---

#### 91. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:306`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 92. Typo: 'manuell'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:306`

**Description:** Possible typo found: 'manuell' should be 'manual'

- **Suggestion:** `manual`

---

#### 93. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:317`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 94. Typo: 'Als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:325`

**Description:** Possible typo found: 'Als' should be 'Also'

- **Suggestion:** `Also`

---

#### 95. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:325`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 96. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:333`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 97. Typo: 'lokal'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:333`

**Description:** Possible typo found: 'lokal' should be 'local'

- **Suggestion:** `local`

---

#### 98. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:342`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 99. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:342`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 100. Typo: 'sie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:342`

**Description:** Possible typo found: 'sie' should be 'size, sigh, side'

- **Suggestion:** `size, sigh, side`

---

#### 101. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:342`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 102. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:349`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 103. Typo: 'sie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:361`

**Description:** Possible typo found: 'sie' should be 'size, sigh, side'

- **Suggestion:** `size, sigh, side`

---

#### 104. Typo: 'sie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:361`

**Description:** Possible typo found: 'sie' should be 'size, sigh, side'

- **Suggestion:** `size, sigh, side`

---

#### 105. Typo: 'alle'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:367`

**Description:** Possible typo found: 'alle' should be 'all, alley'

- **Suggestion:** `all, alley`

---

#### 106. Typo: 'committe'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:367`

**Description:** Possible typo found: 'committe' should be 'committee'

- **Suggestion:** `committee`

---

#### 107. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:367`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 108. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:383`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 109. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:383`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 110. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:383`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 111. Typo: 'alle'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:383`

**Description:** Possible typo found: 'alle' should be 'all, alley'

- **Suggestion:** `all, alley`

---

#### 112. Typo: 'committe'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:383`

**Description:** Possible typo found: 'committe' should be 'committee'

- **Suggestion:** `committee`

---

#### 113. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:389`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 114. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:389`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 115. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:398`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 116. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:398`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 117. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:414`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 118. Typo: 'Branche'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:420`

**Description:** Possible typo found: 'Branche' should be 'Branch, Branches, Branched'

- **Suggestion:** `Branch, Branches, Branched`

---

#### 119. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:430`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 120. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\development.po:436`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 121. Typo: 'Ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:32`

**Description:** Possible typo found: 'Ist' should be 'Is, It, Its, It's, Sit, List'

- **Suggestion:** `Is, It, Its, It's, Sit, List`

---

#### 122. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:43`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 123. Typo: 'sie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:43`

**Description:** Possible typo found: 'sie' should be 'size, sigh, side'

- **Suggestion:** `size, sigh, side`

---

#### 124. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:43`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 125. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:43`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 126. Typo: 'Probleme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:47`

**Description:** Possible typo found: 'Probleme' should be 'Problem'

- **Suggestion:** `Problem`

---

#### 127. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:59`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 128. Typo: 'Probleme'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:81`

**Description:** Possible typo found: 'Probleme' should be 'Problem'

- **Suggestion:** `Problem`

---

#### 129. Typo: 'Adresse'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:91`

**Description:** Possible typo found: 'Adresse' should be 'Address'

- **Suggestion:** `Address`

---

#### 130. Typo: 'lokal'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:91`

**Description:** Possible typo found: 'lokal' should be 'local'

- **Suggestion:** `local`

---

#### 131. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:91`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 132. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:91`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 133. Typo: 'lokale'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:91`

**Description:** Possible typo found: 'lokale' should be 'locale'

- **Suggestion:** `locale`

---

#### 134. Typo: 'deines'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:91`

**Description:** Possible typo found: 'deines' should be 'denies, defines, defined'

- **Suggestion:** `denies, defines, defined`

---

#### 135. Typo: 'Proxys'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:91`

**Description:** Possible typo found: 'Proxys' should be 'Proxies'

- **Suggestion:** `Proxies`

---

#### 136. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\faq.po:91`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 137. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\plugindev.po:212`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 138. Typo: 'infastructure'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\recipes.po:291`

**Description:** Possible typo found: 'infastructure' should be 'infrastructure'

- **Suggestion:** `infrastructure`

---

#### 139. Typo: 'Ende'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:37`

**Description:** Possible typo found: 'Ende' should be 'End'

- **Suggestion:** `End`

---

#### 140. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:37`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 141. Typo: 'als'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:37`

**Description:** Possible typo found: 'als' should be 'also'

- **Suggestion:** `also`

---

#### 142. Typo: 'Referenz'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:37`

**Description:** Possible typo found: 'Referenz' should be 'Reference'

- **Suggestion:** `Reference`

---

#### 143. Typo: 'Sie'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:37`

**Description:** Possible typo found: 'Sie' should be 'Size, Sigh, Side'

- **Suggestion:** `Size, Sigh, Side`

---

#### 144. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:37`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 145. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:37`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 146. Typo: 'alle'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:57`

**Description:** Possible typo found: 'alle' should be 'all, alley'

- **Suggestion:** `all, alley`

---

#### 147. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:57`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 148. Typo: 'Oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:69`

**Description:** Possible typo found: 'Oder' should be 'Order, Older, Coder, Odder, Odor, Over, Doer'

- **Suggestion:** `Order, Older, Coder, Odder, Odor, Over, Doer`

---

#### 149. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:69`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 150. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:80`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 151. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:86`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 152. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:96`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 153. Typo: 'Funktion'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:96`

**Description:** Possible typo found: 'Funktion' should be 'Function'

- **Suggestion:** `Function`

---

#### 154. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:96`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 155. Typo: 'startet'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:106`

**Description:** Possible typo found: 'startet' should be 'started'

- **Suggestion:** `started`

---

#### 156. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:106`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 157. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:106`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 158. Typo: 'deine'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:106`

**Description:** Possible typo found: 'deine' should be 'define'

- **Suggestion:** `define`

---

#### 159. Typo: 'ans'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:106`

**Description:** Possible typo found: 'ans' should be 'and'

- **Suggestion:** `and`

---

#### 160. Typo: 're-usable'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\de_DE\LC_MESSAGES\tutorial.po:1093`

**Description:** Possible typo found: 're-usable' should be 'reusable'

- **Suggestion:** `reusable`

---

#### 161. Typo: 'childs'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\api.po:622`

**Description:** Possible typo found: 'childs' should be 'children, child's'

- **Suggestion:** `children, child's`

---

#### 162. Typo: 'accpets'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\changelog.po:498`

**Description:** Possible typo found: 'accpets' should be 'accepts'

- **Suggestion:** `accepts`

---

#### 163. Typo: 'Whats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\changelog.po:521`

**Description:** Possible typo found: 'Whats' should be 'What's'

- **Suggestion:** `What's`

---

#### 164. Typo: 'modue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\configuration.po:226`

**Description:** Possible typo found: 'modue' should be 'module'

- **Suggestion:** `module`

---

#### 165. Typo: 'ans'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:39`

**Description:** Possible typo found: 'ans' should be 'and'

- **Suggestion:** `and`

---

#### 166. Typo: 'langage'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:39`

**Description:** Possible typo found: 'langage' should be 'language'

- **Suggestion:** `language`

---

#### 167. Typo: 'projet'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:50`

**Description:** Possible typo found: 'projet' should be 'project'

- **Suggestion:** `project`

---

#### 168. Typo: 'projet'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:50`

**Description:** Possible typo found: 'projet' should be 'project'

- **Suggestion:** `project`

---

#### 169. Typo: 'projet'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:50`

**Description:** Possible typo found: 'projet' should be 'project'

- **Suggestion:** `project`

---

#### 170. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:64`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 171. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:66`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 172. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:66`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 173. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:68`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 174. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:68`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 175. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\contact.po:68`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 176. Typo: 'Thats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\development.po:232`

**Description:** Possible typo found: 'Thats' should be 'That's'

- **Suggestion:** `That's`

---

#### 177. Typo: 'applyed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\development.po:285`

**Description:** Possible typo found: 'applyed' should be 'applied'

- **Suggestion:** `applied`

---

#### 178. Typo: 'Exemple'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\index.po:58`

**Description:** Possible typo found: 'Exemple' should be 'Example'

- **Suggestion:** `Example`

---

#### 179. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\plugindev.po:212`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 180. Typo: 'infastructure'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\recipes.po:291`

**Description:** Possible typo found: 'infastructure' should be 'infrastructure'

- **Suggestion:** `infrastructure`

---

#### 181. Typo: 're-usable'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\fr\LC_MESSAGES\tutorial.po:1091`

**Description:** Possible typo found: 're-usable' should be 'reusable'

- **Suggestion:** `reusable`

---

#### 182. Typo: 'childs'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\api.po:622`

**Description:** Possible typo found: 'childs' should be 'children, child's'

- **Suggestion:** `children, child's`

---

#### 183. Typo: 'accpets'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\changelog.po:498`

**Description:** Possible typo found: 'accpets' should be 'accepts'

- **Suggestion:** `accepts`

---

#### 184. Typo: 'Whats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\changelog.po:521`

**Description:** Possible typo found: 'Whats' should be 'What's'

- **Suggestion:** `What's`

---

#### 185. Typo: 'modue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\configuration.po:226`

**Description:** Possible typo found: 'modue' should be 'module'

- **Suggestion:** `module`

---

#### 186. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\contact.po:63`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 187. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\contact.po:65`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 188. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\contact.po:65`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 189. Typo: 'Thats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\development.po:232`

**Description:** Possible typo found: 'Thats' should be 'That's'

- **Suggestion:** `That's`

---

#### 190. Typo: 'applyed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\development.po:285`

**Description:** Possible typo found: 'applyed' should be 'applied'

- **Suggestion:** `applied`

---

#### 191. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\plugindev.po:212`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 192. Typo: 'infastructure'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\recipes.po:291`

**Description:** Possible typo found: 'infastructure' should be 'infrastructure'

- **Suggestion:** `infrastructure`

---

#### 193. Typo: 're-usable'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ja_JP\LC_MESSAGES\tutorial.po:1092`

**Description:** Possible typo found: 're-usable' should be 'reusable'

- **Suggestion:** `reusable`

---

#### 194. Typo: 'childs'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\api.po:624`

**Description:** Possible typo found: 'childs' should be 'children, child's'

- **Suggestion:** `children, child's`

---

#### 195. Typo: 'accpets'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\changelog.po:498`

**Description:** Possible typo found: 'accpets' should be 'accepts'

- **Suggestion:** `accepts`

---

#### 196. Typo: 'Whats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\changelog.po:521`

**Description:** Possible typo found: 'Whats' should be 'What's'

- **Suggestion:** `What's`

---

#### 197. Typo: 'modue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\configuration.po:226`

**Description:** Possible typo found: 'modue' should be 'module'

- **Suggestion:** `module`

---

#### 198. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\contact.po:63`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 199. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\contact.po:65`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 200. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\contact.po:65`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 201. Typo: 'Thats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\development.po:232`

**Description:** Possible typo found: 'Thats' should be 'That's'

- **Suggestion:** `That's`

---

#### 202. Typo: 'applyed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\development.po:285`

**Description:** Possible typo found: 'applyed' should be 'applied'

- **Suggestion:** `applied`

---

#### 203. Typo: 'leve'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\index.po:33`

**Description:** Possible typo found: 'leve' should be 'level, levee'

- **Suggestion:** `level, levee`

---

#### 204. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\plugindev.po:212`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 205. Typo: 'infastructure'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\recipes.po:291`

**Description:** Possible typo found: 'infastructure' should be 'infrastructure'

- **Suggestion:** `infrastructure`

---

#### 206. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\tutorial.po:37`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 207. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\tutorial.po:37`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 208. Typo: 'vai'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\tutorial.po:57`

**Description:** Possible typo found: 'vai' should be 'via, vie'

- **Suggestion:** `via, vie`

---

#### 209. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\tutorial.po:57`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 210. Typo: 'prefere'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\tutorial.po:57`

**Description:** Possible typo found: 'prefere' should be 'prefer, preferred'

- **Suggestion:** `prefer, preferred`

---

#### 211. Typo: 'ser'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\tutorial.po:57`

**Description:** Possible typo found: 'ser' should be 'set'

- **Suggestion:** `set`

---

#### 212. Typo: 'vai'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\tutorial.po:86`

**Description:** Possible typo found: 'vai' should be 'via, vie'

- **Suggestion:** `via, vie`

---

#### 213. Typo: 're-usable'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\tutorial.po:1093`

**Description:** Possible typo found: 're-usable' should be 'reusable'

- **Suggestion:** `reusable`

---

#### 214. Typo: 'returend'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\api.po:400`

**Description:** Possible typo found: 'returend' should be 'returned'

- **Suggestion:** `returned`

---

#### 215. Typo: 'accpets'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\changelog.po:239`

**Description:** Possible typo found: 'accpets' should be 'accepts'

- **Suggestion:** `accepts`

---

#### 216. Typo: 'Whats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\changelog.po:262`

**Description:** Possible typo found: 'Whats' should be 'What's'

- **Suggestion:** `What's`

---

#### 217. Typo: 'Autor'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\contact.po:19`

**Description:** Possible typo found: 'Autor' should be 'Author'

- **Suggestion:** `Author`

---

#### 218. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\contact.po:57`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 219. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\contact.po:59`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 220. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\contact.po:59`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 221. Typo: 'Thats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\development.po:231`

**Description:** Possible typo found: 'Thats' should be 'That's'

- **Suggestion:** `That's`

---

#### 222. Typo: 'applyed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\development.po:284`

**Description:** Possible typo found: 'applyed' should be 'applied'

- **Suggestion:** `applied`

---

#### 223. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\plugindev.po:206`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 224. Typo: 'virtaully'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\plugindev.po:341`

**Description:** Possible typo found: 'virtaully' should be 'virtually'

- **Suggestion:** `virtually`

---

#### 225. Typo: 'infastructure'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\recipes.po:264`

**Description:** Possible typo found: 'infastructure' should be 'infrastructure'

- **Suggestion:** `infrastructure`

---

#### 226. Typo: 're-usable'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\tutorial.po:1132`

**Description:** Possible typo found: 're-usable' should be 'reusable'

- **Suggestion:** `reusable`

---

#### 227. Typo: 'beeing'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\tutorial.po:1284`

**Description:** Possible typo found: 'beeing' should be 'being, been'

- **Suggestion:** `being, been`

---

#### 228. Typo: 'progess'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\tutorial_app.po:20`

**Description:** Possible typo found: 'progess' should be 'progress'

- **Suggestion:** `progress`

---

#### 229. Typo: 'databse'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\tutorial_app.po:40`

**Description:** Possible typo found: 'databse' should be 'database'

- **Suggestion:** `database`

---

#### 230. Typo: 'adress'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\pt_BR\LC_MESSAGES\_pot\tutorial_app.po:751`

**Description:** Possible typo found: 'adress' should be 'address'

- **Suggestion:** `address`

---

#### 231. Typo: 'childs'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\api.po:622`

**Description:** Possible typo found: 'childs' should be 'children, child's'

- **Suggestion:** `children, child's`

---

#### 232. Typo: 'accpets'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\changelog.po:498`

**Description:** Possible typo found: 'accpets' should be 'accepts'

- **Suggestion:** `accepts`

---

#### 233. Typo: 'Whats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\changelog.po:521`

**Description:** Possible typo found: 'Whats' should be 'What's'

- **Suggestion:** `What's`

---

#### 234. Typo: 'modue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\configuration.po:226`

**Description:** Possible typo found: 'modue' should be 'module'

- **Suggestion:** `module`

---

#### 235. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\contact.po:63`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 236. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\contact.po:65`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 237. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\contact.po:65`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 238. Typo: 'Thats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\development.po:232`

**Description:** Possible typo found: 'Thats' should be 'That's'

- **Suggestion:** `That's`

---

#### 239. Typo: 'applyed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\development.po:285`

**Description:** Possible typo found: 'applyed' should be 'applied'

- **Suggestion:** `applied`

---

#### 240. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\plugindev.po:212`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 241. Typo: 'infastructure'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\recipes.po:291`

**Description:** Possible typo found: 'infastructure' should be 'infrastructure'

- **Suggestion:** `infrastructure`

---

#### 242. Typo: 're-usable'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\ru_RU\LC_MESSAGES\tutorial.po:1092`

**Description:** Possible typo found: 're-usable' should be 'reusable'

- **Suggestion:** `reusable`

---

#### 243. Typo: 'childs'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\api.po:623`

**Description:** Possible typo found: 'childs' should be 'children, child's'

- **Suggestion:** `children, child's`

---

#### 244. Typo: 'accpets'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\changelog.po:498`

**Description:** Possible typo found: 'accpets' should be 'accepts'

- **Suggestion:** `accepts`

---

#### 245. Typo: 'Whats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\changelog.po:521`

**Description:** Possible typo found: 'Whats' should be 'What's'

- **Suggestion:** `What's`

---

#### 246. Typo: 'modue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\configuration.po:226`

**Description:** Possible typo found: 'modue' should be 'module'

- **Suggestion:** `module`

---

#### 247. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\contact.po:63`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 248. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\contact.po:65`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 249. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\contact.po:65`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 250. Typo: 'Thats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\development.po:232`

**Description:** Possible typo found: 'Thats' should be 'That's'

- **Suggestion:** `That's`

---

#### 251. Typo: 'applyed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\development.po:285`

**Description:** Possible typo found: 'applyed' should be 'applied'

- **Suggestion:** `applied`

---

#### 252. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\plugindev.po:212`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 253. Typo: 'infastructure'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\recipes.po:291`

**Description:** Possible typo found: 'infastructure' should be 'infrastructure'

- **Suggestion:** `infrastructure`

---

#### 254. Typo: 're-usable'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\tutorial.po:1091`

**Description:** Possible typo found: 're-usable' should be 'reusable'

- **Suggestion:** `reusable`

---

#### 255. Typo: 'unistall'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\tutorial.po:1173`

**Description:** Possible typo found: 'unistall' should be 'uninstall'

- **Suggestion:** `uninstall`

---

#### 256. Typo: 'returend'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\api.po:400`

**Description:** Possible typo found: 'returend' should be 'returned'

- **Suggestion:** `returned`

---

#### 257. Typo: 'accpets'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\changelog.po:239`

**Description:** Possible typo found: 'accpets' should be 'accepts'

- **Suggestion:** `accepts`

---

#### 258. Typo: 'Whats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\changelog.po:262`

**Description:** Possible typo found: 'Whats' should be 'What's'

- **Suggestion:** `What's`

---

#### 259. Typo: 'Autor'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\contact.po:19`

**Description:** Possible typo found: 'Autor' should be 'Author'

- **Suggestion:** `Author`

---

#### 260. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\contact.po:57`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 261. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\contact.po:59`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 262. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\contact.po:59`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 263. Typo: 'Thats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\development.po:231`

**Description:** Possible typo found: 'Thats' should be 'That's'

- **Suggestion:** `That's`

---

#### 264. Typo: 'applyed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\development.po:284`

**Description:** Possible typo found: 'applyed' should be 'applied'

- **Suggestion:** `applied`

---

#### 265. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\plugindev.po:206`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 266. Typo: 'virtaully'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\plugindev.po:341`

**Description:** Possible typo found: 'virtaully' should be 'virtually'

- **Suggestion:** `virtually`

---

#### 267. Typo: 'infastructure'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\recipes.po:264`

**Description:** Possible typo found: 'infastructure' should be 'infrastructure'

- **Suggestion:** `infrastructure`

---

#### 268. Typo: 're-usable'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\tutorial.po:1132`

**Description:** Possible typo found: 're-usable' should be 'reusable'

- **Suggestion:** `reusable`

---

#### 269. Typo: 'beeing'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\tutorial.po:1284`

**Description:** Possible typo found: 'beeing' should be 'being, been'

- **Suggestion:** `being, been`

---

#### 270. Typo: 'progess'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\tutorial_app.po:20`

**Description:** Possible typo found: 'progess' should be 'progress'

- **Suggestion:** `progress`

---

#### 271. Typo: 'databse'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\tutorial_app.po:40`

**Description:** Possible typo found: 'databse' should be 'database'

- **Suggestion:** `database`

---

#### 272. Typo: 'adress'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\zh_CN\LC_MESSAGES\_pot\tutorial_app.po:751`

**Description:** Possible typo found: 'adress' should be 'address'

- **Suggestion:** `address`

---

#### 273. Typo: 'childs'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\api.pot:513`

**Description:** Possible typo found: 'childs' should be 'children, child's'

- **Suggestion:** `children, child's`

---

#### 274. Typo: 'accpets'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\changelog.pot:372`

**Description:** Possible typo found: 'accpets' should be 'accepts'

- **Suggestion:** `accepts`

---

#### 275. Typo: 'Whats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\changelog.pot:392`

**Description:** Possible typo found: 'Whats' should be 'What's'

- **Suggestion:** `What's`

---

#### 276. Typo: 'modue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\configuration.pot:160`

**Description:** Possible typo found: 'modue' should be 'module'

- **Suggestion:** `module`

---

#### 277. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\contact.pot:48`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 278. Typo: 'oder'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\contact.pot:48`

**Description:** Possible typo found: 'oder' should be 'order, older, coder, odder, odor, over, doer'

- **Suggestion:** `order, older, coder, odder, odor, over, doer`

---

#### 279. Typo: 'ist'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\contact.pot:48`

**Description:** Possible typo found: 'ist' should be 'is, it, its, it's, sit, list'

- **Suggestion:** `is, it, its, it's, sit, list`

---

#### 280. Typo: 'Thats'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\development.pot:156`

**Description:** Possible typo found: 'Thats' should be 'That's'

- **Suggestion:** `That's`

---

#### 281. Typo: 'applyed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\development.pot:188`

**Description:** Possible typo found: 'applyed' should be 'applied'

- **Suggestion:** `applied`

---

#### 282. Typo: 'informations'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\plugindev.pot:132`

**Description:** Possible typo found: 'informations' should be 'information'

- **Suggestion:** `information`

---

#### 283. Typo: 'infastructure'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\recipes.pot:217`

**Description:** Possible typo found: 'infastructure' should be 'infrastructure'

- **Suggestion:** `infrastructure`

---

#### 284. Typo: 're-usable'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\docs\_locale\_pot\tutorial.pot:701`

**Description:** Possible typo found: 're-usable' should be 'reusable'

- **Suggestion:** `reusable`

---

#### 285. Typo: 'doen't'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_config.py:10`

**Description:** Possible typo found: 'doen't' should be 'doesn't'

- **Suggestion:** `doesn't`

---

#### 286. Typo: 'overlayed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_config.py:118`

**Description:** Possible typo found: 'overlayed' should be 'overlaid'

- **Suggestion:** `overlaid`

---

#### 287. Typo: 'overlayed'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_config.py:152`

**Description:** Possible typo found: 'overlayed' should be 'overlaid'

- **Suggestion:** `overlaid`

---

#### 288. Typo: 'multible'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_environ.py:321`

**Description:** Possible typo found: 'multible' should be 'multiple'

- **Suggestion:** `multiple`

---

#### 289. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_environ.py:866`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 290. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_environ.py:867`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 291. Typo: 'returs'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_formsdict.py:9`

**Description:** Possible typo found: 'returs' should be 'returns'

- **Suggestion:** `returns`

---

#### 292. Typo: 'returs'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_formsdict.py:15`

**Description:** Possible typo found: 'returs' should be 'returns'

- **Suggestion:** `returns`

---

#### 293. Typo: 'clen'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_multipart.py:21`

**Description:** Possible typo found: 'clen' should be 'clean, clan'

- **Suggestion:** `clean, clan`

---

#### 294. Typo: 'clen'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_multipart.py:26`

**Description:** Possible typo found: 'clen' should be 'clean, clan'

- **Suggestion:** `clean, clan`

---

#### 295. Typo: 'Te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_multipart.py:59`

**Description:** Possible typo found: 'Te' should be 'The, Be, We, To'

- **Suggestion:** `The, Be, We, To`

---

#### 296. Typo: 'Te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_multipart.py:60`

**Description:** Possible typo found: 'Te' should be 'The, Be, We, To'

- **Suggestion:** `The, Be, We, To`

---

#### 297. Typo: 'withoud'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_multipart.py:130`

**Description:** Possible typo found: 'withoud' should be 'without'

- **Suggestion:** `without`

---

#### 298. Typo: 'clen'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_multipart.py:703`

**Description:** Possible typo found: 'clen' should be 'clean, clan'

- **Suggestion:** `clean, clan`

---

#### 299. Typo: 'indention'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_stpl.py:106`

**Description:** Possible typo found: 'indention' should be 'indentation'

- **Suggestion:** `indentation`

---

#### 300. Typo: 'indention'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_bottlepy__bottle_9s_57lb7\bottle\test\test_stpl.py:117`

**Description:** Possible typo found: 'indention' should be 'indentation'

- **Suggestion:** `indentation`

---

## Notes

- All secrets are **redacted** in this report for safety.
- Remediation instructions are AI-generated and should be reviewed by a human.
- This report is generated for educational purposes (MIT AI+X PBL).

*Report generated on 2026-01-07 07:04:03 UTC*