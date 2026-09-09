## Q4: Reflection – Mira Capstone
### Findings
Building Mira demonstrated that multi‑agent orchestration can significantly reduce manual PM effort. Each agent performed well when grounded in CSV inputs, and milestone alerts added real value by preventing missed deadlines.

### Improvement Plan
Future iterations should improve:
- Handling of vague or incomplete inputs (e.g., “new project starting soon”)  
- More robust CSV validation to avoid formatting errors  
- Enhanced stakeholder reporting with charts/visuals

### Evaluation & Fine‑Tuning
Baseline tests (T1–T12) showed consistent accuracy. Fine‑tuning could focus on:
- Better classification in the Orchestrator Agent  
- Domain‑specific risk libraries for logistics and AI projects  
- Optimizing cost by reducing redundant LLM calls

### Privacy Considerations
All outputs were grounded in project files only. No external sensitive data was used. Future rollout must ensure compliance with data privacy policies and restrict access to project datasets.

### Rollout Reflection
Pilot rollout to 10 PMs/TPMs at Nexora will validate adoption. Early feedback suggests strong potential for scaling across teams, provided observability and evaluation are maintained.
