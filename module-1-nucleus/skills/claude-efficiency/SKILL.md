---
name: Claude Logic Efficiency (CLE)
description: A specialized skill for maximizing Claude's operational efficiency using XML-tagging, Chain-of-Thought (CoT), and standardized project structures.
---

# Claude Logic Efficiency (CLE)

Use this skill to optimize how tasks are processed, documented, and executed within a Claude-based agentic environment. This skill follows the official Anthropic "Cookbook" patterns for high-reliability outputs.

## Core Guidelines

### 1. Structural Tagging (XML)
ALWAYS wrap distinct parts of your prompt/analysis in XML tags. This helps the model delineate between background, current state, and instructions.
- `<context>`: Historical data or requirements.
- `<analysis>`: Logical evaluation of the situation.
- `<instruction>`: Exact steps to take.
- `<verification>`: Checkpoints for success.

### 2. Explicit Thinking (CoT)
Before providing a final answer or code, use a `<thought>` block to:
- Break down the user's request into atomic parts.
- Identify potential edge cases.
- Select the best tool or algorithm.
- Plan the output structure.

### 3. Artifact Utilization
When generating persistent content (Code, HTML, SVG, Markdown Reports):
- Use the **Artifacts** window-compatible formatting.
- Ensure the content is "Drop-in" ready.
- Comment code extensively using the Project's "Coding Standards".

### 4. Project Initialization Pattern
When starting a new Project or Task Folder:
1. **Define the Vision**: Create a `VISION.md`.
2. **Setup Tracking**: Initialize `task.md`.
3. **Establish Constraints**: Create a `.agents/instructions.md` for local rules.

## Examples

### Good Structural Prompting
```xml
<context>
The user wants to refactor the login module to support OAuth.
</context>

<thought>
1. Identify current auth flow.
2. Select OAuth provider (Google/GitHub).
3. Plan API changes.
</thought>

<instruction>
1. Modify /auth/login.js to include passport middleware.
2. ...
</instruction>
```

### Verification Checklist
- [ ] Are all instructions wrapped in XML?
- [ ] Is there a `<thought>` block present?
- [ ] Is the output structured for maximum readability?
- [ ] Are project-specific constraints respected?
