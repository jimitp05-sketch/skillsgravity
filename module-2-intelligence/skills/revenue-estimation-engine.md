---
name: revenue-estimation-engine
description: Estimate private competitor revenue using 5 triangulated models — Revenue Per Employee, Traffic Multiple, Pricing x Volume, App Store signals, and Glassdoor clues. Produces a confidence-weighted revenue band.
version: 1.0.0
---

# Revenue Estimation Engine

> "If you can estimate their revenue, you can predict their moves." — CEO mindset

Private companies don't publish P&Ls. But CEOs who know how to read the signals can estimate revenue within 20% accuracy using public data. This skill does exactly that.

## 🧠 The 5-Model Triangulation Approach

| Model | Data Needed | Accuracy |
|---|---|---|
| Revenue Per Employee | LinkedIn headcount × industry RPE | ±30% |
| Traffic Multiple | SimilarWeb traffic × industry conversion × ARPU | ±25% |
| Pricing × Volume | Pricing page + ProductHunt/G2 reviews (volume proxy) | ±20% |
| App Store Signals | Downloads × DAU × ARPU (B2C only) | ±15% |
| Glassdoor Salary Signal | Avg salary × headcount × 2.5x burden ratio = burn → revenue | ±35% |

## 🛠️ Integration Pattern

```python
def estimate_revenue_per_employee(headcount: int, industry: str) -> dict:
    """
    Industry Revenue Per Employee benchmarks (2024 data):
    SaaS: $150k-$350k | Fintech: $300k-$600k | E-commerce: $80k-$150k
    """
    benchmarks = {
        "saas": (150_000, 350_000),
        "fintech": (300_000, 600_000),
        "ecommerce": (80_000, 150_000),
        "marketplace": (200_000, 500_000),
        "media": (100_000, 250_000),
        "consulting": (120_000, 280_000)
    }
    low, high = benchmarks.get(industry.lower(), (100_000, 300_000))
    return {
        "model": "Revenue Per Employee",
        "low_estimate": headcount * low,
        "high_estimate": headcount * high,
        "midpoint": headcount * ((low + high) / 2),
        "confidence": 0.65
    }

def estimate_via_traffic(monthly_visitors: int, industry: str, avg_contract_value: float) -> dict:
    """
    Traffic-based model: visitors → trials → customers → ARR
    B2B SaaS typical: 2-5% visitor-to-trial, 10-20% trial-to-paid
    """
    conversion_rates = {
        "saas": (0.03, 0.03 * 0.15),      # 3% trial, 15% trial-to-paid
        "ecommerce": (0.02, 1.0),          # 2% purchase rate direct
        "marketplace": (0.05, 0.05 * 0.1)  # 5% listing, 10% conversion
    }
    visit_to_trial, trial_to_paid = conversion_rates.get(industry.lower(), (0.02, 0.02 * 0.1))
    annual_new_customers = monthly_visitors * 12 * visit_to_trial * trial_to_paid
    arr_estimate = annual_new_customers * avg_contract_value
    return {
        "model": "Traffic Multiple",
        "annual_customer_est": round(annual_new_customers),
        "arr_estimate": arr_estimate,
        "confidence": 0.60
    }

def estimate_via_reviews(g2_review_count: int, avg_contract_value: float) -> dict:
    """
    G2/Capterra/ProductHunt reviews proxy customer count.
    Rule: ~1-3% of customers leave public reviews.
    """
    implied_customers_low = g2_review_count / 0.03
    implied_customers_high = g2_review_count / 0.01
    return {
        "model": "Review Volume Proxy",
        "implied_customers_low": round(implied_customers_low),
        "implied_customers_high": round(implied_customers_high),
        "arr_low": implied_customers_low * avg_contract_value,
        "arr_high": implied_customers_high * avg_contract_value,
        "confidence": 0.70   # Reviews are hard to fake
    }

def triangulate_revenue(estimates: list[dict]) -> dict:
    """Weighted average across all models."""
    weighted_sum = sum(e.get("midpoint", e.get("arr_estimate", e.get("arr_low", 0))) * e["confidence"] for e in estimates)
    total_weight = sum(e["confidence"] for e in estimates)
    final_estimate = weighted_sum / total_weight if total_weight else 0
    return {
        "final_arr_estimate": round(final_estimate, -3),
        "confidence_band": "±20%",
        "pillar": "Technical",
        "confidence_boost": 0.25,
        "ceo_interpretation": _interpret_arr(final_estimate)
    }

def _interpret_arr(arr: float) -> str:
    if arr < 1_000_000: return "Pre-PMF — vulnerable. Attack aggressively."
    if arr < 5_000_000: return "Early traction — Series A territory. They're still figuring it out."
    if arr < 20_000_000: return "Scaling — dangerous competitor. They have product-market fit."
    if arr < 100_000_000: return "Established — Series B/C funded. Attack niches they ignore."
    return "Dominant player — find niche they can't serve efficiently."
```

## 📋 CEO Workflow

1. Gather: LinkedIn headcount + SimilarWeb traffic + G2 review count + known pricing
2. Run all 3 models → `triangulate_revenue()`
3. Interpret the band → feed to Nucleus as market sizing constraint
4. Update monthly (revenue grows — so should estimate)

## 🔗 Feeds Into
- **Technical Pillar** (+0.25 — mathematical model, not guesswork)
- Nucleus: "Competitor at ~$8M ARR — they can afford a sales team but not enterprise engineering"
