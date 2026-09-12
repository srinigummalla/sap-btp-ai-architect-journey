# sap-btp-ai-architect-journey
Srini Reddy — 19y SAP ABAP/RAP/OData/Fiori → BTP AI Architect evidence repo.
UC1: Intelligent Goods Receipt Assistant (SuggestGRPosting).
Clean-core: GR posting stays RAP/ABAP; AI suggestion is CAP on BTP.
Stack target: CAP + Generative AI Hub + HANA Vector + Joule later.
Week 1: trial + CAP stub only. GenAI Hub not entitled yet.
Trial: US East (VA) / 69b7f502trial / space dev.

## Architecture (UC1)

User (Fiori/Joule)
  → CAP on BTP (`SuggestGRPosting`)
    → Destination to S/4 OData (inbound delivery)
    → Generative AI Hub / AI Core → Foundation Model
    → HANA Vector Engine (RAG: GR SOPs, packing docs)

Clean-core: RAP/ABAP posts GR. CAP on BTP only suggests.
