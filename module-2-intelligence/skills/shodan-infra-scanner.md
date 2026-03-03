---
name: shodan-infra-scanner
description: Discover competitor tech stacks, server infrastructure, open ports, and vulnerability exposure via Shodan API. Feeds the Technical Pillar.
version: 1.0.0
---

# Shodan Infra Scanner

Use when you need **hard technical evidence** about a competitor's infrastructure — what they run, how exposed they are, and how fast they're scaling.

## 🧠 What Shodan Reveals

| Data Point | Intelligence Value |
|---|---|
| Server software & version | "They use Nginx 1.18 — no longer patched" |
| Open ports | "Port 6379 exposed = Redis likely unprotected" |
| SSL certificate | "Domain registered 3 months ago" |
| Organization size | "ASN owns 54 IPs = serious infra investment" |
| Country/hosting provider | "All on AWS us-east-1 = single-region risk" |

## 🛠️ Integration Pattern

```python
import shodan

API_KEY = "YOUR_SHODAN_KEY"
api = shodan.Shodan(API_KEY)

def scan_competitor_domain(domain: str) -> dict:
    """Full competitor infra profile via Shodan."""
    try:
        # DNS lookup
        dns = api.dns.resolve(domain)
        ip = list(dns.values())[0]

        # IP info
        host = api.host(ip)

        signals = {
            "ip": ip,
            "org": host.get("org", "Unknown"),
            "country": host.get("country_name", "Unknown"),
            "ports": host.get("ports", []),
            "technologies": [],
            "vulns": list(host.get("vulns", {}).keys()),
            "pillar": "Technical",
            "confidence_boost": 0.3    # Direct technical data = max boost
        }

        # Extract tech stack from banners
        for item in host.get("data", []):
            if "product" in item:
                signals["technologies"].append(item["product"])

        return signals

    except shodan.APIError as e:
        return {"error": str(e), "confidence_boost": 0}


def assess_moat_strength(signals: dict) -> str:
    """Evaluate if competitor's infra represents a strong technical moat."""
    port_count = len(signals.get("ports", []))
    vuln_count = len(signals.get("vulns", []))

    if port_count > 20 and vuln_count == 0:
        return "STRONG MOAT — Well-hardened infrastructure"
    elif vuln_count > 3:
        return "WEAK MOAT — Multiple CVEs exposed"
    else:
        return "MODERATE MOAT — Standard setup"
```

## 📋 Workflow

1. Extract competitor's domain from Market Pillar sources
2. Run `scan_competitor_domain(domain)` → get infra profile
3. Run `assess_moat_strength(signals)` → determine if threat is real
4. Feed into `IntelligenceEngine.triangulate_multi_pillar()` as Technical source

## 🔗 Feeds Into
- **Technical Pillar** (+0.30 max, direct API data)
- Grounding Gasket: "Competitor X runs on single AWS region — outage risk present"
