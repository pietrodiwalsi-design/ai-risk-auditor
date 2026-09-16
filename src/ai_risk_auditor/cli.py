import sys
import json
import argparse
from ai_risk_auditor.nist_rmf import NISTAIRMFAuditor
from ai_risk_auditor.mitre_atlas import MITREATLASProber
from ai_risk_auditor.eu_ai_act import EUAIActClassifier
from ai_risk_auditor.report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="AI Risk Auditor CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Classify EU AI Act
    eu_p = subparsers.add_parser("classify", help="Classify AI system under EU AI Act")
    eu_p.add_argument("--domain", required=True, help="Domain (e.g. life_and_pensions_underwriting)")
    eu_p.add_argument("--purpose", default="", help="Intended purpose")

    # Probe ATLAS
    atlas_p = subparsers.add_parser("probe-prompt", help="Test prompt against MITRE ATLAS threat patterns")
    atlas_p.add_argument("--prompt", required=True, help="Prompt text to test")

    args = parser.parse_args()

    if args.command == "classify":
        classifier = EUAIActClassifier()
        res = classifier.classify_ai_system(args.domain, args.purpose)
        print(json.dumps(res, indent=2))
    elif args.command == "probe-prompt":
        prober = MITREATLASProber()
        res = prober.probe_prompt(args.prompt)
        print(json.dumps(res, indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
