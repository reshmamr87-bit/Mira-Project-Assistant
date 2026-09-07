import pandas as pd

def generate_status_report(task_file):
    df = pd.read_csv(task_file)

    report = {
        "Task ID": df["task_id"].tolist(),
        "Task Name": df["task_name"].tolist(),
        "Status": df["status"].tolist(),
        "Assignee": df["assignee"].tolist(),
        "Priority": df["priority"].tolist(),
        "Sprint": df["sprint"].tolist(),
        "Due Date": df["due_date"].tolist(),
        "Labels": df["labels"].tolist(),
        "Description": df["description"].tolist()
    }

    return report
