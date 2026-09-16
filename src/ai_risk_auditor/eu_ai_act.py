from typing import Dict, Any

class EUAIActClassifier:
    """Classifies AI systems under Regulation (EU) 2024/1689 (EU AI Act)."""

    PROHIBITED_USE_CASES = ["social_scoring", "biometric_categorization_sensitive", "subliminal_manipulation"]
    HIGH_RISK_DOMAINS = ["life_and_pensions_underwriting", "credit_scoring", "employment_recruitment", "critical_infrastructure"]

    def classify_ai_system(self, domain: str, intended_purpose: str) -> Dict[str, Any]:
        if not isinstance(domain, str) or not domain.strip():
            raise ValueError("domain must be a non-empty string")
        if intended_purpose is not None and not isinstance(intended_purpose, str):
            raise TypeError("intended_purpose must be a string or None")
        domain_clean = domain.strip().lower().replace(" ", "_")
        
        if domain_clean in self.PROHIBITED_USE_CASES:
            risk_tier = "PROHIBITED (Article 5)"
            obligations = ["Complete ban within the European Union"]
        elif domain_clean in self.HIGH_RISK_DOMAINS:
            risk_tier = "HIGH RISK (Annex III / Article 6)"
            obligations = [
                "Risk Management System (Art. 9)",
                "Data Governance & Bias Testing (Art. 10)",
                "Technical Documentation (Art. 11)",
                "Automatic Record-Keeping & Logging (Art. 12)",
                "Human Oversight Measures (Art. 14)",
                "Cybersecurity & Robustness (Art. 15)"
            ]
        else:
            risk_tier = "MINIMAL RISK"
            obligations = ["Voluntary codes of conduct & general transparency"]

        return {
            "regulation": "EU AI Act (Regulation EU 2024/1689)",
            "domain": domain,
            "risk_tier": risk_tier,
            "mandatory_obligations": obligations
        }
