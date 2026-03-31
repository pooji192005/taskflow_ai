import json
import os

MEMORY_FILE = "memory.json"

def load():
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

            # ensure it's always a list
            if isinstance(data, list):
                return data
            else:
                return []

    except:
        return []

def save(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add(entry):
    data = load()
    data.append(entry)
    save(data)

def context():
    data = load()
    return data[-5:]   # now safe ✅