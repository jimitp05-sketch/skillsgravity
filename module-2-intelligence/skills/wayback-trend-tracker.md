---
name: wayback-trend-tracker
description: Use Wayback Machine CDX API to detect pricing changes, pivots, messaging shifts, and team evolution. Confirms Historical Projection pillar.
version: 1.0.0
---

# Wayback Trend Tracker

Use when you need to **verify that a market signal is persistent** — not just a moment in time. Historical consistency confirms the signal is a real trend, not noise.

## 🎯 What It Detects

- **Pricing pivots** — "They raised prices 3x over 18 months"
- **Messaging changes** — "Homepage changed from 'API tool' to 'AI platform'"
- **Team growth** — "About page went from 3 people to 40"
- **Product pivots** — "Features section rewritten to target enterprise"

## 🛠️ Integration Pattern

```python
import requests
from datetime import datetime, timedelta

CDX_API = "http://web.archive.org/cdx/search/cdx"

def get_snapshots(domain: str, months_back: int = 12) -> list[dict]:
    """Get all Wayback snapshots for a domain over the past N months."""
    from_date = (datetime.now() - timedelta(days=30 * months_back)).strftime("%Y%m%d")
    params = {
        "url": domain,
        "output": "json",
        "fl": "timestamp,statuscode,mimetype",
        "from": from_date,
        "filter": "statuscode:200",
        "collapse": "timestamp:8",   # One snapshot per day
        "limit": 50
    }
    resp = requests.get(CDX_API, params=params)
    raw = resp.json()
    return [{"ts": r[0], "url": f"https://web.archive.org/web/{r[0]}/{domain}"} for r in raw[1:]]

def fetch_snapshot_text(archive_url: str) -> str:
    """Fetch plain-text content of a Wayback snapshot."""
    resp = requests.get(archive_url, timeout=10)
    # Quick extraction of visible text (no BS4 required)
    import re
    text = re.sub(r"<[^>]+>", " ", resp.text)
    text = re.sub(r"\s+", " ", text)
    return text[:3000]   # Cap at 3000 chars for token efficiency

def detect_pivot(snapshots: list[dict], keyword: str) -> dict:
    """Check if a keyword appears/disappears over time — signals a pivot."""
    timeline = []
    for snap in snapshots[:5]:   # Check 5 snapshots spread over period
        text = fetch_snapshot_text(snap["url"])
        present = keyword.lower() in text.lower()
        timeline.append({"date": snap["ts"], "keyword_present": present})
    
    changes = sum(1 for i in range(1, len(timeline)) if timeline[i]["keyword_present"] != timeline[i-1]["keyword_present"])
    return {
        "keyword": keyword,
        "timeline": timeline,
        "pivot_detected": changes >= 2,
        "pillar": "Official",         # Historical public data = Official pillar
        "confidence_boost": 0.15
    }

# Example Usage
snapshots = get_snapshots("competitor.com", months_back=12)
pivot = detect_pivot(snapshots, "enterprise")
# → "enterprise" first appeared 9 months ago → messaging pivot confirmed
```

## 📋 Workflow

1. Get competitor domain from earlier OSINT scan
2. Fetch 12-month snapshot history via `get_snapshots()`
3. Run `detect_pivot()` for keywords: "pricing", "enterprise", "API", "team"
4. Historical pivots → feed into Official Pillar as supporting evidence

## 🔗 Feeds Into
- **Official Pillar** (+0.15 historical verification bonus)
- Memory Vault: "Company X pivoted to enterprise 9 months ago [Confirmed]"
