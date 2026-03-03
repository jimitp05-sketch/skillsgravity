---
name: bypass-patterns-vault
description: A self-growing library of platform-specific bypass signatures for Cloudflare, DataDome, Akamai, and more. Consulted by StealthOrchestrator before every session.
version: 1.0.0
---

# Bypass Patterns Vault

A living knowledge base that the `StealthOrchestrator` consults BEFORE attempting any extraction. Stores what has worked and what has failed, per platform.

## 🧠 Architecture

```
bypass-patterns.json
├── per_platform_profiles
│   ├── cloudflare
│   ├── datadome
│   ├── akamai
│   └── generic_bot_wall
└── session_lessons
    ├── success_signatures
    └── failed_patterns
```

## 🛠️ Bypass Signatures by Platform

### Cloudflare (Turnstile / Bot Management)
```python
CLOUDFLARE_PROFILE = {
    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36",
    "headers": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1"
    },
    "tls_fingerprint": "chrome_120",   # JA3/JA4 must match Chrome 120
    "pre_action": "visit_homepage_first",   # Don't jump to deep URL
    "delay_between_pages": (3.5, 8.0),     # Heavy jitter
    "max_pages_per_session": 12            # Don't scrape more — triggers ML
}
```

### DataDome (Behavioral ML Analyzer)
```python
DATADOME_PROFILE = {
    "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/119.0.0.0",
    "strategy": "simulate_full_session",   # Must look like human browsing journey
    "mouse_entropy": True,                 # Requires jitter simulation
    "scroll_pattern": "non_linear",        # DataDome tracks scroll entropy
    "session_actions": [
        "hover_nav",                       # Hover over nav bar before clicking
        "partial_scroll_down",             # Scroll 40% then back up
        "wait_3s",                         # Reading simulation
        "click_target"
    ],
    "proxy_type": "residential",           # Mobile proxies fool DataDome best
    "max_requests_per_min": 8             # Stay well below ML threshold
}
```

### Akamai Bot Manager
```python
AKAMAI_PROFILE = {
    "ua": "Mozilla/5.0 (X11; Linux x86_64) Chrome/121.0.0.0",
    "critical": "tls_ja3_must_match_declared_browser",
    "http2_settings": "mimic_chrome_121",  # H2 SETTINGS frames must match
    "header_order": ["Host", "User-Agent", "Accept", "Accept-Language",
                     "Accept-Encoding", "Connection"],   # Order matters for Akamai
    "cookie_reuse": True,                  # Reuse session cookies across requests
    "bypass_known_pattern": "prefetch_static_assets_first"
}
```

## 🛠️ Integration Pattern

```python
import json
import os

PATTERNS_PATH = "bypass-patterns.json"

def load_bypass_profile(anti_bot_system: str) -> dict:
    """Load the appropriate bypass profile for a detected anti-bot system."""
    profiles = {
        "cloudflare": CLOUDFLARE_PROFILE,
        "datadome": DATADOME_PROFILE,
        "akamai": AKAMAI_PROFILE
    }
    return profiles.get(anti_bot_system.lower(), {})

def log_bypass_result(platform: str, strategy: str, success: bool):
    """Self-learning: record what worked or failed for future sessions."""
    log = {}
    if os.path.exists(PATTERNS_PATH):
        with open(PATTERNS_PATH) as f:
            log = json.load(f)

    session = {
        "platform": platform,
        "strategy": strategy,
        "success": success
    }
    log.setdefault("session_lessons", []).append(session)

    with open(PATTERNS_PATH, "w") as f:
        json.dump(log, f, indent=2)

def detect_anti_bot(page_content: str) -> str:
    """Identify which anti-bot system a page uses."""
    content_lower = page_content.lower()
    if "__cf_bm" in content_lower or "cloudflare" in content_lower:
        return "cloudflare"
    elif "datadome" in content_lower or "_dd_s" in content_lower:
        return "datadome"
    elif "ak_bmsc" in content_lower or "bm_sz" in content_lower:
        return "akamai"
    return "generic_bot_wall"
```

## 📋 Workflow

1. Before any scrape: `detect_anti_bot(page_content)`
2. Load matching profile: `load_bypass_profile("cloudflare")`
3. Apply headers, delays, and session behavior
4. After attempt: `log_bypass_result(...)` → vault grows smarter each session

## 🔗 Feeds Into
- `stealth_orchestrator.py` → `bypass_retry_logic()` method
- Self-improving: every session teaches the vault
