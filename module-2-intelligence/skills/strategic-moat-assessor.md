---
name: strategic-moat-assessor
description: Objectively score a competitor's strategic moat across 7 dimensions. Know exactly where they're unbeatable, where they're weak, and where to attack.
version: 1.0.0
---

# Strategic Moat Assessor

> "The best founders don't fight markets — they find the crack in the wall the incumbent can't patch." — CEO mindset

A moat isn't just "they're big." It's a specific, compounding structural advantage. This skill scores ALL of them objectively so you know exactly where to fight.

## 🧠 The 7-Dimensional Moat Framework

| Moat Type | Maximum Score | Evidence Source |
|---|---|---|
| **Network Effects** | 25 | User growth rate, marketplace density, social sharing |
| **Switching Costs** | 20 | Integration depth, data portability, migration pain |
| **Data Advantage** | 15 | Unique datasets, training data moat, personalization depth |
| **Brand & Trust** | 15 | NPS surveys, Glassdoor score, media mentions |
| **Regulatory Moat** | 10 | Licenses, compliance certifications, government contracts |
| **Cost Structure** | 10 | Gross margin (public comps), infra efficiency signals |
| **Talent Density** | 5 | PhD/ex-FAANG concentration on LinkedIn |
| **TOTAL** | **100** | |

## 🛠️ Integration Pattern

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class MoatScore:
    network_effects: float = 0       # 0-25
    switching_costs: float = 0       # 0-20
    data_advantage: float = 0        # 0-15
    brand_trust: float = 0           # 0-15
    regulatory_moat: float = 0       # 0-10
    cost_structure: float = 0        # 0-10
    talent_density: float = 0        # 0-5

def score_network_effects(user_growth_rate: float, marketplace_density: float) -> float:
    """Higher user growth + density = stronger network moat."""
    growth_score = min(user_growth_rate * 5, 15)     # Cap at 15 for growth
    density_score = min(marketplace_density * 2, 10)  # Cap at 10 for density
    return min(growth_score + density_score, 25)

def score_switching_costs(integrations_count: int, has_migration_tool: bool, data_export: bool) -> float:
    """More integrations + no migration tool = higher lock-in."""
    score = min(integrations_count * 1.5, 10)
    if not has_migration_tool: score += 7
    if not data_export: score += 3
    return min(score, 20)

def score_data_advantage(unique_dataset: bool, user_data_value: str) -> float:
    """Proprietary data is almost impossible to replicate."""
    score = 0
    if unique_dataset: score += 10
    data_values = {"low": 0, "medium": 3, "high": 5}
    score += data_values.get(user_data_value, 0)
    return min(score, 15)

def assess_full_moat(competitor: str, signals: dict) -> dict:
    """Build complete moat score from signal dict."""
    score = MoatScore()
    score.network_effects = score_network_effects(
        signals.get("user_growth_rate", 0),
        signals.get("marketplace_density", 0)
    )
    score.switching_costs = score_switching_costs(
        signals.get("integrations_count", 0),
        signals.get("has_migration_tool", True),
        signals.get("has_data_export", True)
    )
    score.data_advantage = score_data_advantage(
        signals.get("unique_dataset", False),
        signals.get("user_data_value", "low")
    )
    score.brand_trust = signals.get("brand_score", 0)
    score.regulatory_moat = signals.get("regulatory_score", 0)
    score.cost_structure = signals.get("cost_score", 0)
    score.talent_density = signals.get("talent_score", 0)
    
    total = sum([score.network_effects, score.switching_costs, score.data_advantage,
                 score.brand_trust, score.regulatory_moat, score.cost_structure, score.talent_density])
    
    weakest = min(
        [("Network Effects", score.network_effects, 25),
         ("Switching Costs", score.switching_costs, 20),
         ("Data Advantage", score.data_advantage, 15)],
        key=lambda x: x[1] / x[2]   # Score as % of max
    )
    
    return {
        "competitor": competitor,
        "total_moat_score": round(total, 1),
        "moat_tier": "FORTRESS" if total > 75 else "STRONG" if total > 50 else "MODERATE" if total > 30 else "WEAK",
        "attack_vector": f"Weakest moat: {weakest[0]} at {weakest[1]:.0f}/{weakest[2]} — THIS is where to attack",
        "scores": score.__dict__,
        "pillar": "Technical",
        "confidence_boost": 0.25
    }

# CEO output example:
# → MODERATE moat (42/100). Attack vector: Data Advantage (2/15). 
# → "Build proprietary dataset they can't access — this is our wedge."
```

## 📋 CEO Workflow

1. Gather signals from SpiderFoot, Shodan, Sherlock, LinkedIn scans
2. Score each dimension with available evidence
3. **Find the lowest score/max ratio** → that's your attack vector
4. Feed to Nucleus: "Competitor moat is 42/100 — exploit data gap"

## 🔗 Feeds Into
- **Technical Pillar** (+0.25)
- Nucleus decision layer as hard strategic constraint
