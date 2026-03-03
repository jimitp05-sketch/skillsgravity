---
name: competitor-pricing-radar
description: Track competitor pricing changes in real-time. Detects stealth price hikes, discounting patterns, and packaging pivots before they hit the market. CEO-level intelligence for pricing strategy.
version: 1.0.0
---

# Competitor Pricing Radar

> "Pricing is strategy. If you don't know what competitors charge, you're flying blind." — CEO mindset

A CEO watches pricing the way a general watches enemy troop movements. Every price change tells a story: funding pressure, customer churn, new ICP, or a desperate bid to survive.

## 🧠 What Pricing Changes Actually Signal

| Change | What It Really Means |
|---|---|
| Sudden 20%+ price hike | They found their ICP and are squeezing loyal customers |
| New "Startup" tier added | Their enterprise deal velocity has slowed |
| Freemium to paid-only pivot | Burn rate pressure — runway is shortening |
| Annual discount appeared | Monthly churn is hurting them |
| Seat-based → usage-based switch | Enterprise deals are being blocked by legal/procurement |
| Enterprise tier removed from website | Moving upmarket OR downmarket |

## 🛠️ Integration Pattern

```python
import requests, hashlib, json, os
from datetime import datetime

PRICING_CACHE = "pricing_cache.json"

def scrape_pricing_page(domain: str) -> str:
    """Fetch raw pricing page content."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}
    resp = requests.get(f"https://{domain}/pricing", headers=headers, timeout=10)
    return resp.text[:8000]

def hash_page(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()

def load_cache() -> dict:
    if os.path.exists(PRICING_CACHE):
        with open(PRICING_CACHE) as f:
            return json.load(f)
    return {}

def detect_pricing_change(domain: str) -> dict:
    """Compare current pricing page to cached version — detect any drift."""
    cache = load_cache()
    current_content = scrape_pricing_page(domain)
    current_hash = hash_page(current_content)
    
    result = {
        "domain": domain,
        "timestamp": datetime.now().isoformat(),
        "changed": False,
        "signal": None
    }
    
    if domain in cache:
        if cache[domain]["hash"] != current_hash:
            result["changed"] = True
            result["signal"] = f"PRICING CHANGED: {domain} — manual review required"
            result["previous_snapshot"] = cache[domain]["snapshot"][:500]
            result["current_snapshot"] = current_content[:500]
    
    # Update cache
    cache[domain] = {
        "hash": current_hash,
        "snapshot": current_content[:1000],
        "last_seen": datetime.now().isoformat()
    }
    with open(PRICING_CACHE, "w") as f:
        json.dump(cache, f, indent=2)
    
    return result

def run_pricing_sweep(competitors: list[str]) -> list[dict]:
    """Run pricing check across all tracked competitors."""
    alerts = []
    for domain in competitors:
        result = detect_pricing_change(domain)
        if result["changed"]:
            alerts.append(result)
    return alerts

# Example
alerts = run_pricing_sweep(["competitor-a.com", "competitor-b.com"])
for a in alerts:
    print(f"🚨 PRICING ALERT: {a['domain']} at {a['timestamp']}")
```

## 📋 CEO Workflow

1. **Daily sweep** (cron at 9am): `run_pricing_sweep(competitor_list)`
2. Any alert → **manual review** of diff (snapshot vs. current)
3. Classify the change (see Signal Matrix above)
4. Feed classified change into Nucleus: `"Competitor X raised prices 30% — window to poach churned customers"`

## 🔗 Feeds Into
- **Market Pillar** of Triangulation (+0.15)
- Nucleus: "Adjust our pricing positioning based on X's changes"
