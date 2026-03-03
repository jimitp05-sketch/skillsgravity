---
name: spiderfoot-auto-recon
description: Run automated OSINT reconnaissance via SpiderFoot API. Covers 200+ public sources — DNS, WHOIS, social, threat intel, dark web mentions.
version: 1.0.0
---

# SpiderFoot Auto-Recon

Use this skill when you need deep, automated background intelligence on a **company, domain, or person** before your main Intelligence scan.

## 🧠 How SpiderFoot Works

SpiderFoot sends a single seed (domain, IP, email, username) and recursively fans out across **200+ modules** — discovering subdomains, breached emails, Shodan-indexed services, social media handles, company registrations, and threat intel matches.

```
Seed → Scan ID → Module network fans out → JSON report
```

## 🛠️ Integration Pattern

```python
import requests

BASE = "http://127.0.0.1:5001"   # Local SpiderFoot instance

def run_spiderfoot_scan(seed: str, scan_name: str) -> dict:
    """Start a SpiderFoot scan and return the scan ID."""
    payload = {
        "scanname": scan_name,
        "scantarget": seed,
        "typetarget": "INTERNET_NAME",
        "usecase": "all",
        "modulelist": "",
    }
    resp = requests.post(f"{BASE}/startscan", data=payload)
    return resp.json()  # Returns scan_id

def get_results(scan_id: str) -> list[dict]:
    """Fetch structured results once scan completes."""
    resp = requests.get(f"{BASE}/scaneventresultsunique?id={scan_id}&eventType=all")
    return resp.json()

def extract_high_value(results: list[dict]) -> dict:
    """Filter SpiderFoot output for Intelligence Engine signals."""
    signals = []
    for r in results:
        if r.get("type") in ["EMAILADDR", "LINKED_URL_INTERNAL", "SOCIAL_MEDIA", "COMPANY_NAME", "VULNERABILITY_GENERAL"]:
            signals.append({
                "type": r["type"],
                "data": r["data"],
                "confidence_boost": 0.2     # Technical pillar contribution
            })
    return {"pillar": "Technical", "source": "SpiderFoot", "signals": signals}
```

## 📋 Workflow

1. Boot SpiderFoot: `python3 sf.py -l 127.0.0.1:5001`
2. Call `run_spiderfoot_scan(seed="target.com", scan_name="CI Scan 001")`
3. Wait for scan complete (poll `/scanstatus`)
4. Call `get_results(scan_id)` → filter with `extract_high_value()`
5. Feed results to `IntelligenceEngine.triangulate_multi_pillar()`

## ⚠️ Stealth Rules
- Only run in OFFLINE/VM mode (SpiderFoot pings many services — your IP gets logged)
- Use Tor exit node if targeting live competitors
- Always run after StealthOrchestrator has set session delay

## 🔗 Feeds Into
- **Technical Pillar** of Triple-Pillar Triangulation (+0.20 confidence)
- `research-log.json` via `IntelligenceEngine.log_research()`
