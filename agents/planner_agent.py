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
    "Phases": timeline["phase_name"].tolist(),
    "Start Weeks": timeline["start_week"].tolist(),
    "End Weeks": timeline["end_week"].tolist(),
    "Key Activities": timeline["key_activities"].tolist(),
    "Milestones & Deliverables": timeline["milestones_deliverables"].tolist()
}


    return plan

