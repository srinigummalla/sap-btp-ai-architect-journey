# Standard SAP versus rules and AI

| Need | Preferred responsibility | Why | What I must verify |
|---|---|---|---|
| Invoice posting and payment controls | Standard SAP | Business system controls remain authoritative | Product release and configuration |
| Quantity and price comparison | Deterministic rule or standard SAP | Repeatable calculation | Real tolerances and PO settings |
| Current PO receipts and invoice status | Released SAP API later | Current facts must be fetched | Suitable API and permission |
| Policy explanation | RAG plus LLM later | Grounded language support | Policy source ownership and retrieval permissions |
| Next step recommendation | Rules plus evidence grounded AI | Explain the case and unknowns | Evaluation and human review |
| Payment execution | Existing finance process | Outside this prototype | No action tool provided |

SAP has invoice verification and GR/IR reconciliation capabilities. Read the linked SAP sources
in the guide and explain what your proposal adds before writing a custom replacement.
An invoice exception before posting and an open GR/IR balance after posting are related
but distinct cases. Do not collapse them into the same workflow.

My 150 word architecture explanation: TODO
Two cases where AI is unnecessary: TODO
One case where AI could help without deciding the financial action: TODO
