# Playbook: Intelligence Logic — Signal & Memory

This manual explains how the **Intelligence Module** provides the "Cold Hard Truth" that the **Nucleus** needs to build industrial-grade strategy.

## 1. 🔍 Signal Extraction (RAG-lite)
- **Problem**: Traditional agents build on "hallucinated optimism."
- **The Intelligence Bit**: We don't just "research"; we **triangulate**.
- **Logic**: Every signal must be cross-verified across a Technical source (GitHub/Docs) and a Market source (ProductHunt/Reddit). This eliminates "Theory Fluff."

## 2. 🧠 Long-Term Memory (LTM)
- **Problem**: Agents reset every session (Amnesia).
- **The Intelligence Bit**: We use a **Persistent Knowledge Graph**.
- **Execution**: Every project decision is logged in the `memory-vault.json`. When a new session starts, the agent "remembers" your preferences and past failures.

## 3. 🛡️ The Grounding Gasket
- **Integration**: During the **Nucleus [Grounding]** phase, the Intelligence module acts as a "Gasket."
- **Constraint**: If there is no high-confidence signal for a claim, the claim is treated as a "Hypothesis" and marked for mandatory Red-Teaming.

## 📈 The Evolution Loop
1. **Signal** found (Intelligence).
2. **Strategy** built (Nucleus).
3. **Execution** happens (Systems).
4. **Result** logged (Memory).
5. **Next Strategy** gets 10% more efficient.

---
*Status: Intelligence Layer 100% Armed.*
