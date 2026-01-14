"""
Anthropic Claude adapter for API-based evaluation.

MIT Blended AI+X PBL - AI-Enabled Cybersecurity
"""

import os
from typing import Optional
from .base_adapter import BaseAdapter, ClassificationResult

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


class AnthropicAdapter(BaseAdapter):
    """
    Adapter for Anthropic Claude API.
    
    Requires ANTHROPIC_API_KEY environment variable or explicit key.
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-haiku-20240307"):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model
        self._client = None
    
    @property
    def name(self) -> str:
        return f"anthropic:{self.model.split('-')[2] if '-' in self.model else self.model}"
    
    def is_available(self) -> bool:
        """Check if Anthropic API is available."""
        if not ANTHROPIC_AVAILABLE:
            return False
        if not self.api_key:
            return False
        return True
    
    def _get_client(self):
        """Get or create the Anthropic client."""
        if self._client is None and self.is_available():
            self._client = anthropic.Anthropic(api_key=self.api_key)
        return self._client
    
    def classify(
        self,
        snippet: str,
        category: str,
        language: str,
        context: str = ""
    ) -> ClassificationResult:
        """Classify using Anthropic Claude API."""
        if not self.is_available():
            missing = []
            if not ANTHROPIC_AVAILABLE:
                missing.append("anthropic package not installed")
            if not self.api_key:
                missing.append("ANTHROPIC_API_KEY not set")
            return ClassificationResult(
                is_vulnerable=False,
                confidence=0.0,
                rationale=f"Anthropic not available: {', '.join(missing)}",
                raw_response="ERROR: Anthropic not available"
            )
        
        prompt = self.get_prompt(snippet, category, language)
        
        try:
            client = self._get_client()
            message = client.messages.create(
                model=self.model,
                max_tokens=256,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            response = message.content[0].text.strip()
            return self._parse_response(response)
            
        except Exception as e:
            return ClassificationResult(
                is_vulnerable=False,
                confidence=0.0,
                rationale=f"API error: {str(e)[:100]}",
                raw_response=f"ERROR: {str(e)}"
            )
    
    def _parse_response(self, response: str) -> ClassificationResult:
        """Parse the LLM response to extract classification."""
        lines = response.strip().split('\n')
        
        first_line = lines[0].strip().upper() if lines else ""
        rationale = ' '.join(lines[1:]).strip() if len(lines) > 1 else ""
        
        if "VULNERABLE" in first_line:
            return ClassificationResult(
                is_vulnerable=True,
                confidence=0.95,
                rationale=rationale or "Classified as vulnerable",
                raw_response=response
            )
        elif "SAFE" in first_line:
            return ClassificationResult(
                is_vulnerable=False,
                confidence=0.95,
                rationale=rationale or "Classified as safe",
                raw_response=response
            )
        else:
            vuln_indicators = ["vulnerable", "security issue", "injection", "exposed", "hardcoded", "leak"]
            safe_indicators = ["safe", "placeholder", "example", "test", "false positive", "benign"]
            
            response_lower = response.lower()
            vuln_score = sum(1 for ind in vuln_indicators if ind in response_lower)
            safe_score = sum(1 for ind in safe_indicators if ind in response_lower)
            
            is_vulnerable = vuln_score > safe_score
            confidence = 0.7 if vuln_score != safe_score else 0.5
            
            return ClassificationResult(
                is_vulnerable=is_vulnerable,
                confidence=confidence,
                rationale=f"Inferred from response (vuln:{vuln_score}, safe:{safe_score})",
                raw_response=response
            )
