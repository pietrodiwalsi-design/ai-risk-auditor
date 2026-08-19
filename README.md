# AI Risk Auditor (`ai-risk-auditor`)

> **Enterprise AI Risk & Governance Assessment Tool**  
> Mapped to **NIST AI RMF 1.0**, **MITRE ATLAS**, and the **EU AI Act**.  
> Built for automated model auditing, guardrails testing, and agentic permission reviews.

---

## 🎯 Executive Overview

**AI Risk Auditor** is a specialized assessment and governance tool tailored for Chief Risk Officers (CROs), Heads of IT Risk, and Enterprise AI Governance Teams (specifically in regulated sectors like Life & Pensions, Banking, and Insurance).

The tool automates the structured evaluation of AI/LLM implementations against internationally recognized governance frameworks:
1. **NIST AI RMF 1.0:** Evaluation across the four core functions: *Govern*, *Map*, *Measure*, and *Manage*.
2. **MITRE ATLAS (Adversarial Threat Landscape for AI Systems):** Automated vulnerability probing for prompt injection, jailbreaking, training data poisoning, and model evasion.
3. **EU AI Act Compliance Engine:** Automated risk-tier classification (Prohibited, High-Risk, Specific Transparency Risk, Minimal Risk) and Annex III conformity checking.
4. **On-Demand Skill Integration:** Integrates seamlessly with local AgentSkills libraries (800+ structured cybersecurity and AI risk procedures).

---

## 🏗️ Architecture & Core Modules

```
┌─────────────────────────────────────────────────────────────┐
│                    AI Risk Auditor CLI                      │
└──────────────────────────────┬──────────────────────────────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  NIST AI RMF │       │ MITRE ATLAS  │       │  EU AI Act   │
│  Governance  │       │ Threat Probe │       │ Conformity   │
│   Engine     │       │    Engine    │       │   Checker    │
└──────┬───────┘       └──────┬───────┘       └──────┬───────┘
       │                      │                      │
       └──────────────────────┼──────────────────────┘
                              │
                              ▼
        ┌───────────────────────────────────────────┐
        │   Audit Report & Risk Register Generator  │
        │      (Markdown / PDF / JSON Export)       │
        └───────────────────────────────────────────┘
```

### Key Modules:
- `src/evaluator.py`: Core scoring and compliance evaluation logic.
- `src/probes/`: Automated prompt injection, guardrails, and adversarial testing harnesses.
- `src/reporters/`: Generates audit-ready Executive Memos, Heatmaps, and Risk Registers.
- `config/frameworks.json`: Comprehensive mappings to NIST AI RMF, MITRE ATLAS, and EU AI Act articles.

---

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/pietrodiwalsi-design/ai-risk-auditor.git
cd ai-risk-auditor
pip install -r requirements.txt
```

### Basic Usage
```bash
# Run full assessment on an AI System profile
python3 -m src.cli assess --config examples/customer-support-llm.json

# Check EU AI Act risk classification
python3 -m src.cli classify-eu --system-type "biometric-or-pension-scoring"

# Probe LLM endpoints for prompt injection vulnerabilities
python3 -m src.cli probe --endpoint "https://api.internal/llm" --type injection
```

---

## 📋 Compliance & Framework Coverage

| Framework | Core Scope | Implemented Checks |
| :--- | :--- | :--- |
| **NIST AI RMF 1.0** | Govern, Map, Measure, Manage | 48 verification checks across transparency, accountability & robustness |
| **MITRE ATLAS** | AI/ML Threat Matrix | 32 adversarial test scenarios (Jailbreak, Inversion, Poisoning) |
| **EU AI Act** | Articles 9, 10, 13, 14, 15 | High-Risk technical documentation, human oversight & accuracy checks |

---

## 📄 License
MIT License. Developed by [pietrodiwalsi-design](https://github.com/pietrodiwalsi-design).
