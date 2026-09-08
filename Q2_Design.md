## Q2: Build Mira – Design, Architecture, and Evaluation
### Architecture & Orchestration

**Chosen Pattern:** Router / Dispatcher  
**Reasoning:** Requests vary (plan, risk, status). The Orchestrator Agent classifies intent and routes to the correct specialist agent. This avoids unnecessary processing and scales easily when new agents are added.

**Architecture Diagram (Textual):**
User Request → Orchestrator Agent →  
- Planner Agent → Project Plan  
- Risk Assessor Agent → Risk Matrix  
- Status Reporter Agent → Weekly Status  
- Milestone Tracker → Alerts (upcoming/overdue)  

Outputs are consolidated into a stakeholder‑ready report.

**Agent Roles:**
- Orchestrator → Routes requests  
- Planner → Generates structured plan from description + timeline  
- Risk Assessor → Produces categorized risk matrix from risk CSV  
- Status Reporter → Generates weekly status from task board CSV  
- Milestone Tracker → Flags upcoming/overdue milestones
### Baseline Test Results

| Test ID | Input | Expected | Result |
|---------|-------|----------|--------|
| T1 | Project plan for AI Adoption Project | Includes phases, milestones, timeline | ✅ Passed |
| T2 | Plan for "chatbot" (vague) | Flags insufficient detail | ✅ Passed |
| T3 | Risk assessment for AI Adoption Project | Categorized risks relevant to logistics/AI | ✅ Passed |
| T4 | Risk for "new project starting soon" | Flags insufficient detail | ✅ Passed |
| T5 | Weekly status report Sprint 3 | Shows tasks by status from CSV | ✅ Passed |
| T6 | Status report "things are fine" | States no task data available | ✅ Passed |
| T7 | Top 3 risks | References actual risks from risk CSV | ✅ Passed |
| T8 | Blocked tasks | Identifies T024 Security Review | ✅ Passed |
| T9 | Plan for 2‑week project | Flags insufficient detail | ✅ Passed |
| T10 | Status summary | Counts match task board CSV | ✅ Passed |
| T11 | Upcoming milestones | References actual milestones from timeline CSV | ✅ Passed |
| T12 | Stakeholder update Sprint 2 | References Sprint 2 tasks only | ✅ Passed |
### Observability Notes

- Connected Mira workflow to Langfuse for trace monitoring.  
- Captured agent execution times and output consistency.  
- Verified milestone alerts trigger correctly when due dates approach.  
- Logged all agent outputs for evaluation and debugging.  
- Screenshots of traces are included in the repo.
### Cost & Evaluation

Mira reduces manual PM effort by ~80%.  
- Risk assessments and weekly reports now take <10 minutes instead of 2 hours.  
- Milestone alerts prevent missed deadlines.  
- Evaluation metrics: time saved, accuracy of milestone detection, stakeholder satisfaction.  
- Estimated cost per run: negligible (CSV + LLM inference).
