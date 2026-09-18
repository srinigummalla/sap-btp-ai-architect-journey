# Project 1 Procurement invoice exception assistant

Version 0.1 approved as the initial project charter. This is a living document and will be revised as process, architecture and evaluation evidence develops.

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

My edits to this proposal: 
Confirmed the Accounts Payable analyst as the primary user, with the procurement buyer, receiving clerk, AP process owner and authorized approver as secondary stakeholders. The initial prototype will cover missing or unavailable goods-receipt evidence, invoice price variance and invoiced quantity exceeding the received or remaining quantity. It must correctly handle partial receipts and prior invoices. The prototype may recommend a next action, but an authorized human must approve it. It cannot post, release, block or modify an SAP invoice.

Why this problem fits my SAP experience: 
This problem combines my SAP technical experience in ABAP, S/4HANA development, CDS, RAP, OData, Fiori and enterprise integration. It allows me to apply that background to a business process while developing BTP, enterprise AI, security, governance and architecture capabilities. My SAP experience helps me understand the importance of deterministic business rules, document evidence, authorizations, exception handling and production controls.

What I would ask an AP owner first: 
Which invoice exceptions consume the most analyst time; how are they currently investigated and routed; which SAP documents, tolerances and policies determine the decision; who owns each exception type; what actions require approval; and what are the current exception volume, average handling time and resolution rate?

Three acceptance criteria in my own words: 
1.  The deterministic baseline must correctly classify all 12 agreed synthetic invoice cases, including partial receipts, prior invoices and unavailable evidence.
2.  Every result must show the relevant PO, receipt, prior-invoice, quantity and price evidence, along with the exception reason and recommended next action.
3.  The system may recommend an action, but it must not modify an SAP invoice. Missing or unavailable evidence must result in human review rather than an unsupported conclusion.
