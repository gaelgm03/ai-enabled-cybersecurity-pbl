# Security Scan Report

**Scan ID:** `scan-20260107-070238-64f647d8`  
**Timestamp:** 2026-01-07T07:02:38.812846Z  
**Target:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click`

---

## Summary

**Total Findings:** 48

### By Severity

| Severity | Count |
|----------|-------|
| 🟠 High | 1 |
| 🟢 Low | 47 |

### By Type

| Type | Count |
|------|-------|
| 📝 Typo | 47 |
| 🔐 Secret | 1 |

---

## Findings

### 🔐 Secret Issues

#### 1. Potential Password/Secret

- **Severity:** 🟠 High
- **Detector:** `regex-patterns`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_utils.py:230`
- **Match (redacted):** `\nin*******ed\n`

**Description:** Detected potential secret matching Password/Secret pattern

---

### 📝 Typo Issues

#### 1. Typo: 're-used'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\CHANGES.rst:891`

**Description:** Possible typo found: 're-used' should be 'reused'

- **Suggestion:** `reused`

---

#### 2. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\docs\handling-files.md:29`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 3. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\docs\handling-files.md:42`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 4. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\docs\handling-files.md:44`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 5. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\docs\quickstart.md:21`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 6. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\docs\quickstart.md:21`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 7. Typo: 'bulitin'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\examples\aliases\aliases.py:43`

**Description:** Possible typo found: 'bulitin' should be 'built-in'

- **Suggestion:** `built-in`

---

#### 8. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\examples\inout\README:3`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 9. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\examples\inout\README:10`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 10. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\examples\inout\inout.py:14`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 11. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\examples\inout\inout.py:18`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 12. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\examples\inout\inout.py:22`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 13. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\examples\inout\pyproject.toml:4`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 14. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\examples\inout\pyproject.toml:11`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 15. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\examples\inout\pyproject.toml:11`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 16. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\examples\inout\pyproject.toml:18`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 17. Typo: 'odering'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\core.py:1069`

**Description:** Possible typo found: 'odering' should be 'ordering'

- **Suggestion:** `ordering`

---

#### 18. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\decorators.py:18`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 19. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\decorators.py:20`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 20. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\decorators.py:28`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 21. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\decorators.py:39`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 22. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\decorators.py:53`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 23. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\decorators.py:76`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 24. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\decorators.py:102`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 25. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\decorators.py:115`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 26. Typo: 'larg'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\parser.py:424`

**Description:** Possible typo found: 'larg' should be 'large'

- **Suggestion:** `large`

---

#### 27. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\types.py:21`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 28. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\types.py:875`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 29. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\utils.py:25`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 30. Typo: 'te'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\src\click\utils.py:27`

**Description:** Possible typo found: 'te' should be 'the, be, we, to'

- **Suggestion:** `the, be, we, to`

---

#### 31. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_arguments.py:109`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 32. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_arguments.py:117`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 33. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_arguments.py:123`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 34. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_arguments.py:142`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 35. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_arguments.py:152`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 36. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_arguments.py:162`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 37. Typo: 'inout'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_arguments.py:166`

**Description:** Possible typo found: 'inout' should be 'input, in out'

- **Suggestion:** `input, in out`

---

#### 38. Typo: 'ue'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_options.py:512`

**Description:** Possible typo found: 'ue' should be 'use, due'

- **Suggestion:** `use, due`

---

#### 39. Typo: 'wont'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_options.py:991`

**Description:** Possible typo found: 'wont' should be 'won't'

- **Suggestion:** `won't`

---

#### 40. Typo: 'wont'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_options.py:997`

**Description:** Possible typo found: 'wont' should be 'won't'

- **Suggestion:** `won't`

---

#### 41. Typo: 'wont'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_options.py:1007`

**Description:** Possible typo found: 'wont' should be 'won't'

- **Suggestion:** `won't`

---

#### 42. Typo: 'wont'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_options.py:1013`

**Description:** Possible typo found: 'wont' should be 'won't'

- **Suggestion:** `won't`

---

#### 43. Typo: 're-use'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_options.py:1060`

**Description:** Possible typo found: 're-use' should be 'reuse'

- **Suggestion:** `reuse`

---

#### 44. Typo: 'wont'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_options.py:1061`

**Description:** Possible typo found: 'wont' should be 'won't'

- **Suggestion:** `won't`

---

#### 45. Typo: 'wont'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_options.py:1077`

**Description:** Possible typo found: 'wont' should be 'won't'

- **Suggestion:** `won't`

---

#### 46. Typo: 'ot'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_termui.py:395`

**Description:** Possible typo found: 'ot' should be 'to, of, or, not, it'

- **Suggestion:** `to, of, or, not, it`

---

#### 47. Typo: 'spacial'

- **Severity:** 🟢 Low
- **Detector:** `codespell`
- **Location:** `C:\Users\gguzm\AppData\Local\Temp\scan_pallets__click_113dv_xy\click\tests\test_types.py:231`

**Description:** Possible typo found: 'spacial' should be 'special, spatial'

- **Suggestion:** `special, spatial`

---

## Notes

- All secrets are **redacted** in this report for safety.
- Remediation instructions are AI-generated and should be reviewed by a human.
- This report is generated for educational purposes (MIT AI+X PBL).

*Report generated on 2026-01-07 07:02:44 UTC*