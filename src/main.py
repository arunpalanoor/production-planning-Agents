# src/main.py

from src.agents.planner_agent import run

goal = "Generate a production plan for next week based on forecasted demand"
response = run(goal)

print("🧠 Planner Agent Response:")
print(response)
