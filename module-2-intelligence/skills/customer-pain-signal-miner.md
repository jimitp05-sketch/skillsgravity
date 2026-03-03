---
name: customer-pain-signal-miner
description: Mine G2, Capterra, Reddit, Glassdoor, and support forums to extract the REAL pain points competitors ignore. This is where billion-dollar product wedges are found.
version: 1.0.0
---

# Customer Pain Signal Miner

> "Your competitor's 1-star reviews are your product roadmap." — CEO mindset

Every negative review of a competitor is a customer who desperately needs a better solution. The CEO who reads them first owns the market.

## 🧠 Where the Gold Is Hidden

| Source | Signal Type | Insight Value |
|---|---|---|
| G2 reviews (1-3 stars) | Product pain points | Direct "what the product fails to do" |
| Reddit r/[industry] | Raw frustration | Unfiltered honest product criticism |
| Glassdoor reviews | Internal culture/product quality | Engineering debt signals |
| Twitter/X complaints (@competitor) | Real-time churn signals | Immediate pain, often viral |
| ProductHunt comments | Early adopter friction | Technical and UX gaps |
| Support forum questions | Feature gaps | "How do I do X?" = X is missing |
| Hacker News threads | Deep technical criticism | Architecture and reliability pain |

## 🛠️ Integration Pattern

```python
import requests, re
from collections import Counter

def scrape_g2_reviews(product_slug: str, min_stars: int = 1, max_stars: int = 3) -> list[dict]:
    """
    Scrape G2 low-rating reviews for competitor pain signals.
    Returns parsed pain point list.
    """
    headers = {"User-Agent": "Mozilla/5.0 Chrome/120.0.0.0"}
    url = f"https://www.g2.com/products/{product_slug}/reviews"
    resp = requests.get(url, headers=headers, timeout=10)
    
    # Extract review text from page (simplified)
    reviews_raw = re.findall(r'"body":"([^"]{50,500})"', resp.text)
    pain_points = [r for r in reviews_raw if any(neg in r.lower() for neg in
                   ["slow", "missing", "wish", "can't", "doesn't", "hard to", "confusing",
                    "expensive", "no way to", "limited", "broken", "buggy", "support"])]
    return pain_points[:20]

def mine_reddit_pain(subreddit: str, competitor_name: str) -> list[dict]:
    """Mine Reddit for frustrated customers.."""
    url = f"https://www.reddit.com/r/{subreddit}/search.json"
    params = {"q": competitor_name, "sort": "new", "limit": 25, "t": "year"}
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, params=params)
    posts = resp.json().get("data", {}).get("children", [])
    
    pain_threads = []
    for p in posts:
        data = p["data"]
        if any(word in data.get("title", "").lower() for word in
               ["problem", "issue", "help", "broken", "alternative", "switch", "frustrated", "worst"]):
            pain_threads.append({
                "title": data["title"],
                "score": data["score"],
                "url": f"https://reddit.com{data['permalink']}"
            })
    return pain_threads

def extract_pain_themes(pain_points: list[str]) -> dict:
    """Cluster pain points into actionable product themes."""
    theme_keywords = {
        "Performance": ["slow", "crash", "lag", "timeout", "down"],
        "Missing Features": ["missing", "no way to", "wish", "can't", "would love"],
        "Pricing": ["expensive", "overpriced", "cost", "per seat", "billing"],
        "UX Complexity": ["confusing", "hard to", "unintuitive", "learning curve"],
        "Support Quality": ["support", "response", "ticket", "ignored"],
        "Integration Gaps": ["integrate", "api", "connect", "export", "import"],
        "Reliability": ["buggy", "broken", "error", "bug", "inconsistent"]
    }
    theme_counts = Counter()
    for point in pain_points:
        point_lower = point.lower()
        for theme, keywords in theme_keywords.items():
            if any(kw in point_lower for kw in keywords):
                theme_counts[theme] += 1
    
    top_pain = theme_counts.most_common(3)
    return {
        "top_pain_themes": top_pain,
        "product_wedge": top_pain[0][0] if top_pain else "Unknown",
        "strategic_note": f"Build what they can't: focus on {top_pain[0][0] if top_pain else 'core gaps'}",
        "pillar": "Market",
        "confidence_boost": 0.25
    }

# Full pipeline
def full_pain_mining(competitor: str, g2_slug: str, reddit: str) -> dict:
    g2_pain = scrape_g2_reviews(g2_slug)
    reddit_pain = mine_reddit_pain(reddit, competitor)
    themes = extract_pain_themes(g2_pain)
    return {
        "competitor": competitor,
        "g2_samples": g2_pain[:5],
        "reddit_signals": reddit_pain[:5],
        "themes": themes
    }
```

## 📋 CEO Workflow

1. Run `full_pain_mining()` for top 3 competitors
2. Extract top pain theme per competitor
3. Cross-reference: **if same pain appears across 2+ competitors → massive market gap**
4. Feed to Nucleus: "3 competitors all fail at [X] — this is our v1 wedge"

## 🔗 Feeds Into
- **Market Pillar** (+0.25 — real customer voice)
- Product team: Direct feature roadmap input
- Nucleus: Shapes product-market fit hypothesis
