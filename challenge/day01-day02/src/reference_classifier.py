"""Reference for the explicitly scoped, synthetic Day 2 exercise only."""
from decimal import Decimal


def classify(case):
    invoice = case["invoice"]
    po = case["po"]
    invoice_qty = Decimal(invoice["quantity"])
    if invoice_qty <= 0:
        return {"outcome": "MANUAL_REVIEW", "flags": ["INVALID_INVOICE_QUANTITY"]}
    if invoice["currency"] != po["currency"]:
        return {"outcome": "MANUAL_REVIEW", "flags": ["CURRENCY_MISMATCH"]}
    if case["receipts"] is None:
        return {"outcome": "NEEDS_DATA", "flags": ["RECEIPT_DATA_UNAVAILABLE"]}

    total_received = sum((Decimal(r["quantity"]) for r in case["receipts"]), Decimal("0"))
    available_received = total_received - Decimal(case["prior_invoiced_quantity"])
    flags = []
    if total_received == 0:
        flags.append("MISSING_GR")
    elif invoice_qty > available_received:
        flags.append("QUANTITY_EXCEEDS_AVAILABLE_GR")
    if Decimal(invoice["unit_price"]) != Decimal(po["unit_price"]):
        flags.append("PRICE_VARIANCE")
    return {"outcome": "EXCEPTION" if flags else "MATCH", "flags": sorted(flags)}
