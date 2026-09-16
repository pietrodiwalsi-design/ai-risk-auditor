class AIDashboardGenerator:
    """Generates an executive standalone HTML AI Risk & EU AI Act Governance Dashboard."""

    def generate_html_dashboard(self, nist_res: dict, atlas_res: dict, eu_res: dict, redteam_res: dict) -> str:
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AI Risk Auditor — Enterprise Governance Dashboard</title>
  <style>
    body {{ background: #0f172a; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 30px; margin: 0; }}
    .card {{ background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 24px; margin-bottom: 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.3); }}
    .grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }}
    .metric-card {{ background: #0f172a; border-radius: 10px; padding: 18px; border-left: 4px solid #38bdf8; }}
    .metric-val {{ font-size: 24px; font-weight: 800; color: #f8fafc; margin-top: 6px; }}
    .metric-lbl {{ font-size: 12px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; }}
  </style>
</head>
<body>
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
    <div>
      <h1 style="margin: 0; font-size: 26px; color: #f472b6;">🤖 AI Risk &amp; Governance Audit Dashboard</h1>
      <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 14px;">Standards: NIST AI RMF 1.0 • MITRE ATLAS • EU AI Act (Regulation EU 2024/1689)</p>
    </div>
    <div style="background: #0f172a; padding: 8px 16px; border-radius: 8px; border: 1px solid #f472b6; font-size: 13px; font-weight: 600; color: #f472b6;">
      Classification: {eu_res.get('risk_tier')}
    </div>
  </div>

  <div class="grid">
    <div class="metric-card" style="border-left-color: #38bdf8;">
      <div class="metric-lbl">NIST RMF Maturity</div>
      <div class="metric-val" style="color: #38bdf8;">{nist_res.get('overall_score')}%</div>
      <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">Tier: {nist_res.get('compliance_tier')}</div>
    </div>
    <div class="metric-card" style="border-left-color: #10b981;">
      <div class="metric-lbl">Adversarial Defense</div>
      <div class="metric-val" style="color: #10b981;">{redteam_res.get('defense_success_rate_pct')}%</div>
      <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">Tests Neutralized: {redteam_res.get('threats_neutralized')}/{redteam_res.get('total_adversarial_tests')}</div>
    </div>
    <div class="metric-card" style="border-left-color: #f59e0b;">
      <div class="metric-lbl">MITRE ATLAS Status</div>
      <div class="metric-val" style="color: #f59e0b; font-size: 18px; margin-top: 10px;">{atlas_res.get('status')}</div>
    </div>
    <div class="metric-card" style="border-left-color: #f472b6;">
      <div class="metric-lbl">EU AI Act Tier</div>
      <div class="metric-val" style="color: #f472b6; font-size: 18px; margin-top: 10px;">Annex III High-Risk</div>
    </div>
  </div>

  <div class="card">
    <h2 style="font-size: 17px; margin-top: 0; color: #f8fafc;">🏛️ Mandatory EU AI Act Compliance Controls</h2>
    <ul style="color: #cbd5e1; line-height: 1.8; font-size: 14px;">
      {"".join(f"<li><b>{ob}</b></li>" for ob in eu_res.get('mandatory_obligations', []))}
    </ul>
  </div>
</body>
</html>"""
        return html
