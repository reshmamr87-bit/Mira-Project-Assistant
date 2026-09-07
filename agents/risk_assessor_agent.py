# Risk Assessor Agent for Mira
# Reads project risks CSV to generate structured risk matrix

import pandas as pd

def generate_risk_matrix(risk_file):
    df = pd.read_csv(risk_file)

    risks = {
        "Risk ID": df["risk_id"].tolist(),
        "Category": df["category"].tolist(),
        "Challenge": df["risk_challenge"].tolist(),
        "Impact": df["impact"].tolist(),
        "Mitigation Strategy": df["mitigation_strategy"].tolist()
    }

    return risks
