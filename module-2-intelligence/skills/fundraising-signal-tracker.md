---
name: fundraising-signal-tracker
description: Track competitor funding rounds, investor moves, and acquisition signals before they're announced. Know who has runway, who's desperate, and who's about to be acquired.
version: 1.0.0
---

# Fundraising Signal Tracker

> "Funding is oxygen. Know who's running out before they do." — CEO mindset

Every startup tells a fundraising story through public signals — job postings, executive hires, domain purchases, and LinkedIn endorsement spikes — weeks before any TechCrunch announcement.

## 🧠 The Pre-Announcement Signal Matrix

| Signal | What It Predicts |
|---|---|
| CxO join LinkedIn + "excited to join" post | Raised a round — hired with new capital |
| "Head of Finance" or "CFO" job posting | Pre-fundraise hiring for investor credibility |
| New `.com` domain purchased (Wayback data) | Rebrand — likely funded, pivoting to new brand |
| Sudden 5x spike in LinkedIn followers | PR push — often pre-announce hype |
| 3+ top-tier VC partners follow on LinkedIn | Due diligence in progress |
| Y Combinator batch list | Funded — 6-12 months of runway |
| Crunchbase "undisclosed" round added | Raised but not disclosed yet |
| Glassdoor: rapid headcount growth | Hired after raising |

## 🛠️ Integration Pattern

```python
import requests, json
from datetime import datetime

CRUNCHBASE_API = "https://api.crunchbase.com/api/v4"
CB_KEY = "YOUR_CRUNCHBASE_KEY"

def get_funding_rounds(org_name: str) -> list[dict]:
    """Get funding history from Crunchbase API."""
    url = f"{CRUNCHBASE_API}/searches/funding_rounds"
    payload = {
        "field_ids": ["funded_organization_identifier", "announced_on", "money_raised", "investment_type"],
        "predicate": {"field_id": "funded_organization_identifier", "operator_id": "includes", "values": [org_name]}
    }
    resp = requests.post(url, json=payload, params={"user_key": CB_KEY})
    return resp.json().get("entities", [])

def estimate_runway(last_round_date: str, amount_raised: float, headcount: int) -> dict:
    """Estimate remaining runway based on burn rate model."""
    avg_burn_per_head_monthly = 15000   # Industry avg: $15k/employee/month (salary + overhead)
    monthly_burn = headcount * avg_burn_per_head_monthly
    from datetime import datetime, timedelta
    funded_date = datetime.fromisoformat(last_round_date)
    months_elapsed = (datetime.now() - funded_date).days / 30
    capital_consumed = months_elapsed * monthly_burn
    remaining = amount_raised - capital_consumed
    months_remaining = remaining / monthly_burn if monthly_burn else 0
    
    return {
        "monthly_burn_est": f"${monthly_burn:,.0f}",
        "months_remaining": round(months_remaining, 1),
        "status": "FUNDRAISING_URGENCY" if months_remaining < 6 else \
                  "HEALTHY" if months_remaining > 18 else "WATCHING",
        "strategic_note": f"Competitor has ~{round(months_remaining,1)} months of runway left"
    }

def scan_linkedin_headcount_growth(company_name: str) -> dict:
    """
    Proxy check: LinkedIn company page employee count changes.
    (Run via Google dork: site:linkedin.com/company company_name)
    """
    dork = f'site:linkedin.com/company "{company_name}"'
    # Feed to google-dorks-deep-scanner → extract employee count from snippet
    return {
        "dork": dork,
        "instruction": "Extract employee count from LinkedIn snippet. Compare to 30-day-ago cache. >20% growth = post-funding hiring spree."
    }

# Full workflow
def fundraising_intelligence(competitor: str, org_name: str, estimated_headcount: int) -> dict:
    rounds = get_funding_rounds(org_name)
    if rounds:
        latest = rounds[0]["properties"]
        runway = estimate_runway(
            latest.get("announced_on", "2024-01-01"),
            float(latest.get("money_raised", {}).get("value", 0) or 0),
            estimated_headcount
        )
        return {
            "competitor": competitor,
            "last_round": latest,
            "runway_model": runway,
            "pillar": "Official",
            "confidence_boost": 0.3
        }
    return {"competitor": competitor, "status": "No public funding found"}
```

## 📋 CEO Workflow

1. Load competitor list + estimated headcounts from memory vault
2. Run `fundraising_intelligence()` for each
3. `FUNDRAISING_URGENCY` → **attack signal**: pitch their customers NOW (they'll churn soon)
4. `HEALTHY` → **respect signal**: they have runway to fight back — plan long-term

## 🔗 Feeds Into
- **Official Pillar** (+0.30 — Crunchbase is an authoritative public record)
- Nucleus: "Competitor X has 4 months of runway — aggressive land-and-expand strategy recommended"
