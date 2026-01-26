# Security Analysis Report

**Target:** `encode/django-rest-framework`  
**Scan Date:** 2026-01-07 07:03:46 UTC  
**Scan ID:** `scan-20260107-070321-62ebe95c`
**Commit:** `3f190b7ddc1a`
**Primary Language:** Python
**GitHub Stars:** 29,794

---

## Executive Summary

**Overall Risk Level:** 🟠 **HIGH** - Significant issues found

This security scan analyzed `encode/django-rest-framework` and identified **493 potential security issues**.

### Findings by Severity

| Severity | Count | Action Required |
|----------|-------|-----------------|
| 🟠 High | 41 | Soon |
| 🟢 Low | 452 | When convenient |

### Findings by Category

- 📝 **Typos & Code Quality**: 452 issue(s)
- 🔐 **Exposed Secrets & Credentials**: 41 issue(s)

---

## Severity Rating Guide

| Level | Meaning | Response Time |
|-------|---------|---------------|
| 🔴 Critical | Exploitable vulnerability with severe impact | Immediate (hours) |
| 🟠 High | Serious issue requiring prompt attention | Days |
| 🟡 Medium | Moderate risk, should be planned | Weeks |
| 🟢 Low | Minor issue, low risk | When convenient |

---

## Findings Overview

| # | Severity | Category | Title | Location |
|---|----------|----------|-------|----------|
| 1 | 🟢 | Typo | Typo: 'fo' | `codespell-ignore-words.txt:8` |
| 2 | 🟢 | Typo | Typo: 'malcom' | `codespell-ignore-words.txt:9` |
| 3 | 🟢 | Typo | Typo: 'ser' | `codespell-ignore-words.txt:10` |
| 4 | 🟢 | Typo | Typo: 'Malcom' | `docs\api-guide\parsers.md:12` |
| 5 | 🟢 | Typo | Typo: 'Malcom' | `docs\api-guide\requests.md:10` |
| 6 | 🟢 | Typo | Typo: 'koordinates' | `docs\community\kickstarter-announcement.md:83` |
| 7 | 🟢 | Typo | Typo: 'Koordinates' | `docs\community\kickstarter-announcement.md:83` |
| 8 | 🟢 | Typo | Typo: 'ser' | `docs\topics\internationalization.md:46` |
| 9 | 🟢 | Typo | Typo: 'bu' | `docs_theme\js\jquery-1.8.1-min.js:2` |
| 10 | 🟢 | Typo | Typo: 'bu' | `docs_theme\js\jquery-1.8.1-min.js:2` |
| 11 | 🟢 | Typo | Typo: 'bu' | `docs_theme\js\jquery-1.8.1-min.js:2` |
| 12 | 🟢 | Typo | Typo: 'bu' | `docs_theme\js\jquery-1.8.1-min.js:2` |
| 13 | 🟢 | Typo | Typo: 'bU' | `docs_theme\js\jquery-1.8.1-min.js:2` |
| 14 | 🟢 | Typo | Typo: 'bU' | `docs_theme\js\jquery-1.8.1-min.js:2` |
| 15 | 🟢 | Typo | Typo: 'bU' | `docs_theme\js\jquery-1.8.1-min.js:2` |
| 16 | 🟢 | Typo | Typo: 'isnt' | `docs_theme\js\prettify-1.0.js:24` |
| 17 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:120` |
| 18 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:157` |
| 19 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:161` |
| 20 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:173` |
| 21 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:178` |
| 22 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:183` |
| 23 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:191` |
| 24 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:224` |
| 25 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:229` |
| 26 | 🟢 | Typo | Typo: 'bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:260` |
| 27 | 🟢 | Typo | Typo: 'bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:278` |
| 28 | 🟢 | Typo | Typo: 'bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:287` |
| 29 | 🟢 | Typo | Typo: 'bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:292` |
| 30 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:311` |
| 31 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:349` |
| 32 | 🟢 | Typo | Typo: 'obyekt' | `rest_framework\locale\az\LC_MESSAGES\django.po:425` |
| 33 | 🟢 | Typo | Typo: 'Obyekt' | `rest_framework\locale\az\LC_MESSAGES\django.po:442` |
| 34 | 🟢 | Typo | Typo: 'obyekt' | `rest_framework\locale\az\LC_MESSAGES\django.po:452` |
| 35 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:528` |
| 36 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:543` |
| 37 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:548` |
| 38 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\az\LC_MESSAGES\django.po:553` |
| 39 | 🟢 | Typo | Typo: 'indicat' | `rest_framework\locale\ca\LC_MESSAGES\django.po:42` |
| 40 | 🟢 | Typo | Typo: 'definit' | `rest_framework\locale\ca\LC_MESSAGES\django.po:141` |
| 41 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\ca\LC_MESSAGES\django.po:160` |
| 42 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\ca\LC_MESSAGES\django.po:223` |
| 43 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\ca\LC_MESSAGES\django.po:228` |
| 44 | 🟢 | Typo | Typo: 'buit' | `rest_framework\locale\ca\LC_MESSAGES\django.po:332` |
| 45 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\ca\LC_MESSAGES\django.po:527` |
| 46 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\ca\LC_MESSAGES\django.po:542` |
| 47 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\ca\LC_MESSAGES\django.po:547` |
| 48 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\ca\LC_MESSAGES\django.po:552` |
| 49 | 🟢 | Typo | Typo: 'objekt' | `rest_framework\locale\cs\LC_MESSAGES\django.po:426` |
| 50 | 🟢 | Typo | Typo: 'objekt' | `rest_framework\locale\cs\LC_MESSAGES\django.po:443` |
| 51 | 🟢 | Typo | Typo: 'Objekt' | `rest_framework\locale\cs\LC_MESSAGES\django.po:453` |
| 52 | 🟢 | Typo | Typo: 'adresse' | `rest_framework\locale\da\LC_MESSAGES\django.po:216` |
| 53 | 🟢 | Typo | Typo: 'formater' | `rest_framework\locale\da\LC_MESSAGES\django.po:261` |
| 54 | 🟢 | Typo | Typo: 'formater' | `rest_framework\locale\da\LC_MESSAGES\django.po:279` |
| 55 | 🟢 | Typo | Typo: 'formater' | `rest_framework\locale\da\LC_MESSAGES\django.po:288` |
| 56 | 🟢 | Typo | Typo: 'formater' | `rest_framework\locale\da\LC_MESSAGES\django.po:293` |
| 57 | 🟢 | Typo | Typo: 'adresse' | `rest_framework\locale\da\LC_MESSAGES\django.po:317` |
| 58 | 🟢 | Typo | Typo: 'oder' | `rest_framework\locale\de\LC_MESSAGES\django.po:47` |
| 59 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:108` |
| 60 | 🟢 | Typo | Typo: 'Sie' | `rest_framework\locale\de\LC_MESSAGES\django.po:128` |
| 61 | 🟢 | Typo | Typo: 'Aktion' | `rest_framework\locale\de\LC_MESSAGES\django.po:128` |
| 62 | 🟢 | Typo | Typo: 'Methode' | `rest_framework\locale\de\LC_MESSAGES\django.po:137` |
| 63 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:165` |
| 64 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:165` |
| 65 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:169` |
| 66 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:181` |
| 67 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:186` |
| 68 | 🟢 | Typo | Typo: 'als' | `rest_framework\locale\de\LC_MESSAGES\django.po:186` |
| 69 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:186` |
| 70 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:191` |
| 71 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:191` |
| 72 | 🟢 | Typo | Typo: 'Adresse' | `rest_framework\locale\de\LC_MESSAGES\django.po:195` |
| 73 | 🟢 | Typo | Typo: 'passt' | `rest_framework\locale\de\LC_MESSAGES\django.po:199` |
| 74 | 🟢 | Typo | Typo: 'Sie' | `rest_framework\locale\de\LC_MESSAGES\django.po:223` |
| 75 | 🟢 | Typo | Typo: 'oder' | `rest_framework\locale\de\LC_MESSAGES\django.po:223` |
| 76 | 🟢 | Typo | Typo: 'Adresse' | `rest_framework\locale\de\LC_MESSAGES\django.po:223` |
| 77 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:227` |
| 78 | 🟢 | Typo | Typo: 'oder' | `rest_framework\locale\de\LC_MESSAGES\django.po:232` |
| 79 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:232` |
| 80 | 🟢 | Typo | Typo: 'oder' | `rest_framework\locale\de\LC_MESSAGES\django.po:237` |
| 81 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:237` |
| 82 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:245` |
| 83 | 🟢 | Typo | Typo: 'als' | `rest_framework\locale\de\LC_MESSAGES\django.po:250` |
| 84 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:250` |
| 85 | 🟢 | Typo | Typo: 'als' | `rest_framework\locale\de\LC_MESSAGES\django.po:256` |
| 86 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:256` |
| 87 | 🟢 | Typo | Typo: 'als' | `rest_framework\locale\de\LC_MESSAGES\django.po:263` |
| 88 | 🟢 | Typo | Typo: 'vor' | `rest_framework\locale\de\LC_MESSAGES\django.po:263` |
| 89 | 🟢 | Typo | Typo: 'Komma' | `rest_framework\locale\de\LC_MESSAGES\django.po:263` |
| 90 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:263` |
| 91 | 🟢 | Typo | Typo: 'Formate' | `rest_framework\locale\de\LC_MESSAGES\django.po:268` |
| 92 | 🟢 | Typo | Typo: 'Formate' | `rest_framework\locale\de\LC_MESSAGES\django.po:286` |
| 93 | 🟢 | Typo | Typo: 'Formate' | `rest_framework\locale\de\LC_MESSAGES\django.po:295` |
| 94 | 🟢 | Typo | Typo: 'Formate' | `rest_framework\locale\de\LC_MESSAGES\django.po:300` |
| 95 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:305` |
| 96 | 🟢 | Typo | Typo: 'als' | `rest_framework\locale\de\LC_MESSAGES\django.po:310` |
| 97 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:324` |
| 98 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:341` |
| 99 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:347` |
| 100 | 🟢 | Typo | Typo: 'ist' | `rest_framework\locale\de\LC_MESSAGES\django.po:353` |
| 101 | 🟢 | Typo | Typo: 'oder' | `rest_framework\locale\de\LC_MESSAGES\django.po:353` |
| 102 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:362` |
| 103 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:367` |
| 104 | 🟢 | Typo | Typo: 'als' | `rest_framework\locale\de\LC_MESSAGES\django.po:367` |
| 105 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:396` |
| 106 | 🟢 | Typo | Typo: 'Objekt' | `rest_framework\locale\de\LC_MESSAGES\django.po:450` |
| 107 | 🟢 | Typo | Typo: 'Objekt' | `rest_framework\locale\de\LC_MESSAGES\django.po:460` |
| 108 | 🟢 | Typo | Typo: 'Elemente' | `rest_framework\locale\de\LC_MESSAGES\django.po:532` |
| 109 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:536` |
| 110 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:551` |
| 111 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:556` |
| 112 | 🟢 | Typo | Typo: 'Feld' | `rest_framework\locale\de\LC_MESSAGES\django.po:561` |
| 113 | 🟢 | Typo | Typo: 'contener' | `rest_framework\locale\es\LC_MESSAGES\django.po:34` |
| 114 | 🟢 | Typo | Typo: 'contener' | `rest_framework\locale\es\LC_MESSAGES\django.po:54` |
| 115 | 🟢 | Typo | Typo: 'contener' | `rest_framework\locale\es\LC_MESSAGES\django.po:59` |
| 116 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\es\LC_MESSAGES\django.po:59` |
| 117 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\es\LC_MESSAGES\django.po:168` |
| 118 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\es\LC_MESSAGES\django.po:172` |
| 119 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\es\LC_MESSAGES\django.po:185` |
| 120 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\es\LC_MESSAGES\django.po:190` |
| 121 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\es\LC_MESSAGES\django.po:217` |
| 122 | 🟢 | Typo | Typo: 'requiere' | `rest_framework\locale\es\LC_MESSAGES\django.po:243` |
| 123 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\es\LC_MESSAGES\django.po:345` |
| 124 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\es\LC_MESSAGES\django.po:378` |
| 125 | 🟢 | Typo | Typo: 'inicial' | `rest_framework\locale\es\LC_MESSAGES\django.po:418` |
| 126 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\es\LC_MESSAGES\django.po:534` |
| 127 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\es\LC_MESSAGES\django.po:549` |
| 128 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\es\LC_MESSAGES\django.po:554` |
| 129 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\es\LC_MESSAGES\django.po:559` |
| 130 | 🟢 | Typo | Typo: 'mis' | `rest_framework\locale\et\LC_MESSAGES\django.po:198` |
| 131 | 🟢 | Typo | Typo: 'versioon' | `rest_framework\locale\et\LC_MESSAGES\django.po:558` |
| 132 | 🟢 | Typo | Typo: 'versioon' | `rest_framework\locale\et\LC_MESSAGES\django.po:562` |
| 133 | 🟢 | Typo | Typo: 'versioon' | `rest_framework\locale\et\LC_MESSAGES\django.po:566` |
| 134 | 🟢 | Typo | Typo: 'versioon' | `rest_framework\locale\et\LC_MESSAGES\django.po:570` |
| 135 | 🟢 | Typo | Typo: 'versioon' | `rest_framework\locale\et\LC_MESSAGES\django.po:574` |
| 136 | 🟢 | Typo | Typo: 'versio' | `rest_framework\locale\fi\LC_MESSAGES\django.po:559` |
| 137 | 🟢 | Typo | Typo: 'versio' | `rest_framework\locale\fi\LC_MESSAGES\django.po:563` |
| 138 | 🟢 | Typo | Typo: 'versio' | `rest_framework\locale\fi\LC_MESSAGES\django.po:567` |
| 139 | 🟢 | Typo | Typo: 'versio' | `rest_framework\locale\fi\LC_MESSAGES\django.po:571` |
| 140 | 🟢 | Typo | Typo: 'versio' | `rest_framework\locale\fi\LC_MESSAGES\django.po:575` |
| 141 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:28` |
| 142 | 🟢 | Typo | Typo: 'Informations' | `rest_framework\locale\fr\LC_MESSAGES\django.po:28` |
| 143 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:32` |
| 144 | 🟢 | Typo | Typo: 'informations' | `rest_framework\locale\fr\LC_MESSAGES\django.po:32` |
| 145 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:36` |
| 146 | 🟢 | Typo | Typo: 'informations' | `rest_framework\locale\fr\LC_MESSAGES\django.po:36` |
| 147 | 🟢 | Typo | Typo: 'mot' | `rest_framework\locale\fr\LC_MESSAGES\django.po:40` |
| 148 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:40` |
| 149 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:48` |
| 150 | 🟢 | Typo | Typo: 'Informations' | `rest_framework\locale\fr\LC_MESSAGES\django.po:48` |
| 151 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:52` |
| 152 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:56` |
| 153 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:60` |
| 154 | 🟢 | Typo | Typo: 'Mot' | `rest_framework\locale\fr\LC_MESSAGES\django.po:92` |
| 155 | 🟢 | Typo | Typo: 'informations' | `rest_framework\locale\fr\LC_MESSAGES\django.po:96` |
| 156 | 🟢 | Typo | Typo: 'invalide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:108` |
| 157 | 🟢 | Typo | Typo: 'Informations' | `rest_framework\locale\fr\LC_MESSAGES\django.po:116` |
| 158 | 🟢 | Typo | Typo: 'Informations' | `rest_framework\locale\fr\LC_MESSAGES\django.po:120` |
| 159 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:169` |
| 160 | 🟢 | Typo | Typo: 'invalide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:173` |
| 161 | 🟢 | Typo | Typo: 'adresse' | `rest_framework\locale\fr\LC_MESSAGES\django.po:191` |
| 162 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:191` |
| 163 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:207` |
| 164 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:211` |
| 165 | 🟢 | Typo | Typo: 'adresse' | `rest_framework\locale\fr\LC_MESSAGES\django.po:215` |
| 166 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:215` |
| 167 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:219` |
| 168 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:237` |
| 169 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:294` |
| 170 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:313` |
| 171 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:338` |
| 172 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:365` |
| 173 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:401` |
| 174 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:413` |
| 175 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:418` |
| 176 | 🟢 | Typo | Typo: 'Lien' | `rest_framework\locale\fr\LC_MESSAGES\django.po:427` |
| 177 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:427` |
| 178 | 🟢 | Typo | Typo: 'Lien' | `rest_framework\locale\fr\LC_MESSAGES\django.po:431` |
| 179 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:431` |
| 180 | 🟢 | Typo | Typo: 'Lien' | `rest_framework\locale\fr\LC_MESSAGES\django.po:435` |
| 181 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:435` |
| 182 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:449` |
| 183 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:471` |
| 184 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:550` |
| 185 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:554` |
| 186 | 🟢 | Typo | Typo: 'invalide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:558` |
| 187 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:562` |
| 188 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\fr\LC_MESSAGES\django.po:566` |
| 189 | 🟢 | Typo | Typo: 'elemet' | `rest_framework\locale\hu\LC_MESSAGES\django.po:311` |
| 190 | 🟢 | Typo | Typo: 'Nome' | `rest_framework\locale\it\LC_MESSAGES\django.po:40` |
| 191 | 🟢 | Typo | Typo: 'Impossibile' | `rest_framework\locale\it\LC_MESSAGES\django.po:97` |
| 192 | 🟢 | Typo | Typo: 'nome' | `rest_framework\locale\it\LC_MESSAGES\django.po:101` |
| 193 | 🟢 | Typo | Typo: 'Impossibile' | `rest_framework\locale\it\LC_MESSAGES\django.po:138` |
| 194 | 🟢 | Typo | Typo: 'nome' | `rest_framework\locale\it\LC_MESSAGES\django.po:334` |
| 195 | 🟢 | Typo | Typo: 'nome' | `rest_framework\locale\it\LC_MESSAGES\django.po:344` |
| 196 | 🟢 | Typo | Typo: 'nome' | `rest_framework\locale\it\LC_MESSAGES\django.po:574` |
| 197 | 🟢 | Typo | Typo: 'vai' | `rest_framework\locale\lv\LC_MESSAGES\django.po:39` |
| 198 | 🟢 | Typo | Typo: 'vai' | `rest_framework\locale\lv\LC_MESSAGES\django.po:197` |
| 199 | 🟢 | Typo | Typo: 'vai' | `rest_framework\locale\lv\LC_MESSAGES\django.po:215` |
| 200 | 🟢 | Typo | Typo: 'vai' | `rest_framework\locale\lv\LC_MESSAGES\django.po:224` |
| 201 | 🟢 | Typo | Typo: 'vai' | `rest_framework\locale\lv\LC_MESSAGES\django.po:229` |
| 202 | 🟢 | Typo | Typo: 'vai' | `rest_framework\locale\lv\LC_MESSAGES\django.po:345` |
| 203 | 🟢 | Typo | Typo: 'teksts' | `rest_framework\locale\lv\LC_MESSAGES\django.po:447` |
| 204 | 🟢 | Typo | Typo: 'passord' | `rest_framework\locale\nb\LC_MESSAGES\django.po:37` |
| 205 | 🟢 | Typo | Typo: 'Passord' | `rest_framework\locale\nb\LC_MESSAGES\django.po:90` |
| 206 | 🟢 | Typo | Typo: 'som' | `rest_framework\locale\nb\LC_MESSAGES\django.po:199` |
| 207 | 🟢 | Typo | Typo: 'lik' | `rest_framework\locale\nb\LC_MESSAGES\django.po:226` |
| 208 | 🟢 | Typo | Typo: 'lik' | `rest_framework\locale\nb\LC_MESSAGES\django.po:231` |
| 209 | 🟢 | Typo | Typo: 'komma' | `rest_framework\locale\nb\LC_MESSAGES\django.po:257` |
| 210 | 🟢 | Typo | Typo: 'Objekt' | `rest_framework\locale\nb\LC_MESSAGES\django.po:454` |
| 211 | 🟢 | Typo | Typo: 'noen' | `rest_framework\locale\nb\LC_MESSAGES\django.po:567` |
| 212 | 🟢 | Typo | Typo: 'te' | `rest_framework\locale\nl\LC_MESSAGES\django.po:125` |
| 213 | 🟢 | Typo | Typo: 'Methode' | `rest_framework\locale\nl\LC_MESSAGES\django.po:134` |
| 214 | 🟢 | Typo | Typo: 'leeg' | `rest_framework\locale\nl\LC_MESSAGES\django.po:166` |
| 215 | 🟢 | Typo | Typo: 'leeg' | `rest_framework\locale\nl\LC_MESSAGES\django.po:178` |
| 216 | 🟢 | Typo | Typo: 'te' | `rest_framework\locale\nl\LC_MESSAGES\django.po:238` |
| 217 | 🟢 | Typo | Typo: 'komma' | `rest_framework\locale\nl\LC_MESSAGES\django.po:253` |
| 218 | 🟢 | Typo | Typo: 'komma' | `rest_framework\locale\nl\LC_MESSAGES\django.po:260` |
| 219 | 🟢 | Typo | Typo: 'leeg' | `rest_framework\locale\nl\LC_MESSAGES\django.po:316` |
| 220 | 🟢 | Typo | Typo: 'leeg' | `rest_framework\locale\nl\LC_MESSAGES\django.po:338` |
| 221 | 🟢 | Typo | Typo: 'leeg' | `rest_framework\locale\nl\LC_MESSAGES\django.po:354` |
| 222 | 🟢 | Typo | Typo: 'valide' | `rest_framework\locale\nl\LC_MESSAGES\django.po:377` |
| 223 | 🟢 | Typo | Typo: 'adres' | `rest_framework\locale\pl\LC_MESSAGES\django.po:190` |
| 224 | 🟢 | Typo | Typo: 'adres' | `rest_framework\locale\pl\LC_MESSAGES\django.po:210` |
| 225 | 🟢 | Typo | Typo: 'adres' | `rest_framework\locale\pl\LC_MESSAGES\django.po:218` |
| 226 | 🟢 | Typo | Typo: 'daty' | `rest_framework\locale\pl\LC_MESSAGES\django.po:263` |
| 227 | 🟢 | Typo | Typo: 'daty' | `rest_framework\locale\pl\LC_MESSAGES\django.po:285` |
| 228 | 🟢 | Typo | Typo: 'daty' | `rest_framework\locale\pl\LC_MESSAGES\django.po:546` |
| 229 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\pt\LC_MESSAGES\django.po:56` |
| 230 | 🟢 | Typo | Typo: 'Nome' | `rest_framework\locale\pt\LC_MESSAGES\django.po:88` |
| 231 | 🟢 | Typo | Typo: 'erro' | `rest_framework\locale\pt\LC_MESSAGES\django.po:104` |
| 232 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt\LC_MESSAGES\django.po:165` |
| 233 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt\LC_MESSAGES\django.po:177` |
| 234 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\pt\LC_MESSAGES\django.po:182` |
| 235 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\pt\LC_MESSAGES\django.po:187` |
| 236 | 🟢 | Typo | Typo: 'itens' | `rest_framework\locale\pt\LC_MESSAGES\django.po:306` |
| 237 | 🟢 | Typo | Typo: 'itens' | `rest_framework\locale\pt\LC_MESSAGES\django.po:311` |
| 238 | 🟢 | Typo | Typo: 'Nome' | `rest_framework\locale\pt\LC_MESSAGES\django.po:333` |
| 239 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt\LC_MESSAGES\django.po:333` |
| 240 | 🟢 | Typo | Typo: 'nome' | `rest_framework\locale\pt\LC_MESSAGES\django.po:343` |
| 241 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\pt\LC_MESSAGES\django.po:343` |
| 242 | 🟢 | Typo | Typo: 'itens' | `rest_framework\locale\pt\LC_MESSAGES\django.po:368` |
| 243 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt\LC_MESSAGES\django.po:376` |
| 244 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt\LC_MESSAGES\django.po:532` |
| 245 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt\LC_MESSAGES\django.po:547` |
| 246 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt\LC_MESSAGES\django.po:552` |
| 247 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt\LC_MESSAGES\django.po:557` |
| 248 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:60` |
| 249 | 🟢 | Typo | Typo: 'Nome' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:92` |
| 250 | 🟢 | Typo | Typo: 'erro' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:108` |
| 251 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:169` |
| 252 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:173` |
| 253 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:186` |
| 254 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:191` |
| 255 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:219` |
| 256 | 🟢 | Typo | Typo: 'itens' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:310` |
| 257 | 🟢 | Typo | Typo: 'itens' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:315` |
| 258 | 🟢 | Typo | Typo: 'Nome' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:337` |
| 259 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:337` |
| 260 | 🟢 | Typo | Typo: 'nome' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:347` |
| 261 | 🟢 | Typo | Typo: 'caracteres' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:347` |
| 262 | 🟢 | Typo | Typo: 'itens' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:372` |
| 263 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:380` |
| 264 | 🟢 | Typo | Typo: 'termo' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:388` |
| 265 | 🟢 | Typo | Typo: 'inicial' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:420` |
| 266 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:536` |
| 267 | 🟢 | Typo | Typo: 'Caracteres' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:546` |
| 268 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:551` |
| 269 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:556` |
| 270 | 🟢 | Typo | Typo: 'ser' | `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:561` |
| 271 | 🟢 | Typo | Typo: 'caractere' | `rest_framework\locale\ro\LC_MESSAGES\django.po:28` |
| 272 | 🟢 | Typo | Typo: 'corect' | `rest_framework\locale\ro\LC_MESSAGES\django.po:32` |
| 273 | 🟢 | Typo | Typo: 'caractere' | `rest_framework\locale\ro\LC_MESSAGES\django.po:48` |
| 274 | 🟢 | Typo | Typo: 'caractere' | `rest_framework\locale\ro\LC_MESSAGES\django.po:53` |
| 275 | 🟢 | Typo | Typo: 'caractere' | `rest_framework\locale\ro\LC_MESSAGES\django.po:53` |
| 276 | 🟢 | Typo | Typo: 'caractere' | `rest_framework\locale\ro\LC_MESSAGES\django.po:179` |
| 277 | 🟢 | Typo | Typo: 'caractere' | `rest_framework\locale\ro\LC_MESSAGES\django.po:184` |
| 278 | 🟢 | Typo | Typo: 'caractere' | `rest_framework\locale\ro\LC_MESSAGES\django.po:198` |
| 279 | 🟢 | Typo | Typo: 'caractere' | `rest_framework\locale\ro\LC_MESSAGES\django.po:234` |
| 280 | 🟢 | Typo | Typo: 'formate' | `rest_framework\locale\ro\LC_MESSAGES\django.po:261` |
| 281 | 🟢 | Typo | Typo: 'formate' | `rest_framework\locale\ro\LC_MESSAGES\django.po:279` |
| 282 | 🟢 | Typo | Typo: 'formate' | `rest_framework\locale\ro\LC_MESSAGES\django.po:288` |
| 283 | 🟢 | Typo | Typo: 'formate' | `rest_framework\locale\ro\LC_MESSAGES\django.po:293` |
| 284 | 🟢 | Typo | Typo: 'elemente' | `rest_framework\locale\ro\LC_MESSAGES\django.po:308` |
| 285 | 🟢 | Typo | Typo: 'caractere' | `rest_framework\locale\ro\LC_MESSAGES\django.po:340` |
| 286 | 🟢 | Typo | Typo: 'incorect' | `rest_framework\locale\ro\LC_MESSAGES\django.po:431` |
| 287 | 🟢 | Typo | Typo: 'incorect' | `rest_framework\locale\ro\LC_MESSAGES\django.po:448` |
| 288 | 🟢 | Typo | Typo: 'elemente' | `rest_framework\locale\ro\LC_MESSAGES\django.po:525` |
| 289 | 🟢 | Typo | Typo: 'parametre' | `rest_framework\locale\sk\LC_MESSAGES\django.po:96` |
| 290 | 🟢 | Typo | Typo: 'objekt' | `rest_framework\locale\sk\LC_MESSAGES\django.po:425` |
| 291 | 🟢 | Typo | Typo: 'objekt' | `rest_framework\locale\sk\LC_MESSAGES\django.po:442` |
| 292 | 🟢 | Typo | Typo: 'Objekt' | `rest_framework\locale\sk\LC_MESSAGES\django.po:452` |
| 293 | 🟢 | Typo | Typo: 'sme' | `rest_framework\locale\sl\LC_MESSAGES\django.po:27` |
| 294 | 🟢 | Typo | Typo: 'sme' | `rest_framework\locale\sl\LC_MESSAGES\django.po:47` |
| 295 | 🟢 | Typo | Typo: 'sme' | `rest_framework\locale\sl\LC_MESSAGES\django.po:52` |
| 296 | 🟢 | Typo | Typo: 'te' | `rest_framework\locale\sl\LC_MESSAGES\django.po:120` |
| 297 | 🟢 | Typo | Typo: 'sme' | `rest_framework\locale\sl\LC_MESSAGES\django.po:161` |
| 298 | 🟢 | Typo | Typo: 'sme' | `rest_framework\locale\sl\LC_MESSAGES\django.po:173` |
| 299 | 🟢 | Typo | Typo: 'sme' | `rest_framework\locale\sl\LC_MESSAGES\django.po:178` |
| 300 | 🟢 | Typo | Typo: 'sme' | `rest_framework\locale\sl\LC_MESSAGES\django.po:311` |
| 301 | 🟢 | Typo | Typo: 'sme' | `rest_framework\locale\sl\LC_MESSAGES\django.po:349` |
| 302 | 🟢 | Typo | Typo: 'stran' | `rest_framework\locale\sl\LC_MESSAGES\django.po:408` |
| 303 | 🟢 | Typo | Typo: 'objekt' | `rest_framework\locale\sl\LC_MESSAGES\django.po:425` |
| 304 | 🟢 | Typo | Typo: 'Objekt' | `rest_framework\locale\sl\LC_MESSAGES\django.po:442` |
| 305 | 🟢 | Typo | Typo: 'Objekt' | `rest_framework\locale\sl\LC_MESSAGES\django.po:452` |
| 306 | 🟢 | Typo | Typo: 'objekt' | `rest_framework\locale\sv\LC_MESSAGES\django.po:303` |
| 307 | 🟢 | Typo | Typo: 'Objekt' | `rest_framework\locale\sv\LC_MESSAGES\django.po:453` |
| 308 | 🟢 | Typo | Typo: 'objekt' | `rest_framework\locale\sv\LC_MESSAGES\django.po:525` |
| 309 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:128` |
| 310 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:165` |
| 311 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:169` |
| 312 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:181` |
| 313 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:186` |
| 314 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:191` |
| 315 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:199` |
| 316 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:319` |
| 317 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:347` |
| 318 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:357` |
| 319 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:362` |
| 320 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:367` |
| 321 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:376` |
| 322 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:536` |
| 323 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:551` |
| 324 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:556` |
| 325 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr\LC_MESSAGES\django.po:561` |
| 326 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:121` |
| 327 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:158` |
| 328 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:162` |
| 329 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:174` |
| 330 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:179` |
| 331 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:184` |
| 332 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:192` |
| 333 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:312` |
| 334 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:340` |
| 335 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:350` |
| 336 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:529` |
| 337 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:544` |
| 338 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:549` |
| 339 | 🟢 | Typo | Typo: 'Bu' | `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:554` |
| 340 | 🟢 | Typo | Typo: 'thay' | `rest_framework\locale\vi\LC_MESSAGES\django.po:279` |
| 341 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 342 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 343 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 344 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 345 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 346 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 347 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 348 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 349 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 350 | 🟢 | Typo | Typo: 'eACG' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 351 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 352 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 353 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 354 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 355 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 356 | 🟢 | Typo | Typo: 'cACE' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 357 | 🟢 | Typo | Typo: 'actived' | `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1` |
| 358 | 🟢 | Typo | Typo: 'tE' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 359 | 🟢 | Typo | Typo: 'tE' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 360 | 🟢 | Typo | Typo: 'tE' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 361 | 🟢 | Typo | Typo: 'tE' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 362 | 🟢 | Typo | Typo: 'tE' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 363 | 🟢 | Typo | Typo: 'inout' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 364 | 🟢 | Typo | Typo: 'iif' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 365 | 🟢 | Typo | Typo: 'lenght' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 366 | 🟢 | Typo | Typo: 'filetest' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 367 | 🟢 | Typo | Typo: 'inout' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 368 | 🟢 | Typo | Typo: 'isnt' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 369 | 🟢 | Typo | Typo: 'tring' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 370 | 🟢 | Typo | Typo: 'ans' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 371 | 🟢 | Typo | Typo: 'alog' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 372 | 🟢 | Typo | Typo: 'iput' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 373 | 🟢 | Typo | Typo: 'inout' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 374 | 🟢 | Typo | Typo: 'appen' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 375 | 🟢 | Typo | Typo: 'asser' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 376 | 🟢 | Typo | Typo: 'describ' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 377 | 🟢 | Typo | Typo: 'displa' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 378 | 🟢 | Typo | Typo: 'doed' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 379 | 🟢 | Typo | Typo: 'erro' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 380 | 🟢 | Typo | Typo: 'fillin' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 381 | 🟢 | Typo | Typo: 'generat' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 382 | 🟢 | Typo | Typo: 'globa' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 383 | 🟢 | Typo | Typo: 'hel' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 384 | 🟢 | Typo | Typo: 'inpu' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 385 | 🟢 | Typo | Typo: 'mata' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 386 | 🟢 | Typo | Typo: 'mor' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 387 | 🟢 | Typo | Typo: 'retur' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 388 | 🟢 | Typo | Typo: 'rotat' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 389 | 🟢 | Typo | Typo: 'sav' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 390 | 🟢 | Typo | Typo: 'seperate' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 391 | 🟢 | Typo | Typo: 'summar' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 392 | 🟢 | Typo | Typo: 'te' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 393 | 🟢 | Typo | Typo: 'versio' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 394 | 🟢 | Typo | Typo: 'windo' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 395 | 🟢 | Typo | Typo: 'inout' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 396 | 🟢 | Typo | Typo: 'checkt' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 397 | 🟢 | Typo | Typo: 'debugg' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 398 | 🟢 | Typo | Typo: 'fo' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 399 | 🟢 | Typo | Typo: 'sav' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 400 | 🟢 | Typo | Typo: 'scrip' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 401 | 🟢 | Typo | Typo: 'scripte' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 402 | 🟢 | Typo | Typo: 'sme' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 403 | 🟢 | Typo | Typo: 'tabe' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 404 | 🟢 | Typo | Typo: 'tabl' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 405 | 🟢 | Typo | Typo: 'te' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 406 | 🟢 | Typo | Typo: 'vie' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 407 | 🟢 | Typo | Typo: 'windo' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 408 | 🟢 | Typo | Typo: 'enew' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 409 | 🟢 | Typo | Typo: 'assymetry' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 410 | 🟢 | Typo | Typo: 'iif' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 411 | 🟢 | Typo | Typo: 'isnt' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 412 | 🟢 | Typo | Typo: 'notin' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 413 | 🟢 | Typo | Typo: 'aas' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 414 | 🟢 | Typo | Typo: 'daa' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 415 | 🟢 | Typo | Typo: 'struc' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 416 | 🟢 | Typo | Typo: 'juxt' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 417 | 🟢 | Typo | Typo: 'rcall' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 418 | 🟢 | Typo | Typo: 'seh' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 419 | 🟢 | Typo | Typo: 'ser' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 420 | 🟢 | Typo | Typo: 'dispaly' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 421 | 🟢 | Typo | Typo: 'inout' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 422 | 🟢 | Typo | Typo: 'BraKet' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 423 | 🟢 | Typo | Typo: 'Ket' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1` |
| 424 | 🟢 | Typo | Typo: 'inout' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:2` |
| 425 | 🟢 | Typo | Typo: 'promt' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:2` |
| 426 | 🟢 | Typo | Typo: 'SectionIn' | `rest_framework\static\rest_framework\docs\js\highlight.pack.js:2` |
| 427 | 🟢 | Typo | Typo: 'build-in' | `rest_framework\static\rest_framework\js\coreapi-0.1.1.js:1157` |
| 428 | 🟢 | Typo | Typo: 'ue' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 429 | 🟢 | Typo | Typo: 'ue' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 430 | 🟢 | Typo | Typo: 'ue' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 431 | 🟢 | Typo | Typo: 'ue' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 432 | 🟢 | Typo | Typo: 'te' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 433 | 🟢 | Typo | Typo: 'te' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 434 | 🟢 | Typo | Typo: 'te' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 435 | 🟢 | Typo | Typo: 'te' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 436 | 🟢 | Typo | Typo: 'te' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 437 | 🟢 | Typo | Typo: 'Te' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 438 | 🟢 | Typo | Typo: 'Te' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 439 | 🟢 | Typo | Typo: 'Te' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 440 | 🟢 | Typo | Typo: 'Ue' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 441 | 🟢 | Typo | Typo: 'ot' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 442 | 🟢 | Typo | Typo: 'te' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 443 | 🟢 | Typo | Typo: 'ot' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 444 | 🟢 | Typo | Typo: 'Ue' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 445 | 🟢 | Typo | Typo: 'ot' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 446 | 🟢 | Typo | Typo: 'te' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 447 | 🟢 | Typo | Typo: 'ue' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 448 | 🟢 | Typo | Typo: 'ue' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 449 | 🟢 | Typo | Typo: 'Ot' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 450 | 🟢 | Typo | Typo: 'Ot' | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 451 | 🟢 | Typo | Typo: 'isnt' | `rest_framework\static\rest_framework\js\prettify-min.js:24` |
| 452 | 🟢 | Typo | Typo: 'fo' | `tests\test_routers.py:293` |
| 453 | 🟠 | Secret | Potential Password/Secret | `rest_framework\authentication.py:82` |
| 454 | 🟠 | Secret | Potential Password/Secret | `tests\test_fields.py:2735` |
| 455 | 🟠 | Secret | Potential Password/Secret | `tests\test_fields.py:2754` |
| 456 | 🟠 | Secret | Potential Password/Secret | `tests\test_filters.py:854` |
| 457 | 🟠 | Secret | Potential Password/Secret | `tests\test_filters.py:869` |
| 458 | 🟠 | Secret | Potential Password/Secret | `tests\test_filters.py:889` |
| 459 | 🟠 | Secret | Potential Password/Secret | `tests\test_permissions.py:550` |
| 460 | 🟠 | Secret | Potential Password/Secret | `tests\test_permissions.py:556` |
| 461 | 🟠 | Secret | Potential Password/Secret | `tests\test_request.py:204` |
| 462 | 🟠 | Secret | Potential Password/Secret | `tests\test_requests_client.py:84` |
| 463 | 🟠 | Secret | Potential Password/Secret | `tests\test_requests_client.py:85` |
| 464 | 🟠 | Secret | Potential Password/Secret | `tests\test_testing.py:167` |
| 465 | 🟠 | Secret | Potential Password/Secret | `tests\test_testing.py:177` |
| 466 | 🟠 | Secret | Potential Password/Secret | `tests\test_write_only_fields.py:10` |
| 467 | 🟠 | Secret | Potential Password/Secret | `docs\api-guide\fields.md:124` |
| 468 | 🟠 | Secret | Potential Password/Secret | `docs\topics\html-and-forms.md:113` |
| 469 | 🟠 | Secret | Potential Password/Secret | `rest_framework\authtoken\serializers.py:12` |
| 470 | 🟠 | Secret | Potential Password/Secret | `rest_framework\authtoken\serializers.py:25` |
| 471 | 🟠 | Secret | Potential Password/Secret | `rest_framework\authtoken\serializers.py:29` |
| 472 | 🟠 | Secret | Potential Password/Secret | `rest_framework\static\rest_framework\js\coreapi-0.1.1.js:15` |
| 473 | 🟠 | Secret | Potential Password/Secret | `rest_framework\static\rest_framework\js\coreapi-0.1.1.js:1191` |
| 474 | 🟠 | Secret | Potential Password/Secret | `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2` |
| 475 | 🟠 | Secret | Potential Password/Secret | `rest_framework\static\rest_framework\docs\js\api.js:206` |
| 476 | 🟠 | Secret | Potential Password/Secret | `rest_framework\static\rest_framework\docs\js\api.js:292` |
| 477 | 🟠 | Secret | Potential Password/Secret | `rest_framework\templates\rest_framework\docs\auth\basic.html:22` |
| 478 | 🟠 | Secret | Potential Password/Secret | `tests\authentication\test_authentication.py:89` |
| 479 | 🟠 | Secret | Potential Password/Secret | `tests\authentication\test_authentication.py:182` |
| 480 | 🟠 | Secret | Potential Password/Secret | `tests\authentication\test_authentication.py:208` |
| 481 | 🟠 | Secret | Potential Password/Secret | `tests\authentication\test_authentication.py:230` |
| 482 | 🟠 | Secret | Potential Password/Secret | `tests\authentication\test_authentication.py:239` |
| 483 | 🟠 | Secret | Potential Password/Secret | `tests\authentication\test_authentication.py:261` |
| 484 | 🟠 | Secret | Potential Password/Secret | `tests\authentication\test_authentication.py:274` |
| 485 | 🟠 | Secret | Potential Password/Secret | `tests\authentication\test_authentication.py:299` |
| 486 | 🟠 | Secret | Potential Password/Secret | `tests\authentication\test_authentication.py:630` |
| 487 | 🟠 | Secret | Potential Password/Secret | `tests\browsable_api\test_browsable_api.py:41` |
| 488 | 🟠 | Secret | Potential Password/Secret | `tests\browsable_api\test_browsable_api.py:52` |
| 489 | 🟠 | Secret | Potential Password/Secret | `tests\browsable_api\test_browsable_api.py:58` |
| 490 | 🟠 | Secret | Potential Password/Secret | `tests\browsable_api\test_browsable_api.py:69` |
| 491 | 🟠 | Secret | Potential Password/Secret | `tests\browsable_api\test_browsable_api.py:82` |
| 492 | 🟠 | Secret | Potential Password/Secret | `tests\browsable_api\test_browsable_api.py:93` |
| 493 | 🟠 | Secret | Potential Password/Secret | `tests\browsable_api\test_browsable_api.py:99` |

---

## Detailed Findings

### 🔐 Exposed Secrets & Credentials

*Hardcoded credentials, API keys, or other sensitive data found in source code.*

#### 1. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `rest_framework\authentication.py:82`
- **Match (redacted):** `auth********lit(`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 2. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_fields.py:2735`
- **Match (redacted):** `seri********ld()`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 3. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_fields.py:2754`
- **Match (redacted):** `seri********ld()`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 4. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_filters.py:854`
- **Match (redacted):** `mode********100)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 5. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_filters.py:869`
- **Match (redacted):** `seri********rue)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 6. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_filters.py:889`
- **Match (redacted):** `pass********ve()`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 7. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_permissions.py:550`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 8. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_permissions.py:556`
- **Match (redacted):** `self******ord)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 9. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_request.py:204`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 10. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_requests_client.py:84`
- **Match (redacted):** `requ*****ata[`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 11. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_requests_client.py:85`
- **Match (redacted):** `pass*ord)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 12. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_testing.py:167`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 13. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_testing.py:177`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 14. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\test_write_only_fields.py:10`
- **Match (redacted):** `seri********rue)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 15. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `docs\api-guide\fields.md:124`
- **Match (redacted):** `seri********eld(`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 16. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `docs\topics\html-and-forms.md:113`
- **Match (redacted):** `seri********eld(`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 17. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `rest_framework\authtoken\serializers.py:12`
- **Match (redacted):** `seri********eld(`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 18. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `rest_framework\authtoken\serializers.py:25`
- **Match (redacted):** `attr**get(`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 19. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `rest_framework\authtoken\serializers.py:29`
- **Match (redacted):** `pass*ord)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 20. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\coreapi-0.1.1.js:15`
- **Match (redacted):** `opti********ord;`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 21. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\coreapi-0.1.1.js:1191`
- **Match (redacted):** `inst******n[1]`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 22. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`
- **Match (redacted):** `!0,i********or(e`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 23. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\api.js:206`
- **Match (redacted):** `wind********word`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 24. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\api.js:292`
- **Match (redacted):** `$for***ind(`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 25. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `rest_framework\templates\rest_framework\docs\auth\basic.html:22`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 26. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\authentication\test_authentication.py:89`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 27. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\authentication\test_authentication.py:182`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 28. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\authentication\test_authentication.py:208`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 29. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\authentication\test_authentication.py:230`
- **Match (redacted):** `self******ord)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 30. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\authentication\test_authentication.py:239`
- **Match (redacted):** `self******ord)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 31. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\authentication\test_authentication.py:261`
- **Match (redacted):** `self*****word`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 32. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\authentication\test_authentication.py:274`
- **Match (redacted):** `self*****word`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 33. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\authentication\test_authentication.py:299`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 34. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\authentication\test_authentication.py:630`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 35. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\browsable_api\test_browsable_api.py:41`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 36. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\browsable_api\test_browsable_api.py:52`
- **Match (redacted):** `self******ord)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 37. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\browsable_api\test_browsable_api.py:58`
- **Match (redacted):** `self******ord)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 38. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\browsable_api\test_browsable_api.py:69`
- **Match (redacted):** `self******ord)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 39. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\browsable_api\test_browsable_api.py:82`
- **Match (redacted):** `********`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 40. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\browsable_api\test_browsable_api.py:93`
- **Match (redacted):** `self******ord)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

#### 41. Potential Password/Secret

**Severity:** 🟠 HIGH  
**Detector:** `regex-patterns`

**Evidence:**

- **File:** `tests\browsable_api\test_browsable_api.py:99`
- **Match (redacted):** `self******ord)`

**Intent:**

The code appears to store a Password/Secret for authentication or API access. This is likely used to connect to an external service.

**Attack Surface:**

- **Entry Point:** Anyone with access to the source code repository
- **Exposure:** The secret value may be in version control history
- **Reach:** If leaked, attackers can use the credential to access external services

**Risk Assessment:**

- **Impact:** Significant - Data breach or service disruption
- **Likelihood:** High - Secrets in code are easily discovered

**Recommended Fix:**

1. **Remove** the hardcoded secret from the source code
2. **Rotate** the exposed credential immediately
3. **Use** environment variables or a secrets manager
4. **Audit** version control history for the exposed value

**Verification:**

- Re-run the security scanner to confirm removal
- Verify the old credential no longer provides access
- Check git history was cleaned if necessary

---

### 📝 Typos & Code Quality

*Spelling errors that may indicate code quality issues or cause bugs.*

#### 1. Typo: 'fo'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `codespell-ignore-words.txt:8`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `of, for, to, do, go`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 2. Typo: 'malcom'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `codespell-ignore-words.txt:9`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `malcolm`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 3. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `codespell-ignore-words.txt:10`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 4. Typo: 'Malcom'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs\api-guide\parsers.md:12`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Malcolm`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 5. Typo: 'Malcom'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs\api-guide\requests.md:10`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Malcolm`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 6. Typo: 'koordinates'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs\community\kickstarter-announcement.md:83`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `coordinates`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 7. Typo: 'Koordinates'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs\community\kickstarter-announcement.md:83`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Coordinates`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 8. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs\topics\internationalization.md:46`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 9. Typo: 'bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs_theme\js\jquery-1.8.1-min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 10. Typo: 'bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs_theme\js\jquery-1.8.1-min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 11. Typo: 'bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs_theme\js\jquery-1.8.1-min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 12. Typo: 'bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs_theme\js\jquery-1.8.1-min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 13. Typo: 'bU'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs_theme\js\jquery-1.8.1-min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 14. Typo: 'bU'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs_theme\js\jquery-1.8.1-min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 15. Typo: 'bU'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs_theme\js\jquery-1.8.1-min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 16. Typo: 'isnt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `docs_theme\js\prettify-1.0.js:24`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `isn't`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 17. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:120`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 18. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:157`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 19. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:161`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 20. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:173`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 21. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:178`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 22. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:183`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 23. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:191`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 24. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:224`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 25. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:229`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 26. Typo: 'bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:260`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 27. Typo: 'bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:278`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 28. Typo: 'bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:287`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 29. Typo: 'bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:292`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `by, be, but, bug, bun, bud, buy, bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 30. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:311`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 31. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:349`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 32. Typo: 'obyekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:425`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 33. Typo: 'Obyekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:442`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 34. Typo: 'obyekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:452`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 35. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:528`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 36. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:543`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 37. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:548`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 38. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\az\LC_MESSAGES\django.po:553`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 39. Typo: 'indicat'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ca\LC_MESSAGES\django.po:42`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `indicate`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 40. Typo: 'definit'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ca\LC_MESSAGES\django.po:141`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `definite`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 41. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ca\LC_MESSAGES\django.po:160`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 42. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ca\LC_MESSAGES\django.po:223`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 43. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ca\LC_MESSAGES\django.po:228`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 44. Typo: 'buit'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ca\LC_MESSAGES\django.po:332`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `built`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 45. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ca\LC_MESSAGES\django.po:527`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 46. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ca\LC_MESSAGES\django.po:542`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 47. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ca\LC_MESSAGES\django.po:547`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 48. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ca\LC_MESSAGES\django.po:552`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 49. Typo: 'objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\cs\LC_MESSAGES\django.po:426`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 50. Typo: 'objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\cs\LC_MESSAGES\django.po:443`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 51. Typo: 'Objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\cs\LC_MESSAGES\django.po:453`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 52. Typo: 'adresse'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\da\LC_MESSAGES\django.po:216`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `address`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 53. Typo: 'formater'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\da\LC_MESSAGES\django.po:261`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `formatter`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 54. Typo: 'formater'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\da\LC_MESSAGES\django.po:279`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `formatter`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 55. Typo: 'formater'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\da\LC_MESSAGES\django.po:288`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `formatter`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 56. Typo: 'formater'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\da\LC_MESSAGES\django.po:293`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `formatter`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 57. Typo: 'adresse'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\da\LC_MESSAGES\django.po:317`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `address`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 58. Typo: 'oder'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:47`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `order, older, coder, odder, odor, over, doer`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 59. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:108`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 60. Typo: 'Sie'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:128`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Size, Sigh, Side`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 61. Typo: 'Aktion'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:128`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Action`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 62. Typo: 'Methode'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:137`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Method`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 63. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:165`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 64. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:165`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 65. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:169`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 66. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:181`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 67. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:186`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 68. Typo: 'als'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:186`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `also`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 69. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:186`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 70. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:191`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 71. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:191`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 72. Typo: 'Adresse'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:195`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Address`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 73. Typo: 'passt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:199`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `past, passed`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 74. Typo: 'Sie'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:223`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Size, Sigh, Side`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 75. Typo: 'oder'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:223`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `order, older, coder, odder, odor, over, doer`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 76. Typo: 'Adresse'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:223`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Address`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 77. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:227`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 78. Typo: 'oder'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:232`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `order, older, coder, odder, odor, over, doer`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 79. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:232`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 80. Typo: 'oder'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:237`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `order, older, coder, odder, odor, over, doer`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 81. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:237`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 82. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:245`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 83. Typo: 'als'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:250`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `also`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 84. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:250`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 85. Typo: 'als'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:256`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `also`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 86. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:256`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 87. Typo: 'als'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:263`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `also`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 88. Typo: 'vor'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:263`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `for`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 89. Typo: 'Komma'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:263`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Comma, Coma`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 90. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:263`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 91. Typo: 'Formate'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:268`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Format`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 92. Typo: 'Formate'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:286`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Format`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 93. Typo: 'Formate'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:295`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Format`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 94. Typo: 'Formate'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:300`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Format`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 95. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:305`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 96. Typo: 'als'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:310`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `also`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 97. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:324`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 98. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:341`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 99. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:347`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 100. Typo: 'ist'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:353`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `is, it, its, it's, sit, list`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 101. Typo: 'oder'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:353`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `order, older, coder, odder, odor, over, doer`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 102. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:362`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 103. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:367`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 104. Typo: 'als'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:367`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `also`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 105. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:396`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 106. Typo: 'Objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:450`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 107. Typo: 'Objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:460`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 108. Typo: 'Elemente'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:532`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Element, Elements`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 109. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:536`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 110. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:551`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 111. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:556`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 112. Typo: 'Feld'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\de\LC_MESSAGES\django.po:561`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Field`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 113. Typo: 'contener'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:34`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `container`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 114. Typo: 'contener'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:54`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `container`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 115. Typo: 'contener'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:59`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `container`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 116. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:59`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 117. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:168`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 118. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:172`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 119. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:185`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 120. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:190`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 121. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:217`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 122. Typo: 'requiere'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:243`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `require`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 123. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:345`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 124. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:378`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 125. Typo: 'inicial'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:418`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `initial, indicial`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 126. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:534`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 127. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:549`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 128. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:554`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 129. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\es\LC_MESSAGES\django.po:559`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 130. Typo: 'mis'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\et\LC_MESSAGES\django.po:198`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `miss, mist`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 131. Typo: 'versioon'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\et\LC_MESSAGES\django.po:558`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 132. Typo: 'versioon'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\et\LC_MESSAGES\django.po:562`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 133. Typo: 'versioon'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\et\LC_MESSAGES\django.po:566`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 134. Typo: 'versioon'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\et\LC_MESSAGES\django.po:570`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 135. Typo: 'versioon'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\et\LC_MESSAGES\django.po:574`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 136. Typo: 'versio'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fi\LC_MESSAGES\django.po:559`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 137. Typo: 'versio'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fi\LC_MESSAGES\django.po:563`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 138. Typo: 'versio'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fi\LC_MESSAGES\django.po:567`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 139. Typo: 'versio'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fi\LC_MESSAGES\django.po:571`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 140. Typo: 'versio'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fi\LC_MESSAGES\django.po:575`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 141. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:28`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 142. Typo: 'Informations'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:28`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Information`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 143. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:32`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 144. Typo: 'informations'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:32`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `information`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 145. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:36`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 146. Typo: 'informations'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:36`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `information`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 147. Typo: 'mot'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:40`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `not`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 148. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:40`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 149. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:48`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 150. Typo: 'Informations'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:48`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Information`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 151. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:52`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 152. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:56`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 153. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:60`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 154. Typo: 'Mot'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:92`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Not`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 155. Typo: 'informations'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:96`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `information`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 156. Typo: 'invalide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:108`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `invalid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 157. Typo: 'Informations'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:116`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Information`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 158. Typo: 'Informations'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:120`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Information`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 159. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:169`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 160. Typo: 'invalide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:173`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `invalid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 161. Typo: 'adresse'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:191`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `address`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 162. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:191`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 163. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:207`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 164. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:211`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 165. Typo: 'adresse'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:215`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `address`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 166. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:215`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 167. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:219`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 168. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:237`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 169. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:294`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 170. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:313`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 171. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:338`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 172. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:365`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 173. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:401`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 174. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:413`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 175. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:418`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 176. Typo: 'Lien'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:427`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Line`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 177. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:427`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 178. Typo: 'Lien'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:431`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Line`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 179. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:431`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 180. Typo: 'Lien'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:435`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Line`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 181. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:435`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 182. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:449`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 183. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:471`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 184. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:550`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 185. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:554`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 186. Typo: 'invalide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:558`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `invalid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 187. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:562`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 188. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\fr\LC_MESSAGES\django.po:566`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 189. Typo: 'elemet'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\hu\LC_MESSAGES\django.po:311`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `element`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 190. Typo: 'Nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\it\LC_MESSAGES\django.po:40`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 191. Typo: 'Impossibile'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\it\LC_MESSAGES\django.po:97`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Impossible`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 192. Typo: 'nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\it\LC_MESSAGES\django.po:101`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 193. Typo: 'Impossibile'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\it\LC_MESSAGES\django.po:138`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Impossible`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 194. Typo: 'nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\it\LC_MESSAGES\django.po:334`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 195. Typo: 'nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\it\LC_MESSAGES\django.po:344`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 196. Typo: 'nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\it\LC_MESSAGES\django.po:574`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 197. Typo: 'vai'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\lv\LC_MESSAGES\django.po:39`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `via, vie`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 198. Typo: 'vai'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\lv\LC_MESSAGES\django.po:197`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `via, vie`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 199. Typo: 'vai'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\lv\LC_MESSAGES\django.po:215`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `via, vie`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 200. Typo: 'vai'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\lv\LC_MESSAGES\django.po:224`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `via, vie`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 201. Typo: 'vai'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\lv\LC_MESSAGES\django.po:229`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `via, vie`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 202. Typo: 'vai'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\lv\LC_MESSAGES\django.po:345`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `via, vie`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 203. Typo: 'teksts'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\lv\LC_MESSAGES\django.po:447`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `texts`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 204. Typo: 'passord'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nb\LC_MESSAGES\django.po:37`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `password`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 205. Typo: 'Passord'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nb\LC_MESSAGES\django.po:90`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Password`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 206. Typo: 'som'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nb\LC_MESSAGES\django.po:199`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `some`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 207. Typo: 'lik'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nb\LC_MESSAGES\django.po:226`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `like, lick, link`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 208. Typo: 'lik'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nb\LC_MESSAGES\django.po:231`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `like, lick, link`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 209. Typo: 'komma'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nb\LC_MESSAGES\django.po:257`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `comma, coma`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 210. Typo: 'Objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nb\LC_MESSAGES\django.po:454`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 211. Typo: 'noen'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nb\LC_MESSAGES\django.po:567`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `none, neon`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 212. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:125`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 213. Typo: 'Methode'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:134`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Method`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 214. Typo: 'leeg'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:166`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `league`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 215. Typo: 'leeg'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:178`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `league`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 216. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:238`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 217. Typo: 'komma'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:253`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `comma, coma`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 218. Typo: 'komma'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:260`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `comma, coma`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 219. Typo: 'leeg'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:316`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `league`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 220. Typo: 'leeg'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:338`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `league`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 221. Typo: 'leeg'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:354`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `league`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 222. Typo: 'valide'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\nl\LC_MESSAGES\django.po:377`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `valid`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 223. Typo: 'adres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pl\LC_MESSAGES\django.po:190`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `address`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 224. Typo: 'adres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pl\LC_MESSAGES\django.po:210`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `address`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 225. Typo: 'adres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pl\LC_MESSAGES\django.po:218`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `address`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 226. Typo: 'daty'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pl\LC_MESSAGES\django.po:263`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `data, date`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 227. Typo: 'daty'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pl\LC_MESSAGES\django.po:285`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `data, date`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 228. Typo: 'daty'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pl\LC_MESSAGES\django.po:546`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `data, date`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 229. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:56`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 230. Typo: 'Nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:88`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 231. Typo: 'erro'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:104`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `error`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 232. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:165`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 233. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:177`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 234. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:182`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 235. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:187`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 236. Typo: 'itens'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:306`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `items`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 237. Typo: 'itens'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:311`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `items`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 238. Typo: 'Nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:333`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 239. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:333`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 240. Typo: 'nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:343`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 241. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:343`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 242. Typo: 'itens'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:368`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `items`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 243. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:376`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 244. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:532`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 245. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:547`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 246. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:552`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 247. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt\LC_MESSAGES\django.po:557`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 248. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:60`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 249. Typo: 'Nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:92`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 250. Typo: 'erro'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:108`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `error`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 251. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:169`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 252. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:173`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 253. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:186`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 254. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:191`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 255. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:219`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 256. Typo: 'itens'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:310`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `items`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 257. Typo: 'itens'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:315`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `items`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 258. Typo: 'Nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:337`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 259. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:337`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 260. Typo: 'nome'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:347`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `gnome`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 261. Typo: 'caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:347`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 262. Typo: 'itens'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:372`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `items`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 263. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:380`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 264. Typo: 'termo'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:388`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `thermo`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 265. Typo: 'inicial'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:420`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `initial, indicial`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 266. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:536`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 267. Typo: 'Caracteres'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:546`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Characters`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 268. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:551`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 269. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:556`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 270. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\pt_BR\LC_MESSAGES\django.po:561`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 271. Typo: 'caractere'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:28`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `character`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 272. Typo: 'corect'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:32`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `correct`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 273. Typo: 'caractere'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:48`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `character`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 274. Typo: 'caractere'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:53`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `character`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 275. Typo: 'caractere'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:53`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `character`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 276. Typo: 'caractere'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:179`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `character`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 277. Typo: 'caractere'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:184`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `character`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 278. Typo: 'caractere'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:198`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `character`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 279. Typo: 'caractere'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:234`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `character`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 280. Typo: 'formate'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:261`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `format`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 281. Typo: 'formate'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:279`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `format`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 282. Typo: 'formate'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:288`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `format`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 283. Typo: 'formate'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:293`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `format`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 284. Typo: 'elemente'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:308`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `element, elements`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 285. Typo: 'caractere'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:340`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `character`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 286. Typo: 'incorect'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:431`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `incorrect`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 287. Typo: 'incorect'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:448`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `incorrect`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 288. Typo: 'elemente'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\ro\LC_MESSAGES\django.po:525`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `element, elements`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 289. Typo: 'parametre'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sk\LC_MESSAGES\django.po:96`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `parameter`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 290. Typo: 'objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sk\LC_MESSAGES\django.po:425`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 291. Typo: 'objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sk\LC_MESSAGES\django.po:442`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 292. Typo: 'Objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sk\LC_MESSAGES\django.po:452`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 293. Typo: 'sme'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:27`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `same, seme, some, sms`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 294. Typo: 'sme'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:47`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `same, seme, some, sms`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 295. Typo: 'sme'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:52`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `same, seme, some, sms`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 296. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:120`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 297. Typo: 'sme'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:161`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `same, seme, some, sms`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 298. Typo: 'sme'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:173`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `same, seme, some, sms`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 299. Typo: 'sme'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:178`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `same, seme, some, sms`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 300. Typo: 'sme'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:311`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `same, seme, some, sms`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 301. Typo: 'sme'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:349`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `same, seme, some, sms`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 302. Typo: 'stran'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:408`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `strand, strain`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 303. Typo: 'objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:425`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 304. Typo: 'Objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:442`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 305. Typo: 'Objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sl\LC_MESSAGES\django.po:452`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 306. Typo: 'objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sv\LC_MESSAGES\django.po:303`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 307. Typo: 'Objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sv\LC_MESSAGES\django.po:453`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 308. Typo: 'objekt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\sv\LC_MESSAGES\django.po:525`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `object`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 309. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:128`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 310. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:165`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 311. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:169`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 312. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:181`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 313. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:186`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 314. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:191`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 315. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:199`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 316. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:319`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 317. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:347`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 318. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:357`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 319. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:362`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 320. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:367`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 321. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:376`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 322. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:536`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 323. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:551`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 324. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:556`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 325. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr\LC_MESSAGES\django.po:561`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 326. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:121`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 327. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:158`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 328. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:162`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 329. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:174`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 330. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:179`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 331. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:184`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 332. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:192`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 333. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:312`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 334. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:340`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 335. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:350`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 336. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:529`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 337. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:544`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 338. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:549`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 339. Typo: 'Bu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\tr_TR\LC_MESSAGES\django.po:554`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `By, Be, But, Bug, Bun, Bud, Buy, Bum`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 340. Typo: 'thay'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\locale\vi\LC_MESSAGES\django.po:279`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `they, that`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 341. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 342. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 343. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 344. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 345. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 346. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 347. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 348. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 349. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 350. Typo: 'eACG'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `each`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 351. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 352. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 353. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 354. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 355. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 356. Typo: 'cACE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `cache`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 357. Typo: 'actived'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\css\bootstrap.min.css.map:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `activated`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 358. Typo: 'tE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 359. Typo: 'tE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 360. Typo: 'tE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 361. Typo: 'tE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 362. Typo: 'tE'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 363. Typo: 'inout'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `input, in out`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 364. Typo: 'iif'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `if`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 365. Typo: 'lenght'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `length`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 366. Typo: 'filetest'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `file test`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 367. Typo: 'inout'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `input, in out`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 368. Typo: 'isnt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `isn't`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 369. Typo: 'tring'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `trying, string, ring`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 370. Typo: 'ans'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `and`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 371. Typo: 'alog'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `along`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 372. Typo: 'iput'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `input`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 373. Typo: 'inout'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `input, in out`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 374. Typo: 'appen'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `append, happen, aspen`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 375. Typo: 'asser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `assert`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 376. Typo: 'describ'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `describe`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 377. Typo: 'displa'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `display`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 378. Typo: 'doed'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `does`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 379. Typo: 'erro'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `error`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 380. Typo: 'fillin'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `filling, fill in`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 381. Typo: 'generat'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `generate, general`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 382. Typo: 'globa'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `global`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 383. Typo: 'hel'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `help, hell, heal`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 384. Typo: 'inpu'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `input`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 385. Typo: 'mata'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `meta, mater`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 386. Typo: 'mor'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `more`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 387. Typo: 'retur'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `return`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 388. Typo: 'rotat'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `rotate`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 389. Typo: 'sav'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `save`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 390. Typo: 'seperate'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `separate`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 391. Typo: 'summar'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `summary, summer`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 392. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 393. Typo: 'versio'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `version`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 394. Typo: 'windo'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `window`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 395. Typo: 'inout'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `input, in out`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 396. Typo: 'checkt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `checked`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 397. Typo: 'debugg'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `debug`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 398. Typo: 'fo'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `of, for, to, do, go`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 399. Typo: 'sav'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `save`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 400. Typo: 'scrip'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `script`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 401. Typo: 'scripte'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `script, scripted`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 402. Typo: 'sme'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `same, seme, some, sms`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 403. Typo: 'tabe'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `table, tab`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 404. Typo: 'tabl'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `table`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 405. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 406. Typo: 'vie'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `via`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 407. Typo: 'windo'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `window`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 408. Typo: 'enew'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `new`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 409. Typo: 'assymetry'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `asymmetry`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 410. Typo: 'iif'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `if`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 411. Typo: 'isnt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `isn't`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 412. Typo: 'notin'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `noting, not in, notion`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 413. Typo: 'aas'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `ass, as`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 414. Typo: 'daa'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `data`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 415. Typo: 'struc'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `struct`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 416. Typo: 'juxt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `just`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 417. Typo: 'rcall'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `recall`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 418. Typo: 'seh'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `she`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 419. Typo: 'ser'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `set`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 420. Typo: 'dispaly'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `display`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 421. Typo: 'inout'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `input, in out`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 422. Typo: 'BraKet'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `bracket, brake`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 423. Typo: 'Ket'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:1`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Key, Kept`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 424. Typo: 'inout'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `input, in out`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 425. Typo: 'promt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `prompt`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 426. Typo: 'SectionIn'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\docs\js\highlight.pack.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `sectioning, section in`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 427. Typo: 'build-in'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\coreapi-0.1.1.js:1157`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `built-in`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 428. Typo: 'ue'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `use, due`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 429. Typo: 'ue'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `use, due`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 430. Typo: 'ue'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `use, due`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 431. Typo: 'ue'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `use, due`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 432. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 433. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 434. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 435. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 436. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 437. Typo: 'Te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `The, Be, We, To`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 438. Typo: 'Te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `The, Be, We, To`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 439. Typo: 'Te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `The, Be, We, To`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 440. Typo: 'Ue'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Use, Due`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 441. Typo: 'ot'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `to, of, or, not, it`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 442. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 443. Typo: 'ot'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `to, of, or, not, it`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 444. Typo: 'Ue'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `Use, Due`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 445. Typo: 'ot'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `to, of, or, not, it`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 446. Typo: 'te'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `the, be, we, to`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 447. Typo: 'ue'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `use, due`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 448. Typo: 'ue'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `use, due`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 449. Typo: 'Ot'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `To, Of, Or, Not, It`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 450. Typo: 'Ot'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\jquery-3.7.1.min.js:2`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `To, Of, Or, Not, It`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 451. Typo: 'isnt'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `rest_framework\static\rest_framework\js\prettify-min.js:24`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `isn't`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

#### 452. Typo: 'fo'

**Severity:** 🟢 LOW  
**Detector:** `codespell`

**Evidence:**

- **File:** `tests\test_routers.py:293`

**Intent:**

A spelling error was detected in the code. This may be in comments, strings, or identifiers.

**Attack Surface:**

- **Entry Point:** N/A (code quality issue)
- **Exposure:** May cause confusion or subtle bugs
- **Reach:** Limited security impact, mainly affects maintainability

**Risk Assessment:**

- **Impact:** Minimal - Code quality or minor information disclosure
- **Likelihood:** Low - Unlikely to cause security issues

**Recommended Fix:**

Replace with the correct spelling: `of, for, to, do, go`

**Verification:**

- Run codespell or similar tool to verify fix
- Ensure no new typos were introduced

---

## General Recommendations

### Immediate Actions

1. **Rotate all exposed secrets** - Assume they are compromised

### Preventive Measures

- **Pre-commit hooks**: Use gitleaks or similar to prevent secret commits
- **CI/CD scanning**: Integrate security scanning into the build pipeline
- **Dependency monitoring**: Use Dependabot or Snyk for continuous monitoring
- **Code review**: Include security review in the PR process
- **Developer training**: Educate team on secure coding practices

---

## About This Report

This security report was generated by the **AI-Enabled Cybersecurity Scanner** developed as part of the MIT Blended AI+X Program (Track 3).

### Limitations

- This is a **static analysis** tool and may produce false positives
- Not all vulnerabilities can be detected through pattern matching
- Human review is essential for accurate risk assessment
- This tool does **not** exploit or test vulnerabilities

### Responsible Disclosure

If this scan revealed potential vulnerabilities in third-party software:

1. Do **NOT** publicly disclose specific vulnerability details
2. Contact the maintainers privately through their security policy
3. Allow reasonable time for patches before any disclosure
4. Follow the project's responsible disclosure guidelines

---

*Report generated on 2026-01-07 07:03:46 UTC*  
*MIT Blended AI+X PBL - AI-Enabled Cybersecurity*