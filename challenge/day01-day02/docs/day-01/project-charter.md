# Project 1 Procurement invoice exception assistant

Status: starter proposal for Srini to review and revise; no customer deployment or savings claimed.

Business problem: An AP analyst investigating an invoice mismatch must compare the purchase
order, receipts, prior invoices and policies before routing a case to the right person.
The prototype will organize this evidence and explain the proposed next step.

Business owner: AP process owner, represented as a simulated stakeholder in this portfolio.
Users: AP analyst, buyer, receiving clerk and authorized approver.
Company code: synthetic US01. Currency USD. Material unit EA. One PO item per case.
Initial exceptions: missing receipt, price difference, invoiced quantity beyond available receipts.
Normal partial receipts and prior invoicing must be handled correctly.

Days 1 and 2 deliverable: process definition, 12 synthetic cases and deterministic triage rules.
Later AI use: summarize evidence, retrieve policy and draft a recommendation with citations.
Future action boundary: approved case note or case workflow action only, subject to API verification.
Excluded: payments, autonomous invoice release, tax, freight, credit memos, service entry sheets,
currency conversion, unit conversion, goods returns and production SAP access.

Success today: classify all 12 specified learning cases and explain three decisions without AI.
Future success hypothesis: reduce analyst handling effort while preserving controls.
Baseline handling time: NOT MEASURED. Business savings: NOT MEASURED.

Constraints: existing BTP trial; no S/4HANA tenant or AI service access established.
Standard fit check: examine SAP invoice verification and reconciliation capabilities before custom AI.
Prototype architecture: JSON fixtures -> deterministic rules -> triage case -> human review.

My edits to this proposal: TODO
Why this problem fits my SAP experience: TODO
What I would ask an AP owner first: TODO
Three acceptance criteria in my own words: TODO
