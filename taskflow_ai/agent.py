from ai_engine import ask_ai
import json


def plan_tasks(user_input):
    prompt = f"""
You are a strict AI agent.

Convert the user request into JSON actions.

⚠️ RULES:
- Return ONLY JSON
- Use ONLY these actions:

    open_website
    search_google
    open_app
    email_summary
    create_code
    schedule_task

❌ DO NOT use words like: search, open, play
✅ MUST use exact names above

---

Examples:

User: open youtube
[{{"action": "open_website", "target": "https://youtube.com"}}]

User: search python tutorials
[{{"action": "search_google", "target": "python tutorials"}}]

User: summarise my gmail
[{{"action": "email_summary", "target": ""}}]

---

User: {user_input}
"""

    response = ask_ai(prompt)

    try:
        tasks = json.loads(response)
        return tasks
    except:
        return [{"action": "unknown", "target": user_input}]