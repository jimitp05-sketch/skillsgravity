---
name: sherlock-identity-pivot
description: Cross-platform username search across 400+ websites via Sherlock. Use when you have a handle and need to pivot to their full digital footprint.
version: 1.0.0
---

# Sherlock Identity Pivot

Use when the **Recursive Pivot Engine detects a username** from one source and needs to trace that identity across other platforms.

## 🎯 When To Use

```
Research Loop finds: GitHub contributor → username = "jimitshah95"
→ Invoke sherlock-identity-pivot
→ Discovers: Twitter, Reddit, Medium, Hacker News, ProductHunt presence
→ Each profile = new data source for Triangulation
```

## 🛠️ Integration Pattern

```python
import subprocess
import json

def sherlock_pivot(username: str, output_dir: str = "/tmp/sherlock") -> list[dict]:
    """
    Run Sherlock username search and parse results.
    Returns a list of discovered platform URLs.
    """
    cmd = [
        "python3", "-m", "sherlock",
        username,
        "--output", f"{output_dir}/{username}.txt",
        "--print-found",
        "--timeout", "10"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    found_profiles = []
    for line in result.stdout.splitlines():
        if line.startswith("[+]"):
            url = line.replace("[+] ", "").strip()
            found_profiles.append({
                "platform": _extract_platform(url),
                "url": url,
                "pillar": "Market",       # Social presence = Market signal
                "confidence_boost": 0.1   # Each profile adds to Market pillar
            })
    return found_profiles

def _extract_platform(url: str) -> str:
    """Extract platform name from URL."""
    for platform in ["reddit", "twitter", "github", "producthunt", "medium", "hackernews"]:
        if platform in url.lower():
            return platform.capitalize()
    return "Unknown"

# Usage
profiles = sherlock_pivot("jimitshah95")
# → Feed each found profile URL into OSINT scan as new source
```

## 📋 Workflow

1. Receive pivot variable from `IntelligenceEngine.research_loop()`
2. Run `sherlock_pivot(username)` with stealth delay pre-set
3. Each discovered profile URL → add as new source to signal data
4. Re-run `triangulate_multi_pillar()` with expanded sources

## 🔒 Stealth Rules
- Max 10 concurrent platform checks (avoid rate-limit ban)
- Add 0.5s jitter between checks via `StealthOrchestrator.human_delay("micro")`
- Never use real name — always search by USERNAME, not email

## 📊 Output Format

```json
{
  "pivot_from": "GitHub contributor",
  "username": "jimitshah95",
  "profiles_found": 7,
  "platforms": ["Reddit", "Twitter", "ProductHunt", "Medium"],
  "market_pillar_contribution": 0.3,
  "new_sources_for_triangulation": ["https://reddit.com/u/jimitshah95"]
}
```
