# 🔐 IAM Policy Classifier using LLM

This project classifies AWS IAM policies as either **"Weak"** or **"Strong"**, based on their structure, scope, and security conditions.

The classification is performed using an open-source language model (Zephyr 7B via Hugging Face Inference API), guided by a carefully crafted prompt.

---

## 📁 Project Structure

```
IAM-Classifier/
│
├── main.py                  # Main execution script
│
├── config/                  # Configuration files
│   ├── api_config.py        # Hugging Face API URL + token placeholder
│   └── constants.py         # Folder paths
│
├── utils/                   # Utility functions
│   ├── prompt_loader.py     # Loads prompt and injects policy
│   ├── policy_runner.py     # Sends prompt to model, parses response
│   └── result_writer.py     # Saves session logs and results
│
├── prompts/
│   └── base_prompt.txt      # Current prompt used to guide the model
│
├── example_policies/        # Test IAM policy files (.json)
│
└── runs/                    # Auto-generated logs per session
```

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install requests
```

### 2. Insert Your Hugging Face Token
Edit `config/api_config.py` and replace:
```python
API_TOKEN = "PASTE_YOUR_TOKEN_HERE"
```
Alternatively, use an environment variable for security:
```python
import os
API_TOKEN = os.getenv("HF_API_TOKEN")
```

### 3. Add Example Policies
Put `.json` files into `example_policies/`. Each file should contain a single IAM policy object.

### 4. Run the Classifier
```bash
python main.py
```

### 5. View Results
- Logs are saved in `runs/session_<timestamp>.json`
- Each log includes:
  - Input file name
  - Whether the format was valid (`success`)
  - Classification result
  - Model's reasoning
  - Raw output if failed

---

## 🧠 Prompt Engineering

### Example Prompt Logic:
- **Weak**:
  - `Action: "*"`, `Resource: "*"`, or overly broad (`s3:*`, `ec2:*`)
  - `NotAction`, `NotResource`, or meaningless conditions (`SecureTransport`)
- **Strong**:
  - Precise actions & scoped resources
  - Conditions like `MFA`, `tags`, `region`, `Deny` for reducing scope

You can refine the prompt in `prompts/base_prompt.txt` and rerun the tests to measure impact.

---

## 🧪 Evaluation Strategy

1. Run a fixed set of known policies (Weak/Strong/Borderline)
2. Log both structural success (`success = True`) and semantic correctness
3. Analyze failures → Improve prompt → Re-test
4. Track improvements across prompt versions via session files

---

## 🔒 Push Protection Tip

Do **not** commit your Hugging Face token.
Add this to `.gitignore`:
```
config/api_config.py
```

---

## 👤 Author

Roie S.  
Bar-Ilan University | Computer Science  
2025

