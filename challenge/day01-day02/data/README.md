# Synthetic procurement data

Read cases.json for input. Keep expected_results.json closed until manual analysis is finished.
There are 12 independent snapshots, not consecutive events for the same PO.
No real suppliers, business data or credentials are present.
Every receipt list is complete for that snapshot, except null means unknown.
An empty list means the lookup succeeded and found no receipts.
Prior invoice quantity excludes the invoice currently being analyzed.
All units are EA and prices are per one EA. Tax, freight, returns, cancellations,
multiple PO items and production invoice blocking behavior are excluded.

Use this as a learning baseline. Do not train on these cases and later describe them as
an unseen evaluation set. A separate held-out dataset will be created later in the program.
