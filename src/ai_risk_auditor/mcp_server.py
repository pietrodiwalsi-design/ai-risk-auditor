#!/usr/bin/env python3
"""
AI Risk Auditor — Model Context Protocol (MCP) Server.
Enables Claude Desktop, Cursor, and OpenClaw to perform automated AI governance audits.
"""

import sys
import os
import json
from ai_risk_auditor.nist_rmf import NISTAIRMFAuditor
from ai_risk_auditor.mitre_atlas import MITREATLASProber
from ai_risk_auditor.eu_ai_act import EUAIActClassifier
from ai_risk_auditor.red_teamer import RedTeamingEngine

PROTOCOL_VERSION = "2024-11-05"
SERVER_INFO = {
    "name": "ai-risk-auditor-mcp",
    "version": "1.0.0"
}

TOOLS = [
    {
        "name": "classify_eu_ai_act",
        "description": "Classifies an AI system under Regulation (EU) 2024/1689 (Annex III High-Risk vs Minimal Risk).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "Target domain (e.g. life_and_pensions_underwriting)"},
                "intended_purpose": {"type": "string", "description": "Description of AI system purpose"}
            },
            "required": ["domain"]
        }
    },
    {
        "name": "probe_mitre_atlas",
        "description": "Evaluates prompts and inputs against MITRE ATLAS adversarial threat patterns (Prompt Injection & Jailbreaks).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "prompt_text": {"type": "string", "description": "Prompt text to inspect"}
            },
            "required": ["prompt_text"]
        }
    },
    {
        "name": "run_red_team_benchmark",
        "description": "Executes an automated adversarial red-teaming test battery against the AI governance engine.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    }
]

def handle_request(req):
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": SERVER_INFO
            }
        }
    elif method == "notifications/initialized":
        return None
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"tools": TOOLS}
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name == "classify_eu_ai_act":
            classifier = EUAIActClassifier()
            res = classifier.classify_ai_system(args.get("domain"), args.get("intended_purpose", ""))
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}], "isError": False}
            }
        elif tool_name == "probe_mitre_atlas":
            prober = MITREATLASProber()
            res = prober.probe_prompt(args.get("prompt_text", ""))
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}], "isError": False}
            }
        elif tool_name == "run_red_team_benchmark":
            prober = MITREATLASProber()
            redteam = RedTeamingEngine()
            res = redteam.run_adversarial_suite(prober.probe_prompt)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}], "isError": False}
            }
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32602, "message": f"Unknown tool: {tool_name}"}}
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method not found: {method}"}}

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            if resp is not None:
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
