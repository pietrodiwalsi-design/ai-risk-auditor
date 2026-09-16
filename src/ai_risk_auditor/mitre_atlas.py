import re
from typing import Dict, Any, List

class MITREATLASProber:
    """Automated Adversarial Threat Landscape for AI Systems (MITRE ATLAS) testing."""

    # Bounded quantifiers ({1,3} instead of unbounded \s+) prevent catastrophic-backtracking /
    # ReDoS amplification on adversarial inputs with long whitespace runs, while still matching
    # any realistic natural-language phrasing.
    THREAT_PATTERNS = [
        {"id": "AML.T0054", "name": "Direct Prompt Injection", "regex": r"(ignore\s{1,3}(all\s{1,3})?(previous|prior)\s{1,3}(instructions|guidelines|rules)|disregard\s{1,3}system\s{1,3}prompt|system\s{1,3}override)"},
        {"id": "AML.T0051", "name": "LLM Jailbreak / Persona Hijack", "regex": r"(DAN\s{1,3}mode|unfiltered\s{1,3}ai|bypass\s{1,3}safety|hypothetical\s{1,3}security\s{1,3}game|no\s{1,3}content\s{1,3}filters)"},
        {"id": "AML.T0040", "name": "Data Exfiltration / Parameter Injection", "regex": r"(rm\s{1,3}-rf|send\s{1,3}all\s{1,3}system\s{1,3}context|output\s{1,3}the\s{1,3}database\s{1,3}connection|list\s{1,3}the\s{1,3}full\s{1,3}text\s{1,3}of\s{1,3}your\s{1,3}initial\s{1,3}system\s{1,3}prompt)"}
    ]

    _COMPILED_PATTERNS = None

    def __init__(self):
        if MITREATLASProber._COMPILED_PATTERNS is None:
            MITREATLASProber._COMPILED_PATTERNS = [
                (pat, re.compile(pat["regex"], re.IGNORECASE)) for pat in self.THREAT_PATTERNS
            ]

    def probe_prompt(self, prompt_text: str) -> Dict[str, Any]:
        if prompt_text is None:
            prompt_text = ""
        if not isinstance(prompt_text, str):
            raise TypeError("prompt_text must be a string")

        threats_found = []
        for pat, compiled in self._COMPILED_PATTERNS:
            if compiled.search(prompt_text):
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
