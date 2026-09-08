# 🏗️ Mira Project Assistant Architecture

## 📌 Overview
Mira Project Assistant is an **Agentic AI system** composed of multiple specialized agents that collaborate to deliver stakeholder‑ready outputs.  
The architecture is modular, allowing each agent to focus on a specific responsibility while contributing to the overall workflow.

---

## 🔄 Agent Flow

1. **Planner Agent**
   - Input: Project goals and requirements.
   - Output: Structured project plan and timeline.
   - Passes plan details to Risk Assessor.

2. **Risk Assessor Agent**
   - Input: Project plan from Planner Agent.
   - Output: Identified risks and mitigation strategies.
   - Passes risk insights to Status Reporter.

3. **Status Reporter Agent**
   - Input: Project plan + risk assessment.
   - Output: Consolidated stakeholder report (progress, risks, next steps).
   - Saves report in `.txt` and `.md` formats.

---

## 📂 Data Flow Diagram

User → mira_main.py → Planner Agent → Risk Assessor Agent → Status Reporter Agent → Stakeholder Report

---

## ⚙️ Components

- **mira_main.py** → Entry point, orchestrates agent execution.
- **agents/** → Contains Planner, Risk Assessor, and Status Reporter modules.
- **tests/** → Unit tests for validating agent outputs.
- **docs/** → Documentation (`README.md`, `ARCHITECTURE.md`).
- **reports/** → Auto‑generated stakeholder reports (ignored in Git).

---

## 📈 Benefits of Agentic Design
- **Autonomy**: Agents act toward defined outcomes without micromanagement.
- **Modularity**: Each agent can be improved independently.
- **Scalability**: New agents (e.g., Budget Tracker, Communication Agent) can be added easily.
- **Stakeholder‑Ready Outputs**: Reports are generated automatically in professional formats.
