"""
Ollama adapter for local LLM evaluation.

MIT Blended AI+X PBL - AI-Enabled Cybersecurity
"""

import subprocess
import json
import re
from typing import Optional
from .base_adapter import BaseAdapter, ClassificationResult


class OllamaAdapter(BaseAdapter):
    """
    Adapter for Ollama local LLM models.
    
    Supported models: llama3.1:8b, mistral:7b, codellama, etc.
    """
    
    def __init__(self, model: str = "llama3.1:8b"):
        self.model = model
        self._available: Optional[bool] = None
    
    @property
    def name(self) -> str:
        return f"ollama:{self.model}"
    
    def is_available(self) -> bool:
        """Check if Ollama is installed and the model is available."""
        if self._available is not None:
            return self._available
        
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode != 0:
                self._available = False
                return False
            
            self._available = True
            return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            self._available = False
            return False
    
    def classify(
        self,
        snippet: str,
        category: str,
        language: str,
        context: str = ""
    ) -> ClassificationResult:
        """Classify using Ollama LLM."""
        if not self.is_available():
            return ClassificationResult(
                is_vulnerable=False,
                confidence=0.0,
                rationale="Ollama not available",
                raw_response="ERROR: Ollama not available"
            )
        
        prompt = self.get_prompt(snippet, category, language)
        
        try:
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True,
                text=True,
                timeout=60,
                encoding='utf-8',
                errors='replace'
            )
            
            if result.returncode != 0:
                return ClassificationResult(
                    is_vulnerable=False,
                    confidence=0.0,
                    rationale=f"Ollama error: {result.stderr[:100]}",
                    raw_response=result.stderr
                )
            
            response = result.stdout.strip()
            return self._parse_response(response)
            
        except subprocess.TimeoutExpired:
            return ClassificationResult(
                is_vulnerable=False,
                confidence=0.0,
                rationale="Ollama timeout",
                raw_response="ERROR: Timeout"
            )
        except Exception as e:
            return ClassificationResult(
                is_vulnerable=False,
                confidence=0.0,
                rationale=f"Error: {str(e)[:100]}",
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
                confidence=0.9,
                rationale=rationale or "Classified as vulnerable",
                raw_response=response
            )
        elif "SAFE" in first_line:
            return ClassificationResult(
                is_vulnerable=False,
                confidence=0.9,
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
            confidence = 0.6 if vuln_score != safe_score else 0.5
            
            return ClassificationResult(
                is_vulnerable=is_vulnerable,
                confidence=confidence,
                rationale=f"Inferred from response (vuln:{vuln_score}, safe:{safe_score})",
                raw_response=response
            )
