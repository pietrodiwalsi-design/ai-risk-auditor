from typing import Dict, Any, List

class NISTAIRMFAuditor:
    """Evaluates AI/LLM systems against NIST AI RMF 1.0 (Govern, Map, Measure, Manage)."""

    FUNCTIONS = ["GOVERN", "MAP", "MEASURE", "MANAGE"]

    def evaluate_system(self, system_profile: Dict[str, Any]) -> Dict[str, Any]:
        has_human_oversight = system_profile.get("human_oversight", False)
        has_eval_metrics = system_profile.get("eval_metrics_defined", False)
        has_incident_plan = system_profile.get("incident_response_plan", False)
        has_data_provenance = system_profile.get("data_provenance_logged", False)

        scores = {
            "GOVERN": 85 if has_human_oversight else 40,
            "MAP": 80 if has_data_provenance else 45,
            "MEASURE": 90 if has_eval_metrics else 35,
            "MANAGE": 85 if has_incident_plan else 50
        }

        overall_score = round(sum(scores.values()) / len(scores), 1)
        compliance_tier = "MATURE" if overall_score >= 80 else "INTERMEDIATE" if overall_score >= 60 else "BASIC"

        return {
            "framework": "NIST AI RMF 1.0",
            "overall_score": overall_score,
            "compliance_tier": compliance_tier,
            "function_breakdown": scores,
            "gap_areas": [f for f, s in scores.items() if s < 70]
        }
