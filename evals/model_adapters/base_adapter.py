"""
Base adapter interface for evaluation models.

MIT Blended AI+X PBL - AI-Enabled Cybersecurity
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple


@dataclass
class ClassificationResult:
    """Result of a vulnerability classification."""
    is_vulnerable: bool
    confidence: float
    rationale: str
    raw_response: str = ""


class BaseAdapter(ABC):
    """Abstract base class for model adapters."""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the model name for reporting."""
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if the model is available for use."""
        pass
    
    @abstractmethod
    def classify(
        self,
        snippet: str,
        category: str,
        language: str,
        context: str = ""
    ) -> ClassificationResult:
        """
        Classify a code snippet as vulnerable or safe.
        
        Args:
            snippet: The code snippet to classify
            category: Category (typo, secret, sqli)
            language: Programming language
            context: Additional context (optional)
        
        Returns:
            ClassificationResult with prediction and rationale
        """
        pass
    
    def get_prompt(self, snippet: str, category: str, language: str) -> str:
        """Generate the classification prompt."""
        category_descriptions = {
            "typo": "a typo/spelling error (vs a legitimate variable/identifier name)",
            "secret": "an exposed secret/credential (vs a placeholder/example value)",
            "sqli": "a SQL injection vulnerability (vs safe parameterized query)",
        }
        
        cat_desc = category_descriptions.get(category, f"a {category} vulnerability")
        
        return f"""You are a security code reviewer. Analyze this code snippet and determine if it contains {cat_desc}.

Category: {category}
Language: {language}

Snippet:
```{language}
{snippet}
```

Respond with EXACTLY one of these two words on the first line:
- VULNERABLE - if this is a real security issue requiring a fix
- SAFE - if this is a false positive, benign pattern, or intentional test/example

Then on the next line, provide a brief one-sentence rationale.

Example response format:
VULNERABLE
This contains a hardcoded API key that should be moved to environment variables.

OR

SAFE
This is a placeholder value clearly marked as an example."""
