# Test script for Planner Agent
from agents.planner_agent import generate_project_plan

# File paths (relative to repo structure)
description_file = "data/project_description.txt"
timeline_file = "data/project_timeline.csv"

# Generate plan
plan = generate_project_plan(description_file, timeline_file)

# Display structured plan
for key, value in plan.items():
    print(f"{key}: {value}\n")

