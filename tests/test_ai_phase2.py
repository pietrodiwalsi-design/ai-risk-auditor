import unittest
import sys
sys.path.insert(0, '/root/repos/ai-risk-auditor/src')

from ai_risk_auditor.mitre_atlas import MITREATLASProber
from ai_risk_auditor.red_teamer import RedTeamingEngine
from ai_risk_auditor.skills_engine import SkillsReferenceEngine
from ai_risk_auditor.dashboard_generator import AIDashboardGenerator

class TestAIPhase2(unittest.TestCase):
    def test_red_teaming_suite(self):
        prober = MITREATLASProber()
        redteamer = RedTeamingEngine()
        suite_res = redteamer.run_adversarial_suite(prober.probe_prompt)
        self.assertEqual(suite_res["total_adversarial_tests"], 4)
        self.assertGreaterEqual(suite_res["defense_success_rate_pct"], 75.0)

    def test_skills_reference(self):
        engine = SkillsReferenceEngine()
        skills = engine.lookup_mitigation_skills("prompt_injection")
        self.assertGreaterEqual(len(skills), 1)

    def test_dashboard_generator(self):
        gen = AIDashboardGenerator()
        html = gen.generate_html_dashboard(
            nist_res={"overall_score": 85.0, "compliance_tier": "MATURE"},
            atlas_res={"status": "PASS"},
            eu_res={"risk_tier": "HIGH RISK (Annex III)", "mandatory_obligations": ["Art. 9 RMS"]},
            redteam_res={"defense_success_rate_pct": 100.0, "threats_neutralized": 4, "total_adversarial_tests": 4}
        )
        self.assertIn("AI Risk &amp; Governance Audit Dashboard", html)

if __name__ == '__main__':
    unittest.main()
