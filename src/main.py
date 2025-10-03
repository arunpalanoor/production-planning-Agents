# src/main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.planner_agent import run

goal = "Generate a production plan for next week based on forecasted demand"
response = run(goal)

print("🧠 Planner Agent Response:")
print(response)
