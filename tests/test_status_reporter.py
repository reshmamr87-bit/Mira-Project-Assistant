from agents.status_reporter_agent import generate_status_report

task_file = "data/sample_task_board.csv"
report = generate_status_report(task_file)

print("Task ID:", report["Task ID"])
print("Task Name:", report["Task Name"])
print("Status:", report["Status"])
print("Assignee:", report["Assignee"])
print("Priority:", report["Priority"])
print("Sprint:", report["Sprint"])
print("Due Date:", report["Due Date"])
print("Labels:", report["Labels"])
print("Description:", report["Description"])
