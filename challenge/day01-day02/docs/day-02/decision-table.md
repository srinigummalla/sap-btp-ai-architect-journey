# Deterministic triage decision table

Lab policy version 1: exact price comparison, zero price tolerance, no currency or unit conversion.
These are invented teaching rules and must not be described as SAP defaults.
MATCH means no mismatch found by this model; it never means approved for payment.

Apply in this order:

1. If invoice quantity <= 0, return MANUAL_REVIEW with INVALID_INVOICE_QUANTITY.
2. If PO and invoice currencies differ, return MANUAL_REVIEW with CURRENCY_MISMATCH.
3. If receipts is null, return NEEDS_DATA with RECEIPT_DATA_UNAVAILABLE.
4. Calculate total receipts and available quantity after prior invoices.
5. If total receipts is zero, add MISSING_GR; do not also add QUANTITY_EXCEEDS_AVAILABLE_GR.
6. Otherwise, if current invoice quantity > available quantity, add QUANTITY_EXCEEDS_AVAILABLE_GR.
7. Independently, if invoice unit price != PO unit price, add PRICE_VARIANCE.
8. If any flag exists, return EXCEPTION; otherwise return MATCH.

| Flag | First owner | Evidence to request | Proposed response |
|---|---|---|---|
| MISSING_GR | Receiving team with AP | Receipt or delivery confirmation | Investigate missing record or delivery |
| PRICE_VARIANCE | Buyer with AP | Agreed price and approved PO changes | Investigate invoice or PO correction |
| QUANTITY_EXCEEDS_AVAILABLE_GR | AP and receiving team | Receipt history and prior invoices | Check partial receipt or prior billing |
| RECEIPT_DATA_UNAVAILABLE | Integration support | Lookup error and freshness | Restore evidence, then re-evaluate |
| INVALID_INVOICE_QUANTITY | AP data validation | Correct source invoice | Correct input before analysis |
| CURRENCY_MISMATCH | AP | Currency and conversion policy | Route to supported manual process |

With multiple flags, preserve all applicable flags and involve the corresponding owners.
Missing a receipt record is a symptom, not proof that goods were not physically delivered.
