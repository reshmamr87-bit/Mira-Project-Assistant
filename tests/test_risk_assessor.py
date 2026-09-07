from agents.risk_assessor_agent import generate_risk_matrix

risk_file = "data/project_risks.csv"   # ✅ point to the data folder
risks = generate_risk_matrix(risk_file)

print("Risk ID:", risks["Risk ID"])
print("Category:", risks["Category"])
print("Challenge:", risks["Challenge"])
print("Impact:", risks["Impact"])
print("Mitigation Strategy:", risks["Mitigation Strategy"])
