---
name: industrial-lead-scraper-pro
description: Industrial-grade lead extraction and scraping engine. handles anti-detection, multi-threading, and data validation at scale.
---

# Minor Skill: Industrial Lead Scraper Pro

This is the primary extraction tool for the **Intelligence** module. Use it to build high-value lead lists and competitor databases.

## 🛠️ The Extraction Logic

### 1. Target Discovery
- **Action**: Use advanced Google Search/Dorking to find "Lead Islands" (Directories, LinkedIn Lists, Portfolio sites).
- **Skill**: Use `deep-surfing` to filter for the highest quality sources.

### 2. Scraping Execution
- **Strategy**:
    - **Dynamic Content**: Use browser automation (Playwright/Puppeteer style) when JS is required.
    - **Fast Extraction**: Direct HTTP requests for static data.
- **Rules**: Randomized delays and User-Agent rotation are mandatory.

### 3. Lead Enrichment
- **Action**: Automatically find missing data (e.g., if you have a name/company, find the email).
- **Validation**: Ping SMTP servers to verify email existence without sending a message.

### 4. Output Storage
- **Path**: `/data/leads/[industry]-[date].json`
- **Output**: Cleaned, deduplicated, and verified lead set.

---
*Created for the [Anti-Gravity Intelligence]().*
