# ADR 001 Establish a deterministic baseline before AI

Status: proposed. Author: Srini Gummalla. Date: TODO.
Context: We need an auditable reference for procurement exception triage before adding an LLM.
Option A: ask an LLM to perform all matching and decide actions.
Option B: calculate matching in deterministic code and use AI later for grounded explanation.
Option C: use standard SAP capabilities without custom AI where they meet the process need.
Proposed choice: B for the learning prototype; assess C for a real customer solution.
Reason: repeatable arithmetic, explicit scope, independently checkable results and controlled actions.
Tradeoff: more explicit rules and data preparation; the small fixture model omits many SAP cases.
Evidence: 12 learning fixtures and later measured comparison with AI assistance.
Revisit when: target SAP release, process configuration and standard capability assessment are known.

My defense in 120 words: TODO
Strongest argument against my decision: TODO
One assumption still requiring verification: TODO
