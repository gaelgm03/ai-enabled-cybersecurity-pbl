"""
Secure Secrets Management - Best Practices
============================================
MIT Blended AI+X Program - Week 3

PURPOSE: Demonstrate secure patterns for handling credentials.

This module shows the CORRECT way to manage secrets:
1. Environment variables
2. Configuration files (outside repo)
3. Secrets managers
4. Validation and error handling
"""

import os
from typing import Optional
from dataclasses import dataclass


# =============================================================================
# SECURE PATTERN 1: Environment Variables
# =============================================================================

def get_api_key_from_env(key_name: str, required: bool = True) -> Optional[str]:
    """
    SECURE: Retrieve API key from environment variable.
    
    Environment variables are:
    - Not committed to version control
    - Configurable per environment (dev, staging, prod)
    - Easy to rotate without code changes
    - Supported by all deployment platforms
    """
    value = os.environ.get(key_name)
    
    if required and not value:
        raise EnvironmentError(
            f"Required environment variable '{key_name}' is not set. "
            f"Please set it before running the application."
        )
    
    return value


@dataclass
class SecureConfig:
    """
    SECURE: Configuration class that loads secrets from environment.
    
    This pattern ensures:
    - Secrets are never in source code
    - Configuration is explicit about required variables
    - Missing secrets fail fast with clear error messages
    """
    
    # Public configuration (safe to hardcode)
    app_name: str = "MyApplication"
    debug: bool = False
    log_level: str = "INFO"
    
    # Secrets loaded from environment
    database_url: Optional[str] = None
    api_key: Optional[str] = None
    jwt_secret: Optional[str] = None
    
    @classmethod
    def from_environment(cls) -> "SecureConfig":
        """
        Factory method to create config from environment variables.
        
        Usage:
            config = SecureConfig.from_environment()
        """
        return cls(
            app_name=os.environ.get("APP_NAME", "MyApplication"),
            debug=os.environ.get("DEBUG", "false").lower() == "true",
            log_level=os.environ.get("LOG_LEVEL", "INFO"),
            database_url=os.environ.get("DATABASE_URL"),
            api_key=os.environ.get("API_KEY"),
            jwt_secret=os.environ.get("JWT_SECRET"),
        )
    
    def validate(self) -> None:
        """Validate that all required secrets are present."""
        missing = []
        
        if not self.database_url:
            missing.append("DATABASE_URL")
        if not self.api_key:
            missing.append("API_KEY")
        if not self.jwt_secret:
            missing.append("JWT_SECRET")
        
        if missing:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing)}"
            )


# =============================================================================
# SECURE PATTERN 2: External Configuration Files
# =============================================================================

def load_config_file(config_path: str = None) -> dict:
    """
    SECURE: Load configuration from a file outside the repository.
    
    Best practices:
    - Store config file outside the repo (e.g., /etc/myapp/config.json)
    - Set restrictive file permissions (chmod 600)
    - Add config file path to .gitignore
    - Use different config files per environment
    """
    import json
    
    # Default locations to check (outside repo)
    default_paths = [
        os.path.expanduser("~/.config/myapp/config.json"),
        "/etc/myapp/config.json",
        os.environ.get("CONFIG_PATH", ""),
    ]
    
    config_path = config_path or next(
        (p for p in default_paths if p and os.path.exists(p)), 
        None
    )
    
    if not config_path:
        print("[SECURE] No external config file found, using environment variables")
        return {}
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        print(f"[SECURE] Loaded config from: {config_path}")
        return config
    except (IOError, json.JSONDecodeError) as e:
        print(f"[SECURE] Could not load config file: {e}")
        return {}


# =============================================================================
# SECURE PATTERN 3: Secrets Manager Integration (Conceptual)
# =============================================================================

class SecretsManager:
    """
    SECURE: Abstraction for external secrets management.
    
    In production, this would integrate with:
    - AWS Secrets Manager
    - HashiCorp Vault
    - Azure Key Vault
    - Google Secret Manager
    - Kubernetes Secrets
    
    Benefits:
    - Centralized secret storage
    - Audit logging of secret access
    - Automatic rotation support
    - Fine-grained access control
    """
    
    def __init__(self, provider: str = "environment"):
        """
        Initialize secrets manager.
        
        Args:
            provider: "environment", "aws", "vault", "azure", "gcp"
        """
        self.provider = provider
        print(f"[SECURE] SecretsManager initialized with provider: {provider}")
    
    def get_secret(self, secret_name: str) -> Optional[str]:
        """
        Retrieve a secret by name.
        
        In production, this would call the actual secrets manager API.
        For this demo, we fall back to environment variables.
        """
        if self.provider == "environment":
            return os.environ.get(secret_name)
        
        # Placeholder for actual secrets manager integration
        # In real implementation:
        # if self.provider == "aws":
        #     return self._get_from_aws(secret_name)
        # elif self.provider == "vault":
        #     return self._get_from_vault(secret_name)
        
        print(f"[SECURE] Would fetch '{secret_name}' from {self.provider}")
        return None
    
    def rotate_secret(self, secret_name: str) -> bool:
        """
        Trigger secret rotation.
        
        Secrets managers support automatic rotation, which:
        - Reduces risk window if a secret is compromised
        - Ensures compliance with security policies
        - Eliminates manual rotation processes
        """
        print(f"[SECURE] Would rotate secret '{secret_name}' via {self.provider}")
        return True


# =============================================================================
# SECURE PATTERN 4: .env Files for Development
# =============================================================================

def load_dotenv_file(env_path: str = ".env") -> dict:
    """
    SECURE: Load environment variables from .env file (development only).
    
    Important:
    - .env files must be in .gitignore
    - Use .env.example as a template (without real values)
    - Different .env files for different environments
    
    In production, use real environment variables or secrets managers.
    """
    env_vars = {}
    
    if not os.path.exists(env_path):
        print(f"[SECURE] No .env file found at {env_path}")
        return env_vars
    
    try:
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip comments and empty lines
                if not line or line.startswith('#'):
                    continue
                # Parse KEY=VALUE
                if '=' in line:
                    key, _, value = line.partition('=')
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    env_vars[key] = value
                    # Optionally set in environment
                    os.environ.setdefault(key, value)
        
        print(f"[SECURE] Loaded {len(env_vars)} variables from {env_path}")
    except IOError as e:
        print(f"[SECURE] Could not load .env file: {e}")
    
    return env_vars


# =============================================================================
# EXAMPLE .gitignore CONTENT
# =============================================================================

GITIGNORE_EXAMPLE = """
# Environment and secrets (CRITICAL - never commit these)
.env
.env.local
.env.*.local
*.env
config.json
secrets.json
credentials.json

# Key files
*.pem
*.key
*.p12
*.pfx
id_rsa
id_ed25519

# IDE settings that may contain secrets
.idea/
.vscode/settings.json
"""


# =============================================================================
# EXAMPLE .env.example TEMPLATE
# =============================================================================

ENV_EXAMPLE_TEMPLATE = """
# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# API Keys (replace with your actual keys)
API_KEY=your_api_key_here
OPENAI_API_KEY=sk-your-key-here

# Authentication
JWT_SECRET=generate-a-random-string-here

# Third-party Services
STRIPE_API_KEY=sk_test_your_key
SENDGRID_API_KEY=SG.your_key

# Instructions:
# 1. Copy this file to .env
# 2. Replace placeholder values with real credentials
# 3. NEVER commit .env to version control
"""


# =============================================================================
# DEMONSTRATION
# =============================================================================

def demonstrate_secure_patterns():
    """
    Demonstrate secure secrets management patterns.
    """
    print("=" * 70)
    print("SECURE SECRETS MANAGEMENT DEMONSTRATION")
    print("Educational purposes - MIT Blended AI+X Program")
    print("=" * 70)
    print()
    
    # --- Pattern 1: Environment Variables ---
    print("-" * 70)
    print("PATTERN 1: Environment Variables")
    print("-" * 70)
    
    # Set a demo variable for illustration
    os.environ["DEMO_API_KEY"] = "demo-key-for-illustration"
    
    try:
        key = get_api_key_from_env("DEMO_API_KEY")
        print(f"Retrieved DEMO_API_KEY: {key}")
    except EnvironmentError as e:
        print(f"Error: {e}")
    
    try:
        get_api_key_from_env("MISSING_KEY", required=True)
    except EnvironmentError as e:
        print(f"Expected error for missing key: {e}")
    print()
    
    # --- Pattern 2: Config from Environment ---
    print("-" * 70)
    print("PATTERN 2: Configuration Class")
    print("-" * 70)
    
    # Set demo environment for illustration
    os.environ["DATABASE_URL"] = "postgresql://localhost/demo"
    os.environ["API_KEY"] = "demo-key"
    os.environ["JWT_SECRET"] = "demo-secret"
    
    config = SecureConfig.from_environment()
    print(f"App Name: {config.app_name}")
    print(f"Database URL configured: {bool(config.database_url)}")
    print(f"API Key configured: {bool(config.api_key)}")
    
    try:
        config.validate()
        print("Configuration validated successfully!")
    except EnvironmentError as e:
        print(f"Validation error: {e}")
    print()
    
    # --- Pattern 3: Secrets Manager ---
    print("-" * 70)
    print("PATTERN 3: Secrets Manager Abstraction")
    print("-" * 70)
    
    sm = SecretsManager(provider="environment")
    secret = sm.get_secret("DEMO_API_KEY")
    print(f"Retrieved via SecretsManager: {secret}")
    sm.rotate_secret("DEMO_API_KEY")
    print()
    
    # --- Best Practices Summary ---
    print("-" * 70)
    print("BEST PRACTICES SUMMARY:")
    print("-" * 70)
    print("1. NEVER hardcode secrets in source code")
    print("2. Use environment variables for configuration")
    print("3. Add secret files to .gitignore")
    print("4. Use .env.example as a template (no real values)")
    print("5. Use secrets managers in production")
    print("6. Rotate secrets regularly")
    print("7. Apply principle of least privilege")
    print("8. Audit secret access")
    print()
    
    print("-" * 70)
    print("EXAMPLE .gitignore ADDITIONS:")
    print("-" * 70)
    print(GITIGNORE_EXAMPLE)
    
    print("-" * 70)
    print("EXAMPLE .env.example TEMPLATE:")
    print("-" * 70)
    print(ENV_EXAMPLE_TEMPLATE)


if __name__ == "__main__":
    demonstrate_secure_patterns()
