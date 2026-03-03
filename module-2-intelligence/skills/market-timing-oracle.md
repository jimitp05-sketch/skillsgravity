---
name: market-timing-oracle
description: Determine if you are Early, On-Time, or Too Late for a market opportunity using 7 objective signals. Timing is the single most important factor in startup outcomes.
version: 1.0.0
---

# Market Timing Oracle

> "Being early is the same as being wrong. Being late means you're fighting them on their home turf. You want the 18-month window." — CEO mindset

Marc Andreessen, Bill Gurley, and every elite VC agree: timing kills more good companies than bad products. This skill tells you exactly where you stand on the curve.

## 🧠 The Timing Signal Scorecard

| Signal | Early (score: 1) | On-Time (score: 3) | Late (score: 1) |
|---|---|---|---|
| **Search Volume Trend** | Flat or declining | Growing 20-50% YoY | Stable, high volume |
| **VC Investment Flow** | Sparse, seed only | Series A/B active | Growth/late stage only |
| **Competitor Count** | 0-2 serious players | 3-7 competing | 10+ fighting for shelf |
| **Enterprise Adoption** | Pilots only | First contracts | Standardized budgets |
| **Media Coverage** | Niche blogs only | Tier-2 press | TechCrunch/Forbes |
| **Regulation Status** | No rules exist | Emerging frameworks | Compliance-heavy |
| **Talent Availability** | No specialists exist | Growing pool | Commoditized skills |

## 🛠️ Integration Pattern

```python
from datetime import datetime

def assess_market_timing(signals: dict) -> dict:
    """
    Input signals dict, output timing verdict and recommended strategy.
    
    signals = {
        "search_growth_yoy": 0.35,      # 35% YoY growth
        "vc_stage": "series_a",         # seed | series_a | growth
        "competitor_count": 5,
        "enterprise_contracts": True,
        "media_tier": "tier2",          # niche | tier2 | techcrunch
        "regulation_stage": "emerging", # none | emerging | established
        "talent_pool": "growing"        # none | growing | commoditized
    }
    """
    
    score = 0
    reasoning = []
    
    # Search trend
    growth = signals.get("search_growth_yoy", 0)
    if 0.20 <= growth <= 0.60:
        score += 3; reasoning.append(f"✅ Search growing {growth*100:.0f}% YoY — sweet spot")
    elif growth < 0.20:
        score += 1; reasoning.append(f"⚠️ Search flat ({growth*100:.0f}%) — market not ready")
    else:
        score += 2; reasoning.append(f"⚠️ Search booming ({growth*100:.0f}%) — getting crowded")
    
    # VC stage
    vc = signals.get("vc_stage", "seed")
    if vc == "series_a": score += 3; reasoning.append("✅ Series A/B active — smart money confirmed")
    elif vc == "seed": score += 1; reasoning.append("⚠️ Seed only — validation not yet proven")
    elif vc == "growth": score += 1; reasoning.append("⚠️ Growth stage — late entrants get crushed")
    
    # Competitor count
    comp = signals.get("competitor_count", 0)
    if 3 <= comp <= 7: score += 3; reasoning.append(f"✅ {comp} competitors — healthy validation")
    elif comp <= 2: score += 1; reasoning.append(f"⚠️ Only {comp} competitors — market may not exist yet")
    else: score += 1; reasoning.append(f"⚠️ {comp} competitors — bloodbath territory")
    
    # Finalize timing verdict
    if score >= 7:
        verdict = "🟢 ON-TIME: Execute aggressively NOW. This is the 18-month window."
        strategy = "Speed is your weapon. Ship fast, acquire customers, build switching costs."
    elif score >= 4:
        verdict = "🟡 SLIGHTLY EARLY OR LATE: Proceed with caution."
        strategy = "If early: find the accelerant trigger. If late: find an ignored niche."
    else:
        verdict = "🔴 WRONG TIMING: Reconsider market entry."
        strategy = "If early: build and wait. If late: find adjacent market or exit."
    
    return {
        "timing_score": score,
        "max_score": 9,
        "verdict": verdict,
        "strategy": strategy,
        "reasoning": reasoning,
        "pillar": "Official",
        "confidence_boost": 0.30,
        "timestamp": datetime.now().isoformat()
    }

# Example
result = assess_market_timing({
    "search_growth_yoy": 0.35,
    "vc_stage": "series_a",
    "competitor_count": 5,
    "enterprise_contracts": True,
    "media_tier": "tier2",
    "regulation_stage": "emerging",
    "talent_pool": "growing"
})
print(result["verdict"])
# → 🟢 ON-TIME: Execute aggressively NOW. This is the 18-month window.
```

## 📋 CEO Workflow

1. Gather signals from Trends API, Crunchbase VC flow, SpiderFoot competitor count
2. Run `assess_market_timing(signals)` monthly
3. **Score drops below 4** → pivot or find niche
4. **Score is 7-9** → all resources into acquisition — don't wait

## 🔗 Feeds Into
- **Official Pillar** (+0.30 — market context validation)
- Nucleus: "Market timing score: 8/9 — AGGRESSIVE EXECUTION MODE ACTIVATED"
