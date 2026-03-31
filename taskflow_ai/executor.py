import json
import webbrowser
import subprocess
import pyautogui
import time


def execute(plan):
    try:
        tasks = json.loads(plan)

        if not tasks:
            return "⚠️ No valid plan generated"

        results = []

        for task in tasks:
            action = task.get("action")

            if action == "open_url":
                webbrowser.open(task.get("target"))
                results.append("🌐 Opened URL")

            elif action == "search_google":
                query = task.get("target")
                webbrowser.open(f"https://www.google.com/search?q={query}")
                results.append(f"🔍 Searched {query}")

            elif action == "open_app":
                subprocess.Popen(task.get("target"))
                results.append("🖥️ App opened")

            elif action == "summarize_email":
                from features.email_ai import summarize_email
                results.append(summarize_email())

            elif action == "generate_code":
                from codegen import auto_build_project
                results.append(auto_build_project(task.get("prompt")))

            elif action == "type_text":
                pyautogui.write(task.get("text", ""), interval=0.05)
                results.append("⌨️ Typed text")

            elif action == "click":
                x = task.get("x", 500)
                y = task.get("y", 500)
                pyautogui.click(x, y)
                results.append("🖱️ Clicked")

            elif action == "wait":
                time.sleep(task.get("duration", 2))
                results.append("⏳ Waited")

            else:
                results.append(f"❓ Unknown action: {action}")

        return "\n".join(results)

    except Exception as e:
        return f"❌ Execution error: {str(e)}"