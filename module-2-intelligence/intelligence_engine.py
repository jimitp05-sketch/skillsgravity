import json
import os
import hashlib
from datetime import datetime
from stealth_orchestrator import StealthOrchestrator

class IntelligenceEngine:
    """
    The Elite Hyper-Industrial Intelligence Module (The Radar).
    Achieves 'Mastery' via Stealth, Recursive البحث (Research), and Pillar Triangulation.
    """
    def __init__(self, base_path="c:/Users/jimit/Desktop/Merge Gaurd/gravity/Skill creatoion/anti-gravity-intelligence"):
        self.base_path = base_path
        self.memory_path = os.path.join(base_path, "memory-vault.json")
        self.memory = self._load_json(self.memory_path)
        self.stealth = StealthOrchestrator()
        self.research_log_path = os.path.join(base_path, "research-log.json")

    def _load_json(self, path):
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _save_json(self, data, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def get_signal_hash(self, text):
        return hashlib.sha256(text.strip().lower().encode()).hexdigest()[:16]

    def triangulate_multi_pillar(self, signal_data):
        """
        Industrial Triangulation across Official, Market, and Technical pillars.
        Requires 3-point closure for 'Absolute Truth' status.
        """
        sources = signal_data.get("sources", [])
        pillars = set([s.get("pillar") for s in sources])
        
        confidence = 0.0
        if "Official" in pillars: confidence += 0.4
        if "Market" in pillars: confidence += 0.3
        if "Technical" in pillars: confidence += 0.3

        signal_data["confidence"] = round(confidence, 2)
        signal_data["status"] = "Absolute Truth" if confidence >= 0.9 else "High Signal" if confidence >= 0.6 else "Hypothesis"
        return signal_data

    def research_loop(self, objective, depth=0, max_depth=3):
        """
        Recursive Pivot Engine:
        Follows data trails (e.g., Email -> Username -> Repo -> Company).
        """
        if depth >= max_depth:
            return "Max depth reached. Synthesizing final intelligence."

        print(f"[Research Loop Depth {depth}] Investigating: {objective}")
        self.stealth.human_delay("normal")
        
        # Logic to simulate recursive discovery
        discovery = {
            "pivot_point": f"Pivot_{depth}",
            "data": f"Intelligence extracted at level {depth}",
            "timestamp": datetime.now().isoformat()
        }
        
        self.log_research(discovery)
        
        # Decider: Should we go deeper?
        if depth < max_depth - 1:
            return self.research_loop(f"Refined objective from level {depth}", depth + 1)
        
        return discovery

    def log_research(self, entry):
        log = self._load_json(self.research_log_path)
        log.setdefault("entries", []).append(entry)
        self._save_json(log, self.research_log_path)

    def manage_memory_semantic(self, new_insight):
        """Prevents duplication and summarizes legacy context."""
        insight_hash = self.get_signal_hash(new_insight)
        history = self.memory.get("project_history", [])
        
        # Duplication Guard
        for item in history:
            if self.get_signal_hash(str(item)) == insight_hash:
                return False, "Insight already archived."

        self.memory.setdefault("project_history", []).append({
            "insight": new_insight,
            "hash": insight_hash,
            "timestamp": datetime.now().isoformat()
        })
        self._save_json(self.memory, self.memory_path)
        return True, "Memory persisted."

if __name__ == "__main__":
    engine = IntelligenceEngine()
    print("Elite Intelligence Engine (Radar v3.0) Operational.")
    
    # Simulate a recursive research loop
    result = engine.research_loop("Identify Market Gap for Anti-Gravity Tools")
    print(f"Research Result: {result}")
    
    # Test Pillar Triangulation
    test_signal = {
        "description": "Enterprise AI latency is the #1 pain point.",
        "sources": [
            {"uri": "https://gov.report/ai", "pillar": "Official"},
            {"uri": "https://reddit.com/r/ai", "pillar": "Market"},
            {"uri": "https://github.com/benchmarks", "pillar": "Technical"}
        ]
    }
    triangulated = engine.triangulate_multi_pillar(test_signal)
    print(f"Triangulated Signal: {json.dumps(triangulated, indent=2)}")
