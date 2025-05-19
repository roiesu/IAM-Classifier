import os
import json
from config.constants import EXAMPLES_DIR, PROMPT_PATH
from utils.prompt_loader import load_prompt
from utils.policy_runner import run_policy
from utils.result_writer import write_session_log

results = []

with open(PROMPT_PATH, "r") as f:
    prompt_template = f.read()

for filename in sorted(os.listdir(EXAMPLES_DIR)):
    if not filename.endswith(".json"):
        continue

    with open(os.path.join(EXAMPLES_DIR, filename)) as f:
        policy = json.load(f)

    prompt = load_prompt(prompt_template, policy)
    success, result_json, raw = run_policy(prompt)

    result_entry = {
        "input_file": filename,
        "success": success
    }

    if success:
        result_entry.update({
            "policy": policy,
            **result_json
        })
    else:
        result_entry["raw_output"] = raw

    results.append(result_entry)

write_session_log(prompt_template, results)
