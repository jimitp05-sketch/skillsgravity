---
name: talent-flow-analyst
description: Track who competitors are hiring, losing, and promoting. Talent flow is the most honest signal of a company's strategic direction — people follow where money and vision go.
version: 1.0.0
---

# Talent Flow Analyst

> "Show me a company's org chart and I'll show you their strategy." — CEO mindset

Hiring patterns are the most honest data a company produces. They can't fake a job posting. Every hire reveals a bet — every departure reveals a crack.

## 🧠 The Talent Signal Matrix

| Hiring Pattern | Strategic Interpretation |
|---|---|
| 5+ ML Engineers in 3 months | AI pivot — product rewrite incoming |
| "Head of Sales" hire | Moving from PLG → sales-led growth |
| "Head of Partnerships" hire | Can't grow organically — ecosystem play |
| "VP of Enterprise" hire | Moving upmarket — SMB is struggling |
| CTO departure | Technical debt crisis OR founder conflict |
| CMO departure | Brand/messaging problems OR revenue miss |
| Chicago/NYC office opening | Enterprise sales push into Fortune 500 belt |
| Mass layoffs (Glassdoor reviews spike) | Burn rate emergency or strategic pivot |
| Intern-heavy hiring | Cost-cutting after missed milestone |

## 🛠️ Integration Pattern

```python
import requests
from datetime import datetime

def get_linkedin_jobs(company: str, keywords: list[str]) -> list[dict]:
    """
    Scrape LinkedIn job listings via Google dorks.
    Returns structured job signal data.
    """
    jobs = []
    for kw in keywords:
        dork = f'site:linkedin.com/jobs "at {company}" "{kw}"'
        jobs.append({
            "keyword": kw,
            "dork": dork,
            "instruction": "Count results. Compare to 30-day cache. Growth % = hiring velocity signal."
        })
    return jobs

def classify_hiring_signals(job_counts: dict) -> dict:
    """
    Input: {"ML Engineer": 8, "Account Executive": 2, "CTO": 0}
    Output: classified strategic interpretation
    """
    signals = []
    if job_counts.get("ML Engineer", 0) + job_counts.get("Data Scientist", 0) > 5:
        signals.append("AI PIVOT — heavy model investment")
    if job_counts.get("Account Executive", 0) > 3:
        signals.append("SALES SCALE — PLG to sales-led shift")
    if job_counts.get("Enterprise", 0) + job_counts.get("VP Sales", 0) > 2:
        signals.append("UPMARKET MOVE — enterprise push")
    if job_counts.get("Intern", 0) > job_counts.get("Senior", 0):
        signals.append("COST PRESSURE — replacing senior with junior")
    return {
        "strategic_signals": signals,
        "pillar": "Market",
        "confidence_boost": 0.2,
        "timestamp": datetime.now().isoformat()
    }

def scan_glassdoor_sentiment(company_name: str) -> dict:
    """
    Check Glassdoor review velocity and rating trend.
    Sudden negative spike = retention crisis.
    """
    dork = f'site:glassdoor.com "{company_name}" review 2024 OR 2025'
    return {
        "dork": dork,
        "instruction": "Extract rating average from snippets. <3.5 = cultural crisis. >4.5 = retention is strong (hard to compete on talent).",
        "pillar": "Market"
    }

# Full talent flow analysis
def analyze_talent_flow(competitor: str) -> dict:
    role_categories = [
        "ML Engineer", "Data Scientist", "Account Executive",
        "Enterprise", "VP Sales", "Head of Marketing",
        "Senior Engineer", "Intern", "Chief", "Head of"
    ]
    job_signals = get_linkedin_jobs(competitor, role_categories)
    glassdoor = scan_glassdoor_sentiment(competitor)
    
    return {
        "competitor": competitor,
        "job_signals": job_signals,
        "glassdoor_check": glassdoor,
        "instruction": "After manual count, call classify_hiring_signals() with results"
    }
```

## 📋 CEO Workflow

1. Run `analyze_talent_flow("CompetitorName")` weekly
2. Classify signals → update Nucleus context
3. **If ML spike detected** → accelerate AI feature development NOW (6-9 month head start eroding)
4. **If CTO departed** → contact their top engineers on LinkedIn — talent acquisition opportunity

## 🔗 Feeds Into
- **Market Pillar** (+0.20)
- Nucleus: "Competitor is going sales-led — our PLG advantage window is 12-18 months"
