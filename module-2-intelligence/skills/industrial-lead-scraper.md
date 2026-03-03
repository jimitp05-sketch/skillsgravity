---
name: industrial-lead-scraper
description: Specialized skill for industrial-level lead scraping and data extraction with high reliability and anti-detection.
---

# Minor Skill: Industrial Lead Scraper

Use this skill when the objective requires gathering business intelligence, contact leads, or market data at scale.

## 🛠️ Step-by-Step Protocol

### 1. Target Mapping
- **Action**: Define the "Lead Profile" (Industry, Location, Seniority).
- **Tooling**: Use `anti-gravity-intelligence` search strings to identify top directories (LinkedIn, Clutch, Apollo, etc.).

### 2. Scraping Strategy
- **Action**: Select the extraction method:
    - **Browser Automation**: For complex, JS-heavy sites.
    - **HTTP Requests**: For fast, API-like extraction.
    - **SERP Extraction**: Gathering leads directly from search engine results.

### 3. Data Integrity & Cleaning
- **Action**: Validate extracted emails/phones.
- **Action**: Deduplicate based on domain or company name.
- **Output**: A structured CSV/JSON file in `/data/leads/[date]-leads.csv`.

### 4. Anti-Detection Measures
- **Action**: Rotate User-Agents and introduce randomized delays.
- **Goal**: 100% success rate without IP blocking.

## 🏁 Exit Condition
- **REQUIRED**: Verified lead list ready for `anti-gravity-marketing`.
