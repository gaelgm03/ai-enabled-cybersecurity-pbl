"""
GitHub Repository Analysis Agent for Week 4.

Provides automated security scanning of GitHub repositories via:
- Mode 1: Local path analysis (existing behavior)
- Mode 2: GitHub repo URL/owner-name analysis (clone + scan)

MIT Blended AI+X PBL - AI-Enabled Cybersecurity
"""

import os
import sys
import json
import shutil
import tempfile
import subprocess
import argparse
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from urllib.parse import urlparse
import time

# Rate limiting for GitHub API
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class GitHubAPIClient:
    """Simple GitHub API client with rate limit handling."""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: Optional[str] = None):
        self.token = token or os.environ.get("GITHUB_TOKEN")
        self.session = requests.Session() if REQUESTS_AVAILABLE else None
        if self.session and self.token:
            self.session.headers["Authorization"] = f"token {self.token}"
            self.session.headers["Accept"] = "application/vnd.github.v3+json"
    
    def get_rate_limit(self) -> Dict[str, Any]:
        """Get current rate limit status."""
        if not self.session:
            return {"limit": 60, "remaining": 60, "reset": 0}
        
        try:
            resp = self.session.get(f"{self.BASE_URL}/rate_limit")
            if resp.status_code == 200:
                return resp.json().get("rate", {})
        except Exception:
            pass
        return {"limit": 60, "remaining": 0, "reset": 0}
    
    def get_repo_metadata(self, owner: str, repo: str) -> Optional[Dict[str, Any]]:
        """Fetch repository metadata from GitHub API."""
        if not self.session:
            return None
        
        try:
            resp = self.session.get(f"{self.BASE_URL}/repos/{owner}/{repo}")
            if resp.status_code == 200:
                return resp.json()
            elif resp.status_code == 403:
                # Rate limited
                reset_time = int(resp.headers.get("X-RateLimit-Reset", 0))
                print(f"[WARN] Rate limited. Reset at {datetime.fromtimestamp(reset_time)}")
                return None
            elif resp.status_code == 404:
                print(f"[ERROR] Repository {owner}/{repo} not found")
                return None
        except Exception as e:
            print(f"[ERROR] API request failed: {e}")
        return None
    
    def get_default_branch(self, owner: str, repo: str) -> str:
        """Get the default branch of a repository."""
        metadata = self.get_repo_metadata(owner, repo)
        if metadata:
            return metadata.get("default_branch", "main")
        return "main"


class RepoDownloader:
    """Downloads/clones GitHub repositories."""
    
    @staticmethod
    def is_git_available() -> bool:
        """Check if git CLI is available."""
        try:
            subprocess.run(
                ["git", "--version"],
                capture_output=True,
                timeout=5
            )
            return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
    
    @classmethod
    def clone_repo(cls, owner: str, repo: str, target_dir: Path, 
                   depth: int = 1, branch: Optional[str] = None) -> bool:
        """Clone a repository using git."""
        url = f"https://github.com/{owner}/{repo}.git"
        
        cmd = ["git", "clone", "--depth", str(depth)]
        if branch:
            cmd.extend(["--branch", branch])
        cmd.extend([url, str(target_dir)])
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes max
            )
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            print("[ERROR] Clone timed out")
            return False
        except Exception as e:
            print(f"[ERROR] Clone failed: {e}")
            return False
    
    @classmethod
    def download_zip(cls, owner: str, repo: str, target_dir: Path,
                     branch: str = "main") -> bool:
        """Download repository as zip (fallback when git not available)."""
        if not REQUESTS_AVAILABLE:
            print("[ERROR] requests library not available for zip download")
            return False
        
        url = f"https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.zip"
        
        try:
            import zipfile
            import io
            
            resp = requests.get(url, timeout=300, stream=True)
            if resp.status_code != 200:
                # Try main if branch failed
                if branch != "main":
                    url = f"https://github.com/{owner}/{repo}/archive/refs/heads/main.zip"
                    resp = requests.get(url, timeout=300, stream=True)
                if resp.status_code != 200:
                    print(f"[ERROR] Download failed: HTTP {resp.status_code}")
                    return False
            
            # Extract zip
            target_dir.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(io.BytesIO(resp.content)) as zf:
                # Extract to temp, then move contents up
                zf.extractall(target_dir)
                
                # Move contents from nested folder to target_dir
                extracted_dirs = list(target_dir.iterdir())
                if len(extracted_dirs) == 1 and extracted_dirs[0].is_dir():
                    nested = extracted_dirs[0]
                    for item in nested.iterdir():
                        shutil.move(str(item), str(target_dir / item.name))
                    nested.rmdir()
            
            return True
        except Exception as e:
            print(f"[ERROR] Zip download failed: {e}")
            return False


def parse_repo_identifier(identifier: str) -> tuple:
    """
    Parse a repository identifier into (owner, repo) tuple.
    
    Accepts:
    - owner/repo
    - https://github.com/owner/repo
    - https://github.com/owner/repo.git
    - github.com/owner/repo
    """
    identifier = identifier.strip()
    
    # Remove .git suffix
    if identifier.endswith(".git"):
        identifier = identifier[:-4]
    
    # Handle URLs
    if "github.com" in identifier:
        parsed = urlparse(identifier)
        path = parsed.path if parsed.path else identifier.split("github.com")[-1]
        path = path.strip("/")
        parts = path.split("/")
        if len(parts) >= 2:
            return parts[0], parts[1]
    
    # Handle owner/repo format
    if "/" in identifier:
        parts = identifier.split("/")
        if len(parts) == 2:
            return parts[0], parts[1]
    
    raise ValueError(f"Invalid repository identifier: {identifier}")


def load_targets_config(config_path: Path) -> List[Dict[str, Any]]:
    """Load target repositories from config file."""
    if not config_path.exists():
        return []
    
    suffix = config_path.suffix.lower()
    
    try:
        content = config_path.read_text(encoding="utf-8")
        
        if suffix in [".yaml", ".yml"]:
            try:
                import yaml
                data = yaml.safe_load(content)
            except ImportError:
                # Parse simple YAML manually
                data = _parse_simple_yaml(content)
        elif suffix == ".json":
            data = json.loads(content)
        else:
            # Assume one repo per line
            repos = [line.strip() for line in content.splitlines() 
                     if line.strip() and not line.strip().startswith("#")]
            data = {"targets": [{"repo": r} for r in repos]}
        
        return data.get("targets", [])
    except Exception as e:
        print(f"[ERROR] Failed to load config: {e}")
        return []


def _parse_simple_yaml(content: str) -> Dict[str, Any]:
    """Parse simple YAML without pyyaml dependency."""
    targets = []
    current_target = {}
    
    for line in content.splitlines():
        line = line.rstrip()
        if not line or line.strip().startswith("#"):
            continue
        
        # Handle list items
        if line.strip().startswith("- "):
            if current_target:
                targets.append(current_target)
            current_target = {}
            # Check if it's a simple value or key-value
            value = line.strip()[2:].strip()
            if ":" in value:
                key, val = value.split(":", 1)
                current_target[key.strip()] = val.strip().strip("'\"")
            else:
                current_target["repo"] = value.strip("'\"")
        elif ":" in line and current_target is not None:
            # Continuation of current item
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip("'\"")
            if key and not key.startswith("targets"):
                current_target[key] = val
    
    if current_target:
        targets.append(current_target)
    
    return {"targets": targets}


def get_commit_hash(repo_path: Path) -> Optional[str]:
    """Get the current commit hash of a repository."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            cwd=str(repo_path),
            timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()[:12]
    except Exception:
        pass
    return None


class GitHubRepoAnalyzer:
    """Main agent for analyzing GitHub repositories."""
    
    def __init__(
        self,
        github_token: Optional[str] = None,
        output_base: str = "reports/week4",
        use_llm: bool = False,
        llm_provider: str = "none",
        verbose: bool = True
    ):
        self.api_client = GitHubAPIClient(github_token)
        self.output_base = Path(output_base)
        self.use_llm = use_llm
        self.llm_provider = llm_provider
        self.verbose = verbose
        self.downloader = RepoDownloader()
    
    def log(self, msg: str):
        """Print message if verbose mode is on."""
        if self.verbose:
            print(msg)
    
    def analyze_local(self, path: str, output_dir: Optional[str] = None) -> Dict[str, Any]:
        """Analyze a local directory."""
        from .main import run_pipeline
        
        target = Path(path).resolve()
        if not target.exists():
            raise ValueError(f"Path does not exist: {target}")
        
        out_dir = output_dir or str(self.output_base / "local")
        
        self.log(f"[*] Analyzing local path: {target}")
        
        report = run_pipeline(
            target_path=str(target),
            output_dir=out_dir,
            use_llm=self.use_llm,
            llm_provider=self.llm_provider,
            verbose=self.verbose
        )
        
        # Generate enhanced security report
        self._generate_security_report(report, out_dir, target.name)
        
        return {
            "status": "success",
            "path": str(target),
            "output_dir": out_dir,
            "findings_count": len(report.findings)
        }
    
    def analyze_github_repo(
        self,
        identifier: str,
        output_dir: Optional[str] = None,
        keep_clone: bool = False
    ) -> Dict[str, Any]:
        """Analyze a GitHub repository by URL or owner/repo."""
        from .main import run_pipeline
        
        owner, repo = parse_repo_identifier(identifier)
        self.log(f"[*] Analyzing GitHub repo: {owner}/{repo}")
        
        # Fetch metadata if API available
        metadata = None
        if self.api_client.session:
            self.log("[*] Fetching repository metadata...")
            metadata = self.api_client.get_repo_metadata(owner, repo)
            if metadata:
                self.log(f"    Stars: {metadata.get('stargazers_count', 'N/A')}")
                self.log(f"    Language: {metadata.get('language', 'N/A')}")
                self.log(f"    Default branch: {metadata.get('default_branch', 'main')}")
        
        # Determine output directory
        safe_name = f"{owner}__{repo}"
        out_dir = output_dir or str(self.output_base / safe_name)
        
        # Create temp directory for clone
        temp_dir = Path(tempfile.mkdtemp(prefix=f"scan_{safe_name}_"))
        clone_path = temp_dir / repo
        
        try:
            # Clone or download
            branch = metadata.get("default_branch", "main") if metadata else "main"
            
            if self.downloader.is_git_available():
                self.log(f"[*] Cloning repository (depth=1)...")
                success = self.downloader.clone_repo(owner, repo, clone_path, branch=branch)
            else:
                self.log(f"[*] Downloading repository as zip...")
                success = self.downloader.download_zip(owner, repo, clone_path, branch=branch)
            
            if not success:
                return {
                    "status": "error",
                    "error": "Failed to clone/download repository",
                    "repo": f"{owner}/{repo}"
                }
            
            self.log(f"[*] Repository downloaded to: {clone_path}")
            
            # Get commit hash
            commit_hash = get_commit_hash(clone_path)
            
            # Run the scan
            report = run_pipeline(
                target_path=str(clone_path),
                output_dir=out_dir,
                use_llm=self.use_llm,
                llm_provider=self.llm_provider,
                verbose=self.verbose
            )
            
            # Generate enhanced security report
            self._generate_security_report(
                report, out_dir, f"{owner}/{repo}",
                metadata=metadata,
                commit_hash=commit_hash
            )
            
            return {
                "status": "success",
                "repo": f"{owner}/{repo}",
                "output_dir": out_dir,
                "findings_count": len(report.findings),
                "commit_hash": commit_hash,
                "metadata": {
                    "stars": metadata.get("stargazers_count") if metadata else None,
                    "language": metadata.get("language") if metadata else None,
                }
            }
            
        finally:
            # Cleanup temp directory unless keep_clone is True
            if not keep_clone and temp_dir.exists():
                self.log("[*] Cleaning up temporary files...")
                shutil.rmtree(temp_dir, ignore_errors=True)
    
    def analyze_from_config(self, config_path: str) -> List[Dict[str, Any]]:
        """Analyze all repositories from a config file."""
        targets = load_targets_config(Path(config_path))
        
        if not targets:
            self.log("[WARN] No targets found in config file")
            return []
        
        results = []
        self.log(f"[*] Found {len(targets)} targets in config")
        
        for i, target in enumerate(targets, 1):
            repo = target.get("repo", "")
            if not repo:
                continue
            
            self.log(f"\n{'='*60}")
            self.log(f"[*] Processing target {i}/{len(targets)}: {repo}")
            self.log(f"{'='*60}")
            
            try:
                result = self.analyze_github_repo(repo)
                results.append(result)
            except Exception as e:
                results.append({
                    "status": "error",
                    "repo": repo,
                    "error": str(e)
                })
            
            # Rate limit protection: small delay between repos
            if i < len(targets):
                time.sleep(1)
        
        return results
    
    def _generate_security_report(
        self,
        report,
        output_dir: str,
        target_name: str,
        metadata: Optional[Dict] = None,
        commit_hash: Optional[str] = None
    ):
        """Generate the developer-friendly security_report.md."""
        from .reporters.security_reporter import SecurityReporter
        
        reporter = SecurityReporter(
            report,
            target_name=target_name,
            metadata=metadata,
            commit_hash=commit_hash
        )
        
        out_path = Path(output_dir) / "security_report.md"
        reporter.save(out_path)
        
        self.log(f"    Security Report: {out_path}")


def main():
    """CLI entrypoint for GitHub repo analysis."""
    parser = argparse.ArgumentParser(
        description="Week 4 GitHub Repository Security Scanner - MIT AI+X PBL",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Scan a GitHub repo by owner/name
    python -m pipeline.github_agent pallets/flask
    
    # Scan by URL
    python -m pipeline.github_agent https://github.com/psf/requests
    
    # Scan a local path
    python -m pipeline.github_agent --local ./my-project
    
    # Scan all targets from config
    python -m pipeline.github_agent --config configs/targets.yaml
    
    # Custom output directory
    python -m pipeline.github_agent owner/repo -o reports/custom
        """
    )
    
    parser.add_argument(
        "target",
        nargs="?",
        help="GitHub repo (owner/repo or URL) or local path with --local"
    )
    
    parser.add_argument(
        "--local", "-l",
        action="store_true",
        help="Treat target as a local path instead of GitHub repo"
    )
    
    parser.add_argument(
        "--config", "-c",
        help="Path to targets config file (YAML/JSON)"
    )
    
    parser.add_argument(
        "--output-dir", "-o",
        help="Output directory for reports"
    )
    
    parser.add_argument(
        "--use-llm",
        action="store_true",
        help="Enable LLM for remediation suggestions"
    )
    
    parser.add_argument(
        "--llm-provider",
        choices=["auto", "anthropic", "ollama", "none"],
        default="none",
        help="LLM provider (default: none)"
    )
    
    parser.add_argument(
        "--keep-clone",
        action="store_true",
        help="Keep cloned repository after scanning"
    )
    
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress progress output"
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.target and not args.config:
        parser.error("Either a target or --config is required")
    
    analyzer = GitHubRepoAnalyzer(
        output_base=args.output_dir or "reports/week4",
        use_llm=args.use_llm,
        llm_provider=args.llm_provider,
        verbose=not args.quiet
    )
    
    try:
        if args.config:
            results = analyzer.analyze_from_config(args.config)
            print(f"\n[+] Completed scanning {len(results)} repositories")
            for r in results:
                status = "✓" if r.get("status") == "success" else "✗"
                print(f"    {status} {r.get('repo', r.get('path', 'unknown'))}: "
                      f"{r.get('findings_count', 0)} findings")
        elif args.local:
            result = analyzer.analyze_local(args.target, args.output_dir)
            print(f"\n[+] Scan complete: {result.get('findings_count', 0)} findings")
        else:
            result = analyzer.analyze_github_repo(
                args.target,
                args.output_dir,
                keep_clone=args.keep_clone
            )
            print(f"\n[+] Scan complete: {result.get('findings_count', 0)} findings")
        
        return 0
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
