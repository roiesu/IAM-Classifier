import json
import os
from datetime import datetime
from config.constants import RUNS_DIR

def write_session_log(prompt, results):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    os.makedirs(RUNS_DIR, exist_ok=True)
    session_path = os.path.join(RUNS_DIR, f"session_{timestamp}.json")
    session_data = {
        "prompt": prompt.strip(),
        "examples": results
    }
    with open(session_path, "w") as f:
        json.dump(session_data, f, indent=2)
    print(f"✅ Session saved to: {session_path}")
    
def write_submission_results(results):
    os.makedirs("final_results", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    final_path = os.path.join("final_results", f"session_{timestamp}.json")

    formatted_results = []
    for result in results:
        if result.get("success") and "policy" in result:
            formatted_results.append({
                "policy": result["policy"],
                "classification": result["classification"],
                "reason": result["reason"]
            })
        elif "policy" in result:
            formatted_results.append({
                "policy": result["policy"],
                "error": "Could not extract classification",
                "raw_output": result.get("raw_output", "No output available")
            })

    with open(final_path, "w") as f:
        json.dump(formatted_results, f, indent=2)

    print(f"📦 Final submission file saved to: {final_path}")
