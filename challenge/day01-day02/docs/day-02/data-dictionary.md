# Fixture data dictionary

These fields are a teaching model, not an SAP OData schema or a released API contract.
Amounts and quantities are decimal strings to avoid binary floating point money arithmetic.

| Field | Meaning and boundary |
|---|---|
| case_id | Independent scenario; unique in this dataset |
| company_code | Synthetic US01; the real system must verify user access |
| po.id and po.item | Synthetic purchasing document key, item 10 |
| po.quantity | Total ordered quantity in EA |
| po.unit_price | Net USD price per one EA, excluding tax and freight |
| po.currency | USD in the purchase order |
| receipts | Complete receipt list for this PO item at the scenario snapshot |
| receipts[].quantity | Positive received quantity in EA; reversals excluded |
| receipts null | Receipt lookup unavailable; never interpret as zero |
| receipts empty list | Successful lookup with zero receipt records |
| prior_invoiced_quantity | Net previously invoiced quantity, excluding the current invoice |
| invoice.quantity | Current invoice quantity; must be greater than zero |
| invoice.unit_price | Current net price per one EA |
| invoice.currency | Must equal PO currency for this simple classifier |
| flags | Zero or more explanatory triage flags; not SAP blocking codes |
| outcome | MATCH, EXCEPTION, NEEDS_DATA or MANUAL_REVIEW |

available_received_quantity = sum(receipts quantities) - prior_invoiced_quantity
price_difference_per_unit = invoice.unit_price - po.unit_price
price_difference_amount = price_difference_per_unit * invoice.quantity
quantity_excess = max(invoice.quantity - available_received_quantity, 0)

This model does not allocate invoice items to individual GR items. Real GR-based invoice
verification may require that allocation. We aggregate for the teaching exercise only.
