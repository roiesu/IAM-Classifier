import json
import re
import requests
from config import api_config

def run_policy(prompt):
    headers = {
        "Authorization": f"Bearer {api_config.API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.2
        }
    }

    try:
        response = requests.post(api_config.API_URL, headers=headers, data=json.dumps(payload))
        response_json = response.json()

        if isinstance(response_json, list) and "generated_text" in response_json[0]:
            result_text = response_json[0]["generated_text"]
        elif isinstance(response_json, dict) and "error" in response_json:
            return False, None, f"API Error: {response_json['error']}"
        else:
            return False, None, f"Unexpected API response: {response_json}"

        match = re.search(r"\{\s*\"classification\".*?\}", result_text, re.DOTALL)
        if match:
            return True, json.loads(match.group()), result_text
        else:
            return False, None, result_text

    except Exception as e:
        return False, None, f"Exception: {str(e)}"
