"""
Main evaluation harness for Week 5.

Usage:
    python -m evals.run_eval --dataset evals/datasets/week5_cases.jsonl --models baseline,ollama:llama3.1:8b --out reports/week5

MIT Blended AI+X PBL - AI-Enabled Cybersecurity
"""

import argparse
import json
import time
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime, timezone

from .metrics import ModelMetrics, compute_comparison
from .model_adapters import BaselineAdapter, OllamaAdapter, AnthropicAdapter


def load_dataset(dataset_path: str) -> List[dict]:
    """Load evaluation dataset from JSONL file."""
    cases = []
    path = Path(dataset_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            try:
                case = json.loads(line)
                cases.append(case)
            except json.JSONDecodeError as e:
                print(f"[WARN] Invalid JSON on line {line_num}: {e}")
    
    return cases


def get_adapter(model_spec: str, api_key: Optional[str] = None):
    """Create adapter from model specification string."""
    if model_spec == "baseline":
        return BaselineAdapter()
    elif model_spec.startswith("ollama:"):
        model_name = model_spec.split(":", 1)[1]
        return OllamaAdapter(model=model_name)
    elif model_spec.startswith("anthropic"):
        if ":" in model_spec:
            model_name = model_spec.split(":", 1)[1]
            return AnthropicAdapter(api_key=api_key, model=model_name)
        return AnthropicAdapter(api_key=api_key)
    else:
        raise ValueError(f"Unknown model spec: {model_spec}")


def run_evaluation(
    cases: List[dict],
    adapters: List,
    verbose: bool = True
) -> Dict[str, ModelMetrics]:
    """Run evaluation across all models and cases."""
    results = {}
    
    for adapter in adapters:
        model_name = adapter.name
        
        if not adapter.is_available():
            if verbose:
                print(f"[SKIP] {model_name} - not available")
            continue
        
        if verbose:
            print(f"\n[*] Evaluating: {model_name}")
        
        metrics = ModelMetrics(model_name=model_name)
        
        for i, case in enumerate(cases):
            case_id = case.get("id", f"case-{i}")
            category = case.get("category", "unknown")
            label = case.get("label", "unknown")
            language = case.get("language", "python")
            snippet = case.get("snippet", "")
            
            ground_truth = label == "vulnerable"
            
            start_time = time.perf_counter()
            result = adapter.classify(snippet, category, language)
            elapsed_ms = (time.perf_counter() - start_time) * 1000
            
            metrics.add_result(
                case_id=case_id,
                category=category,
                ground_truth=ground_truth,
                prediction=result.is_vulnerable,
                latency_ms=elapsed_ms,
                rationale=result.rationale
            )
            
            if verbose:
                status = "✓" if ground_truth == result.is_vulnerable else "✗"
                print(f"  [{status}] {case_id}: pred={result.is_vulnerable}, truth={ground_truth}")
        
        results[model_name] = metrics
        
        if verbose:
            overall = metrics.overall_metrics
            print(f"  Summary: P={overall.precision:.2f} R={overall.recall:.2f} F1={overall.f1:.2f}")
    
    return results


def generate_json_report(results: Dict[str, ModelMetrics], comparison: dict) -> dict:
    """Generate JSON report structure."""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "summary": comparison,
        "models": {name: metrics.to_dict() for name, metrics in results.items()},
    }


def generate_markdown_report(results: Dict[str, ModelMetrics], comparison: dict) -> str:
    """Generate Markdown report."""
    lines = [
        "# Week 5 Evaluation Results",
        "",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
        "",
        "---",
        "",
        "## Overall Comparison",
        "",
        "| Model | Precision | Recall | F1 | FPR | Accuracy | Avg Latency |",
        "|-------|-----------|--------|-----|-----|----------|-------------|",
    ]
    
    for row in comparison.get("overall_comparison", []):
        lines.append(
            f"| {row['model']} | {row['precision']:.4f} | {row['recall']:.4f} | "
            f"{row['f1']:.4f} | {row['fpr']:.4f} | {row['accuracy']:.4f} | {row['avg_latency_ms']:.0f}ms |"
        )
    
    lines.extend([
        "",
        "### Best Models",
        "",
        f"- **Best F1:** {comparison['best_model']['by_f1']}",
        f"- **Best Precision:** {comparison['best_model']['by_precision']}",
        f"- **Best Recall:** {comparison['best_model']['by_recall']}",
        f"- **Lowest FPR:** {comparison['best_model']['by_fpr']}",
        "",
        "---",
        "",
        "## Per-Category Results",
        "",
    ])
    
    for cat, cat_results in comparison.get("category_comparison", {}).items():
        lines.extend([
            f"### {cat.upper()}",
            "",
            "| Model | Precision | Recall | F1 | FPR |",
            "|-------|-----------|--------|-----|-----|",
        ])
        for row in cat_results:
            lines.append(
                f"| {row['model']} | {row['precision']:.4f} | {row['recall']:.4f} | "
                f"{row['f1']:.4f} | {row['fpr']:.4f} |"
            )
        lines.append("")
    
    lines.extend([
        "---",
        "",
        "## Analysis",
        "",
        "### Where AI Helps",
        "",
        "- **False positive reduction:** AI models can distinguish between real vulnerabilities and benign patterns",
        "- **Context awareness:** AI understands that placeholder values like `YOUR_API_KEY` are not real secrets",
        "- **Semantic understanding:** AI can identify that variable names like `teh` are intentional identifiers",
        "",
        "### Where AI May Fail",
        "",
        "- **Inconsistent responses:** Same input may get different classifications across runs",
        "- **Hallucination risk:** AI may invent rationales not supported by the code",
        "- **Latency cost:** AI classification is significantly slower than regex matching",
        "",
        "### Methodology Notes",
        "",
        "- **Ground truth:** Manually labeled dataset with clear vulnerable/safe examples",
        "- **Metrics:** Standard precision, recall, F1 computed per category",
        "- **Limitations:** Small dataset (N<100); results are directional, not statistically significant",
        "",
        "---",
        "",
        "*Generated by Week 5 Evaluation Harness*",
    ])
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Run Week 5 evaluation harness")
    parser.add_argument(
        "--dataset",
        default="evals/datasets/week5_cases.jsonl",
        help="Path to evaluation dataset (JSONL)"
    )
    parser.add_argument(
        "--models",
        default="baseline,ollama:llama3.1:8b",
        help="Comma-separated model specs (e.g., baseline,ollama:llama3.1:8b,anthropic)"
    )
    parser.add_argument(
        "--out",
        default="reports/week5",
        help="Output directory for results"
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="Anthropic API key (or use ANTHROPIC_API_KEY env var)"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress verbose output"
    )
    
    args = parser.parse_args()
    verbose = not args.quiet
    
    if verbose:
        print("=" * 60)
        print("Week 5 Evaluation Harness")
        print("MIT Blended AI+X PBL - AI-Enabled Cybersecurity")
        print("=" * 60)
    
    cases = load_dataset(args.dataset)
    if verbose:
        print(f"\n[*] Loaded {len(cases)} test cases from {args.dataset}")
    
    model_specs = [m.strip() for m in args.models.split(",")]
    adapters = [get_adapter(spec, args.api_key) for spec in model_specs]
    
    if verbose:
        print(f"[*] Models to evaluate: {[a.name for a in adapters]}")
    
    results = run_evaluation(cases, adapters, verbose=verbose)
    
    if not results:
        print("\n[ERROR] No models were evaluated successfully")
        return 1
    
    comparison = compute_comparison(results)
    
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    json_report = generate_json_report(results, comparison)
    json_path = out_dir / "eval_results.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_report, f, indent=2)
    
    md_report = generate_markdown_report(results, comparison)
    md_path = out_dir / "eval_results.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_report)
    
    if verbose:
        print(f"\n[*] Results saved to:")
        print(f"    JSON: {json_path}")
        print(f"    Markdown: {md_path}")
        print("\n" + "=" * 60)
        print("Evaluation complete!")
        print("=" * 60)
    
    return 0


if __name__ == "__main__":
    exit(main())
