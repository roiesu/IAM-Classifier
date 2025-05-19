import json

def load_prompt(template_text, policy):
    return template_text.replace("{{POLICY}}", json.dumps(policy, indent=2))

