from agents.planner import plan
from executor import execute
from memory import add

print("🔥 LEVEL 5 AGI READY")

while True:
    user = input(">>> ")

    p = plan(user)
    print("\nPLAN:\n", p)

    res = execute(p)

    print("\nRESULTS:")
    for r in res:
        print("-", r)

    add(user, res)