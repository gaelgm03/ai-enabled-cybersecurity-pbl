"""
LLM-based remediation instruction generator.

IMPORTANT: The LLM is ONLY used for generating fix instructions and prevention guidance.
All detection is done deterministically by the detector modules.
Secrets are ALWAYS redacted before being sent to the LLM.

Supported providers:
- anthropic: Anthropic Claude API (requires ANTHROPIC_API_KEY)
- ollama: Local Ollama instance (free, no API key required)
- none/templates: Built-in templates (always available)
"""

import os
import json
import urllib.request
import urllib.error
from typing import Optional

from .schema import Finding, FindingType
from .redaction import Redactor

# Default Ollama configuration
DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_OLLAMA_MODEL = "llama3.1:8b"
OLLAMA_TIMEOUT = 120  # seconds (longer for first request when model loads)


def is_ollama_available(base_url: str = None) -> bool:
    """Check if Ollama is running and reachable."""
    url = (base_url or os.environ.get("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL)).rstrip("/")
    try:
        req = urllib.request.Request(f"{url}/api/tags", method="GET")
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status == 200
    except (urllib.error.URLError, urllib.error.HTTPError, OSError):
        return False


def auto_select_provider() -> str:
    """
    Auto-select the best available LLM provider.
    Priority: anthropic (if key exists) -> ollama (if running) -> templates
    """
    if os.environ.get("ANTHROPIC_API_KEY"):
        return "anthropic"
    if is_ollama_available():
        return "ollama"
    return "none"


class LLMRemediator:
    """
    Generates remediation instructions using an LLM.
    
    Supports:
    - Anthropic Claude API (requires API key)
    - Ollama local LLM (free, no API key)
    - Template-based fallback (always available)
    """
    
    def __init__(self, provider: str = "auto", api_key: Optional[str] = None):
        """
        Initialize the LLM remediator.
        
        Args:
            provider: LLM provider - "anthropic", "ollama", "none", or "auto"
            api_key: Anthropic API key (optional, uses env var if not provided)
        """
        self.provider = provider if provider != "auto" else auto_select_provider()
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.anthropic_client = None
        
        # Ollama configuration
        self.ollama_base_url = os.environ.get("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL).rstrip("/")
        self.ollama_model = os.environ.get("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL)
        
        # Initialize Anthropic client if needed
        if self.provider == "anthropic" and self.api_key:
            try:
                import anthropic
                self.anthropic_client = anthropic.Anthropic(api_key=self.api_key)
            except ImportError:
                print("[INFO] anthropic package not installed. Falling back to templates.")
                self.provider = "none"
    
    def generate_remediation(self, finding: Finding) -> tuple[str, str]:
        """
        Generate remediation and prevention guidance for a finding.
        
        Returns:
            Tuple of (remediation_instructions, prevention_guidance)
        """
        if self.provider == "anthropic" and self.anthropic_client:
            return self._anthropic_remediation(finding)
        elif self.provider == "ollama":
            return self._ollama_remediation(finding)
        else:
            return self._template_remediation(finding)
    
    def _get_prompt(self, finding: Finding) -> str:
        """Build the prompt for LLM remediation."""
        context = self._build_safe_context(finding)
        
        return f"""You are a security expert providing remediation guidance.

Based on the following security finding, provide:
1. Step-by-step remediation instructions (how to fix this specific issue)
2. Prevention guidance (how to prevent similar issues in the future)

Finding Details:
{context}

Respond in this exact format:
REMEDIATION:
[Your remediation steps here]

PREVENTION:
[Your prevention guidance here]

Keep responses concise and actionable. Do not include any actual secrets or sensitive values."""
    
    def _anthropic_remediation(self, finding: Finding) -> tuple[str, str]:
        """Generate remediation using Anthropic Claude API."""
        try:
            prompt = self._get_prompt(finding)
            
            message = self.anthropic_client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response = message.content[0].text
            return self._parse_llm_response(response)
            
        except Exception as e:
            print(f"[WARN] Anthropic remediation failed: {e}")
            return self._template_remediation(finding)
    
    def _ollama_remediation(self, finding: Finding) -> tuple[str, str]:
        """Generate remediation using local Ollama instance."""
        try:
            prompt = self._get_prompt(finding)
            
            # Prepare request payload
            payload = json.dumps({
                "model": self.ollama_model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 500,
                }
            }).encode("utf-8")
            
            req = urllib.request.Request(
                f"{self.ollama_base_url}/api/generate",
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            
            with urllib.request.urlopen(req, timeout=OLLAMA_TIMEOUT) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                response = result.get("response", "")
                return self._parse_llm_response(response)
                
        except urllib.error.URLError as e:
            print(f"[WARN] Ollama connection failed: {e.reason}")
            return self._template_remediation(finding)
        except Exception as e:
            print(f"[WARN] Ollama remediation failed: {e}")
            return self._template_remediation(finding)
    
    def _build_safe_context(self, finding: Finding) -> str:
        """Build a safe context string with all secrets redacted."""
        lines = [
            f"Type: {finding.finding_type.value}",
            f"Severity: {finding.severity.value}",
            f"Title: {finding.title}",
            f"Description: {finding.description}",
        ]
        
        if finding.file_path:
            lines.append(f"File: {finding.file_path}")
        
        if finding.line_number:
            lines.append(f"Line: {finding.line_number}")
        
        # For secrets, only include the redacted version
        if finding.finding_type == FindingType.SECRET:
            lines.append(f"Match (redacted): {finding.redacted_match}")
            if finding.metadata.get("secret_type"):
                lines.append(f"Secret Type: {finding.metadata['secret_type']}")
        
        # For dependencies, include package info
        if finding.finding_type == FindingType.DEPENDENCY:
            meta = finding.metadata
            if meta.get("package"):
                lines.append(f"Package: {meta['package']}")
            if meta.get("installed_version"):
                lines.append(f"Version: {meta['installed_version']}")
            if meta.get("vuln_id"):
                lines.append(f"Vulnerability ID: {meta['vuln_id']}")
            if meta.get("fix_versions"):
                lines.append(f"Fix Versions: {', '.join(meta['fix_versions'])}")
        
        # For typos, include the suggestion
        if finding.finding_type == FindingType.TYPO:
            meta = finding.metadata
            if meta.get("typo"):
                lines.append(f"Typo: {meta['typo']}")
            if meta.get("suggestion"):
                lines.append(f"Suggestion: {meta['suggestion']}")
        
        return "\n".join(lines)
    
    def _parse_llm_response(self, response: str) -> tuple[str, str]:
        """Parse LLM response into remediation and prevention sections."""
        remediation = ""
        prevention = ""
        
        if "REMEDIATION:" in response and "PREVENTION:" in response:
            parts = response.split("PREVENTION:")
            remediation = parts[0].replace("REMEDIATION:", "").strip()
            prevention = parts[1].strip() if len(parts) > 1 else ""
        else:
            # If format not followed, use whole response as remediation
            remediation = response.strip()
        
        return remediation, prevention
    
    def _template_remediation(self, finding: Finding) -> tuple[str, str]:
        """Generate template-based remediation (fallback when no LLM available)."""
        
        if finding.finding_type == FindingType.SECRET:
            return self._secret_template(finding)
        elif finding.finding_type == FindingType.DEPENDENCY:
            return self._dependency_template(finding)
        elif finding.finding_type == FindingType.TYPO:
            return self._typo_template(finding)
        else:
            return ("Review and address this finding.", "Implement security best practices.")
    
    def _secret_template(self, finding: Finding) -> tuple[str, str]:
        """Template for secret findings."""
        secret_type = finding.metadata.get("secret_type", "credential")
        
        remediation = f"""1. **Immediately rotate** the exposed {secret_type}
2. Review git history to ensure the secret is not in previous commits
3. If committed, consider the secret compromised and generate a new one
4. Remove the hardcoded secret from the code
5. Use environment variables or a secrets manager instead"""
        
        prevention = f"""- Never commit secrets to version control
- Use `.gitignore` to exclude files containing secrets
- Use environment variables for sensitive configuration
- Consider using pre-commit hooks (e.g., gitleaks) to catch secrets before commit
- Use a secrets manager (e.g., HashiCorp Vault, AWS Secrets Manager)"""
        
        return remediation, prevention
    
    def _dependency_template(self, finding: Finding) -> tuple[str, str]:
        """Template for dependency findings."""
        meta = finding.metadata
        package = meta.get("package", "the package")
        fix_versions = meta.get("fix_versions", [])
        
        if fix_versions:
            version_str = f"version {fix_versions[0]}"
        else:
            version_str = "the latest secure version"
        
        remediation = f"""1. Update `{package}` to {version_str}
2. Run tests to ensure compatibility
3. Review the changelog for breaking changes
4. Deploy the updated dependency"""
        
        prevention = """- Regularly audit dependencies with `pip-audit` or `npm audit`
- Enable Dependabot or similar automated security updates
- Pin dependency versions and update intentionally
- Remove unused dependencies
- Subscribe to security advisories for critical dependencies"""
        
        return remediation, prevention
    
    def _typo_template(self, finding: Finding) -> tuple[str, str]:
        """Template for typo findings."""
        meta = finding.metadata
        typo = meta.get("typo", "the typo")
        suggestion = meta.get("suggestion", "the correct spelling")
        
        remediation = f"""1. Replace `{typo}` with `{suggestion}`
2. Search for other occurrences in the codebase
3. If it's in user-facing content, update translations if applicable"""
        
        prevention = """- Use a spell checker in your IDE
- Add codespell to your CI/CD pipeline
- Maintain a custom dictionary for domain-specific terms
- Enable spell check in your code editor"""
        
        return remediation, prevention


def enrich_findings_with_remediation(
    findings: list,
    provider: str = "auto",
    api_key: Optional[str] = None,
    verbose: bool = False
) -> list:
    """
    Enrich a list of findings with LLM-generated remediation.
    
    Args:
        findings: List of Finding objects to enrich
        provider: LLM provider - "anthropic", "ollama", "none", or "auto"
        api_key: Anthropic API key (optional)
        verbose: Print which provider is being used
    
    This is the main entry point for adding remediation to findings.
    """
    remediator = LLMRemediator(provider=provider, api_key=api_key)
    
    if verbose:
        provider_name = remediator.provider
        if provider_name == "ollama":
            print(f"    Using Ollama ({remediator.ollama_model})")
        elif provider_name == "anthropic":
            print("    Using Anthropic Claude")
        else:
            print("    Using built-in templates")
    
    for finding in findings:
        remediation, prevention = remediator.generate_remediation(finding)
        finding.remediation = remediation
        finding.prevention = prevention
    
    return findings
