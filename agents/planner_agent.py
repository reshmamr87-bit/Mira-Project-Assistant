# Planner Agent for Mira
# Reads project description and timeline to generate structured plan

import pandas as pd

def generate_project_plan(description_file, timeline_file):
    # Read project description
    with open(description_file, 'r') as f:
        description = f.read()

    # Read timeline CSV
    timeline = pd.read_csv(timeline_file)

    # Generate structured plan
    plan = {
        "Project Overview": description.strip(),
        "Phases": timeline["phase"].tolist(),
        "Milestones": timeline["Milestone"].tolist(),
        "Deliverables": timeline["Deliverable"].tolist(),
        "Duration (weeks)": timeline["Duration"].tolist()
    }

    return plan

