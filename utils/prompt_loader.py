import json

def load_prompt(template_path, policy):
    with open(template_path, "r") as f:
        template = f.read()
    return template.replace("{{POLICY}}", json.dumps(policy, indent=2))
