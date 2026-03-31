import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def ask_ai(user_input):
    prompt = f"""
You are a strict AI task planner.

Convert user request into VALID JSON only.

Rules:
- Output ONLY JSON
- No explanation
- Always return list []

Actions:
- open_url (target)
- search_google (target)
- open_app (target)
- summarize_email
- generate_code (prompt)
- type_text (text)
- click (x, y)
- wait (duration)

Examples:

User: open youtube
[{{"action":"open_url","target":"https://youtube.com"}}]

User: search python tutorial
[{{"action":"search_google","target":"python tutorial"}}]

User: summarize my gmail
[{{"action":"summarize_email"}}]

User: create python calculator
[{{"action":"generate_code","prompt":"python calculator app"}}]

Now:

User: {user_input}
"""

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        })

        text = response.json()["response"].strip()

        # 🔥 Clean response
        text = text.replace("```json", "").replace("```", "").strip()

        # Extract JSON safely
        start = text.find("[")
        end = text.rfind("]") + 1

        if start != -1 and end != -1:
            return text[start:end]

        return "[]"

    except:
        return "[]"


def chat_ai(prompt):
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        })

        return response.json()["response"]

    except Exception as e:
        return f"AI Error: {str(e)}"