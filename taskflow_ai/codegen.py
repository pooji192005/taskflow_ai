from ai_engine import chat_ai
import os

def generate_code(prompt):
    ai_prompt = f"""
Generate clean Python code for:
{prompt}

Only return code, no explanation.
"""

    code = chat_ai(ai_prompt)

    return code


def save_code(filename, code):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    return f"✅ Code saved to {filename}"


def auto_build_project(prompt):
    code = generate_code(prompt)

    filename = "generated_app.py"
    save_code(filename, code)

    return f"🚀 Project created: {filename}"