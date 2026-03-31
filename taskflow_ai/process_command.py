# process_command.py

def process_command(command):
    command = command.lower()
    tasks = []

    # 📧 EMAIL SUMMARY
    if "gmail" in command or "email" in command:
        tasks.append({"action": "email_summary", "target": None})

    # 🌐 OPEN YOUTUBE
    elif "open youtube" in command:
        tasks.append({"action": "open", "target": "https://www.youtube.com"})

    # 🔍 SEARCH
    elif "search" in command:
        query = command.replace("search", "").strip()
        tasks.append({"action": "search", "target": query})

    # 💻 OPEN VS CODE
    elif "vscode" in command:
        tasks.append({"action": "open_vscode", "target": None})

    # 📅 SCHEDULE
    elif "schedule" in command:
        tasks.append({"action": "schedule", "target": command})

    # 💻 CREATE APP
    elif "create" in command or "code" in command:
        tasks.append({"action": "create_app", "target": command})

    # ❓ UNKNOWN
    else:
        tasks.append({"action": "unknown", "target": command})

    return tasks