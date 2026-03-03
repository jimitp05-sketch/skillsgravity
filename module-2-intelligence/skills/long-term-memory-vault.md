---
name: long-term-memory-vault
description: Manages persistent project context and user preferences to prevent amnesia and generic output.
---

# Skill: Long-Term Memory Vault

This skill ensures that the Anti-Gravity engine "remembers" you. It prevents the agent from asking the same questions or proposing the same failed ideas.

## 🛠️ The Operational Protocol

### 1. [Load] Context Hydration
- **Action**: Read the `memory-vault.json` file.
- **Logic**: Load "User Preferences" (Tone, Budget, Tech Stack) and "Historical Failures."

### 2. [Update] Incremental Learning
- **Logic**: After every session, identify NEW insights:
  - "User hated the subscription model approach."
  - "User prefers Python/FastAPI over Node.js."
- **Action**: Use `multi_replace_file_content` to update the vault.

### 3. [Prune] Relevance Filter
- **Logic**: If the memory-vault exceeds 50k tokens, summarize "Old" projects into single-line "Legacy" entries.
- **Why**: Keeps the active window optimized for current projects.

### 4. [Recall] Proactive Injection
- **Logic**: If the Nucleus proposes a tech stack the user historically dislikes, inject a `WARNING: User Preference Conflict`.

---

## 💾 Vault Schema
```json
{
  "user_profile": {
    "anti_patterns": [],
    "preferred_stacks": []
  },
  "project_history": [
    {
      "name": "Project X",
      "core_decisions": [],
      "failed_paths": []
    }
  ]
}
```

---
*The Memory of the [Anti-Gravity Intelligence Layer]().*
