import tkinter as tk
import threading
from ai_engine import ask_ai
from executor import execute
from voice import listen_voice


def run_ai():
    user_input = entry.get()

    output.insert("end", f"\n🧑 You: {user_input}\n")

    plan = ask_ai(user_input)
    output.insert("end", f"🧠 Plan: {plan}\n")

    result = execute(plan)
    output.insert("end", f"⚙️ Result:\n{result}\n")

    output.see("end")


def run_voice():
    def task():
        text = listen_voice()

        entry.delete(0, tk.END)
        entry.insert(0, text)

        run_ai()

    threading.Thread(target=task).start()


# UI Setup
root = tk.Tk()
root.title("🔥 LEVEL 5 AI Assistant")
root.geometry("600x500")

entry = tk.Entry(root, width=60)
entry.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="▶ Run", command=run_ai).pack(side="left", padx=5)
tk.Button(frame, text="🎤 Speak", command=run_voice).pack(side="left", padx=5)

output = tk.Text(root, height=25, width=75)
output.pack(pady=10)

output.insert("end", "🚀 LEVEL 5 AGI READY\nType or Speak your command...\n")

root.mainloop()