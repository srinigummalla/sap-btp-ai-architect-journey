# Intelligent Goods Receipt Assistant — BTP AI evidence

Senior SAP Technical Architect (19 yrs ABAP / RAP / OData / Fiori)
building a side-by-side AI extension on SAP BTP.

## Use case
Warehouse clerk asks: what should I post for this inbound delivery?
CAP action `SuggestGRPosting` returns a suggestion.
Transactional goods receipt stays in S/4 RAP/ABAP.

## Architecture
User (Fiori / Joule)
  → CAP on BTP (`SuggestGRPosting`)
    → Destination to S/4 OData (inbound delivery facts)
    → Generative AI Hub on AI Core → Foundation Model
    → HANA Vector Engine (RAG: GR SOPs, packing docs)

Clean-core side-by-side: CAP on BTP calls Generative AI Hub for the LLM,
grounds answers with HANA Vector Engine, and exposes an OData action
that S/4 or Joule can consume. ABAP/RAP stays in the core; AI extension
lives on BTP.

## Status
- Week 1: CAP hello running in BAS (GrAssistant/Health).

## Not in this repo
Production S/4 code, secrets, service keys, vendor documents.

## SAP AI architecture foundation


[Days 1 and 2 lab](challenge/day01-day02/README.md)


Scope: environment verification, procurement process analysis,

synthetic invoice cases and a deterministic matching baseline.
