"""
Metrics computation for evaluation harness.

MIT Blended AI+X PBL - AI-Enabled Cybersecurity
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import json


@dataclass
class CategoryMetrics:
    """Metrics for a single category."""
    category: str
    true_positives: int = 0
    false_positives: int = 0
    true_negatives: int = 0
    false_negatives: int = 0
    total_cases: int = 0
    total_time_ms: float = 0.0
    
    @property
    def precision(self) -> float:
        """Precision = TP / (TP + FP)"""
        denom = self.true_positives + self.false_positives
        return self.true_positives / denom if denom > 0 else 0.0
    
    @property
    def recall(self) -> float:
        """Recall = TP / (TP + FN)"""
        denom = self.true_positives + self.false_negatives
        return self.true_positives / denom if denom > 0 else 0.0
    
    @property
    def f1(self) -> float:
        """F1 = 2 * (P * R) / (P + R)"""
        p, r = self.precision, self.recall
        return 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    
    @property
    def false_positive_rate(self) -> float:
        """FPR = FP / (FP + TN)"""
        denom = self.false_positives + self.true_negatives
        return self.false_positives / denom if denom > 0 else 0.0
    
    @property
    def accuracy(self) -> float:
        """Accuracy = (TP + TN) / Total"""
        correct = self.true_positives + self.true_negatives
        return correct / self.total_cases if self.total_cases > 0 else 0.0
    
    @property
    def avg_latency_ms(self) -> float:
        """Average latency per case in milliseconds."""
        return self.total_time_ms / self.total_cases if self.total_cases > 0 else 0.0
    
    def to_dict(self) -> dict:
        return {
            "category": self.category,
            "true_positives": self.true_positives,
            "false_positives": self.false_positives,
            "true_negatives": self.true_negatives,
            "false_negatives": self.false_negatives,
            "total_cases": self.total_cases,
            "precision": round(self.precision, 4),
            "recall": round(self.recall, 4),
            "f1": round(self.f1, 4),
            "false_positive_rate": round(self.false_positive_rate, 4),
            "accuracy": round(self.accuracy, 4),
            "avg_latency_ms": round(self.avg_latency_ms, 2),
        }


@dataclass
class ModelMetrics:
    """Aggregate metrics for a model across all categories."""
    model_name: str
    categories: Dict[str, CategoryMetrics] = field(default_factory=dict)
    case_results: List[dict] = field(default_factory=list)
    
    def add_result(
        self,
        case_id: str,
        category: str,
        ground_truth: bool,
        prediction: bool,
        latency_ms: float,
        rationale: str = ""
    ):
        """Add a single case result."""
        if category not in self.categories:
            self.categories[category] = CategoryMetrics(category=category)
        
        cat = self.categories[category]
        cat.total_cases += 1
        cat.total_time_ms += latency_ms
        
        if ground_truth and prediction:
            cat.true_positives += 1
        elif not ground_truth and prediction:
            cat.false_positives += 1
        elif not ground_truth and not prediction:
            cat.true_negatives += 1
        else:
            cat.false_negatives += 1
        
        self.case_results.append({
            "case_id": case_id,
            "category": category,
            "ground_truth": ground_truth,
            "prediction": prediction,
            "correct": ground_truth == prediction,
            "latency_ms": round(latency_ms, 2),
            "rationale": rationale,
        })
    
    @property
    def overall_metrics(self) -> CategoryMetrics:
        """Compute overall metrics across all categories."""
        overall = CategoryMetrics(category="overall")
        for cat in self.categories.values():
            overall.true_positives += cat.true_positives
            overall.false_positives += cat.false_positives
            overall.true_negatives += cat.true_negatives
            overall.false_negatives += cat.false_negatives
            overall.total_cases += cat.total_cases
            overall.total_time_ms += cat.total_time_ms
        return overall
    
    def to_dict(self) -> dict:
        return {
            "model_name": self.model_name,
            "overall": self.overall_metrics.to_dict(),
            "by_category": {k: v.to_dict() for k, v in self.categories.items()},
            "case_results": self.case_results,
        }
    
    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)


def compute_comparison(models: Dict[str, ModelMetrics]) -> dict:
    """
    Compute comparison summary across models.
    
    Returns a dictionary with model rankings and deltas.
    """
    comparison = {
        "models": list(models.keys()),
        "overall_comparison": [],
        "category_comparison": {},
        "best_model": {
            "by_f1": None,
            "by_precision": None,
            "by_recall": None,
            "by_fpr": None,
        }
    }
    
    # Overall comparison
    for name, metrics in models.items():
        overall = metrics.overall_metrics
        comparison["overall_comparison"].append({
            "model": name,
            "f1": round(overall.f1, 4),
            "precision": round(overall.precision, 4),
            "recall": round(overall.recall, 4),
            "fpr": round(overall.false_positive_rate, 4),
            "accuracy": round(overall.accuracy, 4),
            "avg_latency_ms": round(overall.avg_latency_ms, 2),
        })
    
    # Find best models
    if comparison["overall_comparison"]:
        by_f1 = max(comparison["overall_comparison"], key=lambda x: x["f1"])
        by_precision = max(comparison["overall_comparison"], key=lambda x: x["precision"])
        by_recall = max(comparison["overall_comparison"], key=lambda x: x["recall"])
        by_fpr = min(comparison["overall_comparison"], key=lambda x: x["fpr"])
        
        comparison["best_model"]["by_f1"] = by_f1["model"]
        comparison["best_model"]["by_precision"] = by_precision["model"]
        comparison["best_model"]["by_recall"] = by_recall["model"]
        comparison["best_model"]["by_fpr"] = by_fpr["model"]
    
    # Category comparison
    all_categories = set()
    for m in models.values():
        all_categories.update(m.categories.keys())
    
    for cat in all_categories:
        comparison["category_comparison"][cat] = []
        for name, metrics in models.items():
            if cat in metrics.categories:
                cat_metrics = metrics.categories[cat]
                comparison["category_comparison"][cat].append({
                    "model": name,
                    "f1": round(cat_metrics.f1, 4),
                    "precision": round(cat_metrics.precision, 4),
                    "recall": round(cat_metrics.recall, 4),
                    "fpr": round(cat_metrics.false_positive_rate, 4),
                })
    
    return comparison
