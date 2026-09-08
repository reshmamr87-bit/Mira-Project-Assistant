from agents.planner_agent import generate_project_plan
from agents.risk_assessor_agent import generate_risk_matrix
from agents.status_reporter_agent import generate_status_report
from agents.milestone_tracker import MilestoneTracker
from datetime import datetime, timedelta

def main():
    # Collect report content in a string for saving later
    report_output = "\n==================== Stakeholder Report ====================\n\n"
    markdown_output = "# 📑 Stakeholder Report\n\n"

    # === Project Plan ===
    description_file = "data/project_description.txt"
    timeline_file = "data/project_timeline.csv"
    plan = generate_project_plan(description_file, timeline_file)

    report_output += "📌 Project Plan Overview\n"
    report_output += plan["Project Overview"] + "\n"
    markdown_output += "## 📌 Project Plan Overview\n"
    markdown_output += plan["Project Overview"] + "\n\n"

    for i in range(len(plan["Phases"])):
        report_output += f" Phase: {plan['Phases'][i]} | Start: {plan['Start Weeks'][i]} | End: {plan['End Weeks'][i]}\n"
        report_output += f"   Activities: {plan['Key Activities'][i]}\n"
        report_output += f"   Milestones: {plan['Milestones & Deliverables'][i]}\n\n"

        markdown_output += f"### Phase: {plan['Phases'][i]} (Week {plan['Start Weeks'][i]}–{plan['End Weeks'][i]})\n"
        markdown_output += f"- **Activities:** {plan['Key Activities'][i]}\n"
        markdown_output += f"- **Milestones:** {plan['Milestones & Deliverables'][i]}\n\n"

    # === Risk Matrix ===
    risk_file = "data/project_risks.csv"
    risks = generate_risk_matrix(risk_file)

    report_output += "\n⚠️ Risk Assessment\n"
    markdown_output += "## ⚠️ Risk Assessment\n\n"

    for i in range(len(risks["Risk ID"])):
        report_output += f" {risks['Risk ID'][i]} ({risks['Category'][i]})\n"
        report_output += f"   Challenge: {risks['Challenge'][i]}\n"
        report_output += f"   Impact: {risks['Impact'][i]}\n"
        report_output += f"   Mitigation: {risks['Mitigation Strategy'][i]}\n\n"

        markdown_output += f"### {risks['Risk ID'][i]} ({risks['Category'][i]})\n"
        markdown_output += f"- **Challenge:** {risks['Challenge'][i]}\n"
        markdown_output += f"- **Impact:** {risks['Impact'][i]}\n"
        markdown_output += f"- **Mitigation:** {risks['Mitigation Strategy'][i]}\n\n"

    # === Status Report ===
    task_file = "data/sample_task_board.csv"
    report = generate_status_report(task_file)

    report_output += "📊 Current Task Status\n"
    markdown_output += "## 📊 Current Task Status\n\n"

    for i in range(len(report["Task ID"])):
        report_output += f" {report['Task ID'][i]} | {report['Task Name'][i]}\n"
        report_output += f"   Status: {report['Status'][i]}, Assignee: {report['Assignee'][i]}, Priority: {report['Priority'][i]}\n"
        report_output += f"   Sprint: {report['Sprint'][i]}, Due: {report['Due Date'][i]}\n"
        report_output += f"   Labels: {report['Labels'][i]}\n\n"

        markdown_output += f"### {report['Task ID'][i]} | {report['Task Name'][i]}\n"
        markdown_output += f"- **Status:** {report['Status'][i]}\n"
        markdown_output += f"- **Assignee:** {report['Assignee'][i]}\n"
        markdown_output += f"- **Priority:** {report['Priority'][i]}\n"
        markdown_output += f"- **Sprint:** {report['Sprint'][i]}\n"
        markdown_output += f"- **Due Date:** {report['Due Date'][i]}\n"
        markdown_output += f"- **Labels:** {report['Labels'][i]}\n\n"

    # === Summary Insights ===
    completed = report["Status"].count("Done")
    in_progress = report["Status"].count("In Progress")
    blocked = report["Status"].count("Blocked")
    to_do = report["Status"].count("To Do")

    report_output += "\n📈 Summary Insights\n"
    report_output += f" - Completed tasks: {completed}\n"
    report_output += f" - In Progress tasks: {in_progress}\n"
    report_output += f" - Blocked tasks: {blocked}\n"
    report_output += f" - Remaining To Do: {to_do}\n"

    markdown_output += "## 📈 Summary Insights\n"
    markdown_output += f"- Completed tasks: {completed}\n"
    markdown_output += f"- In Progress tasks: {in_progress}\n"
    markdown_output += f"- Blocked tasks: {blocked}\n"
    markdown_output += f"- Remaining To Do: {to_do}\n\n"

    markdown_output += "### Top Risks to Monitor\n"
    for i in range(3):  # show first 3 risks
        report_output += f" {risks['Risk ID'][i]} - {risks['Category'][i]}: {risks['Challenge'][i]}\n"
        markdown_output += f"- {risks['Risk ID'][i]} - {risks['Category'][i]}: {risks['Challenge'][i]}\n"

    # === Upcoming Deadlines (next 7 days) ===
    report_output += "\n⏰ Upcoming Deadlines (next 7 days)\n"
    markdown_output += "\n## ⏰ Upcoming Deadlines (next 7 days)\n\n"

    today = datetime.today()
    next_week = today + timedelta(days=7)

    for i in range(len(report["Task ID"])):
        try:
            due_date = datetime.strptime(report["Due Date"][i], "%Y-%m-%d")
            if today <= due_date <= next_week:
                report_output += f" {report['Task ID'][i]} | {report['Task Name'][i]} (Due: {report['Due Date'][i]})\n"
                report_output += f"   Status: {report['Status'][i]}, Assignee: {report['Assignee'][i]}, Priority: {report['Priority'][i]}\n\n"

                markdown_output += f"### {report['Task ID'][i]} | {report['Task Name'][i]} (Due: {report['Due Date'][i]})\n"
                markdown_output += f"- **Status:** {report['Status'][i]}\n"
                markdown_output += f"- **Assignee:** {report['Assignee'][i]}\n"
                markdown_output += f"- **Priority:** {report['Priority'][i]}\n\n"
        except Exception:
            continue

    # === Critical Alerts ===
    report_output += "\n🚨 Critical Alerts\n"
    report_output += "Blocked Tasks:\n"
    markdown_output += "## 🚨 Critical Alerts\n\n### Blocked Tasks\n"

    for i in range(len(report["Task ID"])):
        if report["Status"][i] == "Blocked":
            report_output += f" {report['Task ID'][i]} | {report['Task Name'][i]} (Assignee: {report['Assignee'][i]}, Due: {report['Due Date'][i]})\n"
            markdown_output += f"- {report['Task ID'][i]} | {report['Task Name'][i]} (Assignee: {report['Assignee'][i]}, Due: {report['Due Date'][i]})\n"

    report_output += "\nHigh-Priority Risks:\n"
    markdown_output += "\n### High-Priority Risks\n"

    for i in range(len(risks["Risk ID"])):
        report_output += f" {risks['Risk ID'][i]} - {risks['Category'][i]}: {risks['Challenge'][i]}\n"
        markdown_output += f"- {risks['Risk ID'][i]} - {risks['Category'][i]}: {risks['Challenge'][i]}\n"

    # === Milestone Alerts ===
    tracker = MilestoneTracker()
    upcoming = tracker.upcoming_milestones()
    risks_m = tracker.at_risk_milestones()

    report_output += "\n📅 Milestone Alerts\n"
    markdown_output += "\n## 📅 Milestone Alerts\n\n"

    report_output += "\nUpcoming Milestones (next 2 weeks):\n"
    markdown_output += "### Upcoming Milestones (next 2 weeks)\n"
    for m in upcoming:
        report_output += f"- {m['milestone']} (Due: {m['due_date']}, Status: {m['status']})\n"
    for m in upcoming:
        report_output += f"- {m['milestone']} (Due: {m['due_date']}, Status: {m['status']})\n"
        markdown_output += f"- {m['milestone']} (Due: {m['due_date']}, Status: {m['status']})\n"

    report_output += "\nAt-Risk Milestones:\n"
    markdown_output += "\n### At-Risk Milestones\n"
    for r in risks_m:
        report_output += f"- {r['milestone']} (Due: {r['due_date']}, Status: {r['status']})\n"
        markdown_output += f"- {r['milestone']} (Due: {r['due_date']}, Status: {r['status']})\n"

    # === End of Report ===
    report_output += "\n==================== End of Report ====================\n"
    markdown_output += "\n---\n\n_End of Report_\n"

    # Print to terminal
    print(report_output)

    # Save to text file
    with open("stakeholder_report.txt", "w", encoding="utf-8") as f:
        f.write(report_output)

    # Save to Markdown file
    with open("stakeholder_report.md", "w", encoding="utf-8") as f:
        f.write(markdown_output)

    print("📂 Reports saved to stakeholder_report.txt and stakeholder_report.md")

if __name__ == "__main__":
    main()
