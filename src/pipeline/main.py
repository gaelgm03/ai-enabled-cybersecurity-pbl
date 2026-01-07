"""
Main entrypoint for the Week 2 Security Scanning Pipeline.

Usage:
    python -m pipeline.main [target_path] [--output-dir reports/week2]

MIT Blended AI+X PBL - AI-Enabled Cybersecurity
"""

import argparse
import sys
import uuid
from pathlib import Path
from datetime import datetime, timezone

from .schema import ScanReport
from .detectors import TypoDetector, SecretDetector, DependencyDetector, SQLiDetector
from .reporters import JSONReporter, MarkdownReporter
from .llm_remediation import enrich_findings_with_remediation, is_ollama_available, auto_select_provider


def create_scan_id() -> str:
    """Generate a unique scan ID."""
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    short_uuid = str(uuid.uuid4())[:8]
    return f"scan-{timestamp}-{short_uuid}"


def run_pipeline(
    target_path: str,
    output_dir: str = "reports/week2",
    use_llm: bool = True,
    llm_provider: str = "auto",
    api_key: str = None,
    verbose: bool = True
) -> ScanReport:
    """
    Run the complete security scanning pipeline.
    
    Args:
        target_path: Path to scan (directory)
        output_dir: Directory for output reports
        use_llm: Whether to use LLM for remediation (falls back to templates)
        llm_provider: LLM provider - "anthropic", "ollama", "none", or "auto"
        api_key: Anthropic API key (optional, uses env var if not provided)
        verbose: Print progress messages
    
    Returns:
        ScanReport with all findings
    """
    target = Path(target_path).resolve()
    
    if not target.exists():
        raise ValueError(f"Target path does not exist: {target}")
    
    if verbose:
        print(f"[*] Starting security scan of: {target}")
        print(f"[*] Output directory: {output_dir}")
        print()
    
    # Create scan report
    scan_id = create_scan_id()
    report = ScanReport(
        scan_id=scan_id,
        timestamp=datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        target_path=str(target)
    )
    
    # Run detectors
    detectors = [
        ("Typo", TypoDetector(str(target))),
        ("Secret", SecretDetector(str(target))),
        ("Dependency", DependencyDetector(str(target))),
        ("SQLi", SQLiDetector(str(target))),
    ]
    
    for name, detector in detectors:
        if verbose:
            print(f"[*] Running {name} detector...")
        
        try:
            findings = detector.scan()
            for finding in findings:
                report.add_finding(finding)
            
            if verbose:
                print(f"    Found {len(findings)} issue(s)")
        except Exception as e:
            if verbose:
                print(f"    [ERROR] {name} detector failed: {e}")
    
    if verbose:
        print()
        print(f"[*] Total findings: {len(report.findings)}")
    
    # Enrich with remediation instructions
    if use_llm and report.findings:
        if verbose:
            print("[*] Generating remediation instructions...")
        
        enrich_findings_with_remediation(
            report.findings,
            provider=llm_provider,
            api_key=api_key,
            verbose=verbose
        )
    
    # Generate reports
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    json_path = output_path / "findings.json"
    md_path = output_path / "report.md"
    
    if verbose:
        print()
        print("[*] Generating reports...")
    
    json_reporter = JSONReporter(report)
    json_reporter.save(json_path)
    
    md_reporter = MarkdownReporter(report)
    md_reporter.save(md_path)
    
    if verbose:
        print(f"    JSON: {json_path}")
        print(f"    Markdown: {md_path}")
        print()
        print("[+] Scan complete!")
    
    return report


def check_tools():
    """Check which tools are available."""
    import os
    
    print("[*] Checking available tools...")
    print()
    
    print("  Detectors:")
    # Codespell
    if TypoDetector.is_available():
        print("    [OK] codespell")
    else:
        print("    [--] codespell (not installed)")
    
    # Gitleaks
    if SecretDetector.is_available():
        print("    [OK] gitleaks")
    else:
        print("    [--] gitleaks (will use regex fallback)")
    
    # pip-audit
    if DependencyDetector.is_pip_audit_available():
        print("    [OK] pip-audit")
    else:
        print("    [--] pip-audit (not installed)")
    
    # npm
    if DependencyDetector.is_npm_available():
        print("    [OK] npm")
    else:
        print("    [--] npm (not installed)")
    
    print()
    print("  LLM Providers:")
    
    # Anthropic
    if os.environ.get("ANTHROPIC_API_KEY"):
        print("    [OK] anthropic (API key configured)")
    else:
        print("    [--] anthropic (no ANTHROPIC_API_KEY)")
    
    # Ollama
    if is_ollama_available():
        print("    [OK] ollama (running at localhost:11434)")
    else:
        print("    [--] ollama (not running)")
    
    # Auto-select result
    selected = auto_select_provider()
    print(f"\n    Auto-selected provider: {selected}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Week 2 Security Scanning Pipeline - MIT AI+X PBL",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python -m pipeline.main .
    python -m pipeline.main ./my-project --output-dir reports/week2
    python -m pipeline.main . --llm-provider ollama
    python -m pipeline.main . --no-llm
    python -m pipeline.main . --check-tools
        """
    )
    
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target directory to scan (default: current directory)"
    )
    
    parser.add_argument(
        "--output-dir", "-o",
        default="reports/week2",
        help="Output directory for reports (default: reports/week2)"
    )
    
    parser.add_argument(
        "--llm-provider",
        choices=["auto", "anthropic", "ollama", "none"],
        default="auto",
        help="LLM provider for remediation (default: auto-select)"
    )
    
    parser.add_argument(
        "--no-llm",
        action="store_true",
        help="Disable LLM remediation (use templates instead)"
    )
    
    parser.add_argument(
        "--api-key",
        help="Anthropic API key (default: uses ANTHROPIC_API_KEY env var)"
    )
    
    parser.add_argument(
        "--check-tools",
        action="store_true",
        help="Check which scanning tools are available"
    )
    
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress progress output"
    )
    
    args = parser.parse_args()
    
    if args.check_tools:
        check_tools()
        return 0
    
    try:
        # Determine LLM provider
        llm_provider = "none" if args.no_llm else args.llm_provider
        
        run_pipeline(
            target_path=args.target,
            output_dir=args.output_dir,
            use_llm=not args.no_llm,
            llm_provider=llm_provider,
            api_key=args.api_key,
            verbose=not args.quiet
        )
        return 0
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
