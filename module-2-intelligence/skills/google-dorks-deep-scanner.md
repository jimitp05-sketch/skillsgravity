---
name: google-dorks-deep-scanner
description: Generate and execute advanced Google Dork queries to surface hidden pricing pages, internal docs, GitHub repos, and leaked data. Automates what takes analysts hours.
version: 1.0.0
---

# Google Dorks Deep Scanner

Use when standard search isn't finding competitor data. Dorks bypass surface-level results to expose documents, internal pages, and technical artifacts.

## 🧠 Dork Templates by Intelligence Goal

### Find Pricing & Plans
```
site:competitor.com (pricing OR plans OR "per month" OR "per user")
site:competitor.com filetype:pdf "pricing" OR "proposal"
```

### Find Technical Documentation
```
site:competitor.com (api OR docs OR swagger OR openapi)
site:github.com "competitor-name" (config OR env OR .yaml OR .json)
```

### Find Team & Culture Signals
```
site:linkedin.com "competitor name" (engineer OR "software" OR "head of")
site:glassdoor.com "competitor name" review
```

### Find Media & Investor Intel
```
site:techcrunch.com OR site:crunchbase.com "competitor name" (funding OR raised OR valuation)
"competitor name" filetype:pdf (pitch OR deck OR investor)
```

### Find Breaches & Leaks
```
site:pastebin.com "competitor.com"
site:github.com "competitor.com" "api_key" OR "password" OR "secret"
```

## 🛠️ Integration Pattern

```python
from urllib.parse import urlencode
import requests, time

SERPAPI_KEY = "YOUR_SERPAPI_KEY"   # Or use SerpAPI for programmatic access

def execute_dork(dork_query: str, num_results: int = 10) -> list[dict]:
    """Execute a Google Dork via SerpAPI and return structured results."""
    params = {
        "q": dork_query,
        "api_key": SERPAPI_KEY,
        "num": num_results,
        "safe": "off"
    }
    resp = requests.get("https://serpapi.com/search", params=params)
    results = resp.json().get("organic_results", [])
    return [{"title": r["title"], "url": r["link"], "snippet": r.get("snippet", "")} for r in results]

def generate_dork_suite(competitor_domain: str) -> list[str]:
    """Generate a complete dork suite for a competitor domain."""
    return [
        f'site:{competitor_domain} (pricing OR plans OR "per month")',
        f'site:{competitor_domain} filetype:pdf',
        f'site:github.com "{competitor_domain}"',
        f'"{competitor_domain}" (raised OR "series A" OR valuation)',
        f'site:glassdoor.com "{competitor_domain.split(".")[0]}" review',
    ]

def run_full_dork_sweep(competitor_domain: str) -> list[dict]:
    """Run all dorks and collect signals with stealth delays."""
    all_results = []
    for dork in generate_dork_suite(competitor_domain):
        results = execute_dork(dork)
        for r in results:
            r["dork_used"] = dork
            r["pillar"] = "Official"
            r["confidence_boost"] = 0.1
            all_results.append(r)
        time.sleep(2)    # Stealth: don't hammer Google
    return all_results
```

## 📋 Workflow

1. Extract competitor domain from memory vault or prior scan
2. Run `run_full_dork_sweep("competitor.com")`
3. Each result URL → feed into `SignalCompressionPipeline`
4. Compressed signal → `IntelligenceEngine.triangulate_multi_pillar()`

## 🔗 Feeds Into
- **Official Pillar** (primary — document & indexed content)
- **Recursive Pivot Engine** (any GitHub URL found → spawn new Sherlock pivot)
