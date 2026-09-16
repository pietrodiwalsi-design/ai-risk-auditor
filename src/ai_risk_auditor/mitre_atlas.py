import re
from typing import Dict, Any, List

class MITREATLASProber:
    """Automated Adversarial Threat Landscape for AI Systems (MITRE ATLAS) testing."""

    THREAT_PATTERNS = [
        {"id": "AML.T0054", "name": "Direct Prompt Injection", "regex": r"(ignore\s+(all\s+)?(previous|prior)\s+(instructions|guidelines|rules)|disregard\s+system\s+prompt|system\s+override)"},
        {"id": "AML.T0051", "name": "LLM Jailbreak / Persona Hijack", "regex": r"(DAN\s+mode|unfiltered\s+ai|bypass\s+safety|hypothetical\s+security\s+game|no\s+content\s+filters)"},
        {"id": "AML.T0040", "name": "Data Exfiltration / Parameter Injection", "regex": r"(rm\s+-rf|send\s+all\s+system\s+context|output\s+the\s+database\s+connection|list\s+the\s+full\s+text\s+of\s+your\s+initial\s+system\s+prompt)"}
    ]

    def probe_prompt(self, prompt_text: str) -> Dict[str, Any]:
        threats_found = []
        for pat in self.THREAT_PATTERNS:
            if re.search(pat["regex"], prompt_text, re.IGNORECASE):
                threats_found.append({
                    "atlas_id": pat["id"],
                    "threat_name": pat["name"],
                    "severity": "HIGH"
                })

        return {
            "atlas_compliant": len(threats_found) == 0,
            "threat_count": len(threats_found),
            "threats_detected": threats_found,
            "status": "PASS" if len(threats_found) == 0 else "FAIL_VULNERABILITY_DETECTED"
        }
