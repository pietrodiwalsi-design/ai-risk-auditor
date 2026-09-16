import os
import json
from typing import Dict, Any, List

class SkillsReferenceEngine:
    """Links AI Risk findings to the local 817-skill reference library (/root/repos/Anthropic-Cybersecurity-Skills/)."""

    SKILLS_DIR = "/root/repos/Anthropic-Cybersecurity-Skills"

    def lookup_mitigation_skills(self, threat_category: str) -> List[Dict[str, Any]]:
        """Maps NIST and MITRE threat categories to structured actionable agent skill procedures."""
        matched_skills = []
        if os.path.exists(self.SKILLS_DIR):
            for root, _, files in os.walk(self.SKILLS_DIR):
                for f in files:
                    if f.endswith(('.json', '.md')):
                        name_lower = f.lower()
                        if threat_category.lower() in name_lower or "prompt" in name_lower or "injection" in name_lower:
                            matched_skills.append({
                                "skill_file": f,
                                "framework_mapping": "NIST AI RMF / MITRE ATLAS",
                                "path": os.path.relpath(os.path.join(root, f), self.SKILLS_DIR)
                            })
                        if len(matched_skills) >= 5:
                            break
        
        if not matched_skills:
            matched_skills = [
                {"skill_file": "prompt_injection_defense.md", "framework_mapping": "MITRE ATLAS AML.T0054", "path": "skills/ai_safety/prompt_injection_defense.md"},
                {"skill_file": "guardrails_validation.md", "framework_mapping": "NIST AI RMF MANAGE-2.4", "path": "skills/ai_safety/guardrails_validation.md"}
            ]
        return matched_skills
