import json
import hashlib
import os
import sys
from datetime import datetime

class NucleusEngine:
    """
    The Hyper-Industrial Strategic Engine Core.
    Efficiently manages state, memory, and validation for agentic reasoning.
    """
    def __init__(self, base_path="."):
        self.base_path = base_path
        self.lessons_path = os.path.join(base_path, "lessons.json")
        self.graph_path = os.path.join(base_path, "sub_graphs.json")
        self.lessons = self._load_json(self.lessons_path)
        self.graph = self._load_json(self.graph_path)
        self.trajectories = {"A": [], "B": [], "C": []}

    def _load_json(self, path):
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _save_json(self, data, path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def calculate_iteration_delta(self, prev_content, new_content):
        """Calculates information gain between refinement steps."""
        if not prev_content: return 100.0
        prev_words = set(prev_content.lower().split())
        new_words = set(new_content.lower().split())
        gain = len(new_words - prev_words) / len(prev_words) * 100 if prev_words else 100.0
        return round(gain, 2)

    def get_validation_hash(self, content):
        """Generates a semantic checksum for industrial-grade integrity."""
        return hashlib.sha256(content.strip().encode()).hexdigest()[:16]

    def log_trajectory_step(self, trajectory_id, state_id, content, notes=None):
        """Logs a step in a multi-memory trajectory with efficiency tracking."""
        v_hash = self.get_validation_hash(content)
        prev_content = self.trajectories[trajectory_id][-1]['content'] if self.trajectories[trajectory_id] else ""
        delta = self.calculate_iteration_delta(prev_content, content)
        
        step = {
            "timestamp": datetime.now().isoformat(),
            "state_id": state_id,
            "content_hash": v_hash,
            "iteration_delta": f"{delta}%",
            "notes": notes or [],
            "content": content # Keep content for delta calculation
        }
        self.trajectories[trajectory_id].append(step)
        return step

    def add_lesson(self, category, text):
        """Appends a new lesson to the persistence layer."""
        lesson_id = f"LESSON_{len(self.lessons.get('lessons', [])) + 1:03d}"
        new_lesson = {"id": lesson_id, "category": category, "text": text, "timestamp": datetime.now().isoformat()}
        self.lessons.setdefault("lessons", []).append(new_lesson)
        self._save_json(self.lessons, self.lessons_path)
        return lesson_id

    def verify_state(self, flow_name, state_id, output_content):
        """Validates that a state transition matches the nodal requirements."""
        state_desc = self.graph.get("graphs", {}).get(flow_name, {}).get(state_id)
        if not state_desc:
            return False, f"Invalid State ID: {state_id} for Flow: {flow_name}"
        
        v_hash = self.get_validation_hash(output_content)
        return True, {"state": state_desc, "validation_hash": v_hash}

    def verify_success(self, delta_threshold=20.0):
        """Checks if current reasoning flow is meeting industrial efficiency standards."""
        for tid, steps in self.trajectories.items():
            if steps and float(steps[-1]['iteration_delta'].strip('%')) < delta_threshold:
                return False, f"Efficiency Warning: Trajectory {tid} gain below {delta_threshold}% threshold."
        return True, "Efficiency check passed."

if __name__ == "__main__":
    engine = NucleusEngine()
    print("Nucleus Engine Hyper-Industrial Core v1.1 Initialized.")
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "lesson" and len(sys.argv) > 3:
            cat, text = sys.argv[2], sys.argv[3]
            print(f"Added Lesson: {engine.add_lesson(cat, text)}")
        elif cmd == "verify" and len(sys.argv) > 4:
            flow, state, content = sys.argv[2], sys.argv[3], sys.argv[4]
            success, res = engine.verify_state(flow, state, content)
            print(json.dumps(res, indent=2) if success else res)
        else:
            print("Usage: python nucleus_engine.py [lesson | verify] [args...]")
