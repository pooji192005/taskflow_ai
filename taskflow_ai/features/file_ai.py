import os

def create(name, content=""):
    with open(name, "w") as f:
        f.write(content)
    return f"Created {name}"

def read(name):
    return open(name).read() if os.path.exists(name) else "Not found"

def edit(name, content):
    with open(name, "a") as f:
        f.write("\n" + content)
    return f"Edited {name}"