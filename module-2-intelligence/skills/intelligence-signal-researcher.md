---
name: intelligence-signal-researcher
description: Elite skill for extracting "High-Signal" market and technical data to ground strategic brainstorming.
---

# Skill: Intelligence Signal Researcher

This skill is the "Eyes" of the Anti-Gravity engine. It transforms raw web data into "Strategic Signals" that the Nucleus uses to validate trajectories.

## 🛠️ The Operational Protocol

### 1. [Scan] Multi-Source OSINT
- **Action**: Use `search_web` and `read_url_content` to find 3-5 distinct sources for the objective.
- **Sources**: GitHub (Technical), ProductHunt/Reddit (User Desire), Statista/News (Market).

### 2. [Extract] Signal vs. Noise Filter
- **Logic**: Remove generic marketing fluff. Extract only "Hard Signals":
  - **Pricing Power**: How much are people actually paying?
  - **Technical Limit**: What is the current state of API / Hardware limits?
  - **Sentiment Delta**: What is the #1 complaint about current solutions?

### 3. [Validate] Triangulation
- **Logic**: A signal is only "High" if confirmed by 2+ independent sources.
- **Output**: JSON object containing:
  ```json
  {
    "signal_id": "ST-001",
    "type": "Technical",
    "description": "API X has a 500ms latency floor.",
    "confidence": 0.9,
    "source_uris": ["url1", "url2"]
  }
  ```

### 4. [Ground] Nucleus Handoff
- **Action**: Present the signals as "Immutable Constraints" to the Nucleus Module.
- **Success Criteria**: If the Nucleus strategy ignores a High Signal, it must be rejected.

---

## ⚡ Technical Optimization
- **Token Reduction**: Summarize web content into Bullet Points before extraction.
- **Caching**: Store repetitive technical signals in `intelligence-signals.json`.

---
*Powered by the [Anti-Gravity Intelligence Layer]().*
