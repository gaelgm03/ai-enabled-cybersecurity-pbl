"""
SQL Injection Pattern Detector (Week 4).

Detects potential SQL injection vulnerabilities through static pattern analysis:
- String concatenation in SQL queries
- f-strings / format() building queries
- ORM raw query methods
- Multi-language support (Python, JavaScript, PHP)

MIT Blended AI+X PBL - AI-Enabled Cybersecurity
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional

from ..schema import Finding, FindingType, Severity


class SQLiDetector:
    """Detects potential SQL injection patterns in source code."""
    
    DETECTOR_NAME = "sqli-patterns"
    
    # Directories to skip
    SKIP_DIRS = [
        "node_modules", ".git", "__pycache__", "venv", ".venv", 
        "dist", "build", ".tox", ".pytest_cache", "migrations",
        "tests", "test", "__tests__"  # Often contain intentional test patterns
    ]
    
    # File extensions to scan by language
    LANGUAGE_EXTENSIONS = {
        "python": [".py"],
        "javascript": [".js", ".jsx", ".ts", ".tsx", ".mjs"],
        "php": [".php"],
    }
    
    # Python SQL injection patterns
    PYTHON_PATTERNS = [
        # String concatenation with SQL keywords
        (
            r'(?:execute|executemany|cursor\.execute)\s*\(\s*["\'](?:SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER)[^"\']*["\']?\s*\+',
            "String concatenation in execute()",
            Severity.HIGH,
            "Direct string concatenation in SQL query"
        ),
        # f-string SQL queries
        (
            r'(?:execute|executemany|cursor\.execute)\s*\(\s*f["\'](?:SELECT|INSERT|UPDATE|DELETE)',
            "f-string SQL query",
            Severity.HIGH,
            "f-string used to build SQL query - vulnerable to injection"
        ),
        # format() SQL queries
        (
            r'(?:execute|executemany|cursor\.execute)\s*\(\s*["\'](?:SELECT|INSERT|UPDATE|DELETE)[^"\']*["\']\.format\s*\(',
            ".format() SQL query",
            Severity.HIGH,
            ".format() used to build SQL query - vulnerable to injection"
        ),
        # % string formatting in SQL
        (
            r'(?:execute|executemany|cursor\.execute)\s*\(\s*["\'](?:SELECT|INSERT|UPDATE|DELETE)[^"\']*%s[^"\']*["\']?\s*%',
            "% formatting in SQL query",
            Severity.MEDIUM,
            "% string formatting in SQL - may be vulnerable if not parameterized"
        ),
        # SQLAlchemy text() with variables
        (
            r'text\s*\(\s*f["\']',
            "SQLAlchemy text() with f-string",
            Severity.HIGH,
            "SQLAlchemy text() with f-string - use bound parameters instead"
        ),
        # Raw SQL in Django
        (
            r'\.raw\s*\(\s*f["\']|\.raw\s*\(\s*["\'][^"\']*["\']\.format|\.raw\s*\(\s*["\'][^"\']*["\']?\s*%',
            "Django raw() with string formatting",
            Severity.HIGH,
            "Django raw() with string formatting - vulnerable to injection"
        ),
        # execute with variable (not parameterized)
        (
            r'cursor\.execute\s*\(\s*(?:sql|query|stmt|sql_query|sql_string)\s*[,\)]',
            "Variable SQL in execute()",
            Severity.MEDIUM,
            "Variable passed to execute() - verify it uses parameterized queries"
        ),
        # SQLAlchemy session.execute with text
        (
            r'session\.execute\s*\(\s*text\s*\(\s*f["\']',
            "SQLAlchemy session.execute with text f-string",
            Severity.HIGH,
            "SQLAlchemy execute with text() f-string - use bound parameters"
        ),
        # psycopg2/mysql connector patterns
        (
            r'\.execute\s*\(\s*["\'](?:SELECT|INSERT|UPDATE|DELETE)[^"\']*\{[^}]+\}[^"\']*["\']\.format',
            "SQL with .format() interpolation",
            Severity.HIGH,
            "SQL query with .format() string interpolation"
        ),
    ]
    
    # JavaScript/Node.js SQL injection patterns
    JAVASCRIPT_PATTERNS = [
        # Template literal SQL
        (
            r'(?:query|execute|raw)\s*\(\s*`(?:SELECT|INSERT|UPDATE|DELETE)[^`]*\$\{',
            "Template literal SQL query",
            Severity.HIGH,
            "Template literal with variable interpolation in SQL"
        ),
        # String concatenation
        (
            r'(?:query|execute)\s*\(\s*["\'](?:SELECT|INSERT|UPDATE|DELETE)[^"\']*["\']\s*\+',
            "String concatenation in SQL",
            Severity.HIGH,
            "String concatenation used to build SQL query"
        ),
        # Sequelize raw query
        (
            r'sequelize\.query\s*\(\s*`[^`]*\$\{',
            "Sequelize raw query with interpolation",
            Severity.HIGH,
            "Sequelize raw query with template interpolation"
        ),
        # Knex.js raw
        (
            r'\.raw\s*\(\s*`[^`]*\$\{',
            "Knex raw() with interpolation",
            Severity.HIGH,
            "Knex raw() with template literal interpolation"
        ),
        # MySQL/pg module
        (
            r'connection\.query\s*\(\s*["\'](?:SELECT|INSERT|UPDATE|DELETE)[^"\']*["\']\s*\+',
            "mysql/pg query concatenation",
            Severity.HIGH,
            "Database query with string concatenation"
        ),
    ]
    
    # PHP SQL injection patterns
    PHP_PATTERNS = [
        # Variable in query string
        (
            r'(?:mysql_query|mysqli_query|pg_query)\s*\(\s*[^,]*\$',
            "PHP query with variable",
            Severity.HIGH,
            "Variable interpolation in SQL query function"
        ),
        # String concatenation
        (
            r'(?:mysql_query|mysqli_query|pg_query)\s*\(\s*["\'](?:SELECT|INSERT|UPDATE|DELETE)[^"\']*["\']\s*\.\s*\$',
            "PHP query concatenation",
            Severity.HIGH,
            "String concatenation with variable in SQL query"
        ),
        # PDO without prepared statements
        (
            r'\$\w+->query\s*\(\s*["\'](?:SELECT|INSERT|UPDATE|DELETE)[^"\']*["\']\s*\.\s*\$',
            "PDO query with concatenation",
            Severity.HIGH,
            "PDO query() with string concatenation - use prepare() instead"
        ),
        # Double-quoted string with variable
        (
            r'(?:mysql_query|mysqli_query)\s*\([^)]*"[^"]*\$\w+[^"]*"',
            "PHP query with variable in double quotes",
            Severity.HIGH,
            "Variable interpolation in double-quoted SQL string"
        ),
    ]
    
    def __init__(self, target_path: str):
        self.target_path = Path(target_path)
    
    def scan(self) -> List[Finding]:
        """Scan for SQL injection patterns."""
        findings = []
        
        for file_path in self._get_files():
            lang = self._detect_language(file_path)
            if not lang:
                continue
            
            patterns = self._get_patterns_for_language(lang)
            if not patterns:
                continue
            
            file_findings = self._scan_file(file_path, patterns, lang)
            findings.extend(file_findings)
        
        return findings
    
    def _get_files(self) -> List[Path]:
        """Get files to scan, excluding skip directories."""
        files = []
        all_extensions = []
        for exts in self.LANGUAGE_EXTENSIONS.values():
            all_extensions.extend(exts)
        
        for item in self.target_path.rglob("*"):
            if not item.is_file():
                continue
            
            # Check extension
            if item.suffix.lower() not in all_extensions:
                continue
            
            # Check if in skip directory
            skip = False
            for part in item.parts:
                if part in self.SKIP_DIRS:
                    skip = True
                    break
            
            if not skip:
                files.append(item)
        
        return files
    
    def _detect_language(self, file_path: Path) -> Optional[str]:
        """Detect programming language from file extension."""
        ext = file_path.suffix.lower()
        for lang, extensions in self.LANGUAGE_EXTENSIONS.items():
            if ext in extensions:
                return lang
        return None
    
    def _get_patterns_for_language(self, lang: str) -> List[Tuple]:
        """Get SQL injection patterns for a specific language."""
        patterns_map = {
            "python": self.PYTHON_PATTERNS,
            "javascript": self.JAVASCRIPT_PATTERNS,
            "php": self.PHP_PATTERNS,
        }
        return patterns_map.get(lang, [])
    
    def _scan_file(self, file_path: Path, patterns: List[Tuple], lang: str) -> List[Finding]:
        """Scan a single file for SQL injection patterns."""
        findings = []
        
        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            lines = content.splitlines()
            
            for i, line in enumerate(lines, 1):
                # Skip comment lines
                stripped = line.strip()
                if self._is_comment_line(stripped, lang):
                    continue
                
                for pattern, pattern_name, severity, description in patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        # Get context snippet (redacted)
                        snippet = self._get_redacted_snippet(line)
                        
                        finding = Finding(
                            finding_type=FindingType.SQLI,
                            severity=severity,
                            title=f"Potential SQL Injection: {pattern_name}",
                            description=description,
                            file_path=str(file_path),
                            line_number=i,
                            detector=self.DETECTOR_NAME,
                            raw_match="[REDACTED]",
                            redacted_match=snippet,
                            metadata={
                                "language": lang,
                                "pattern_type": pattern_name,
                                "pattern": pattern[:50] + "..." if len(pattern) > 50 else pattern,
                            }
                        )
                        findings.append(finding)
                        break  # One finding per line
                        
        except Exception as e:
            pass  # Skip files that can't be read
        
        return findings
    
    def _is_comment_line(self, line: str, lang: str) -> bool:
        """Check if a line is a comment."""
        if lang == "python":
            return line.startswith("#")
        elif lang in ["javascript", "php"]:
            return line.startswith("//") or line.startswith("/*") or line.startswith("*")
        return False
    
    def _get_redacted_snippet(self, line: str, max_len: int = 80) -> str:
        """Get a redacted snippet of the line for display."""
        # Trim whitespace
        snippet = line.strip()
        
        # Truncate if too long
        if len(snippet) > max_len:
            snippet = snippet[:max_len] + "..."
        
        # Redact potential sensitive values in strings
        # Replace quoted strings that might contain sensitive data
        snippet = re.sub(r'(["\'])(?:(?!\1)[^\\]|\\.)*\1', r'\1[REDACTED]\1', snippet)
        
        return snippet
    
    @staticmethod
    def is_available() -> bool:
        """This detector is always available (regex-based)."""
        return True
