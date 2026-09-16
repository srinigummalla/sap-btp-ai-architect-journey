"""Complete three TODOs. This is an offline teaching model, not SAP posting logic."""
from decimal import Decimal


def classify(case):
    invoice = case["invoice"]
    po = case["po"]
    invoice_qty = Decimal(invoice["quantity"])

    # Input routing is supplied so you can focus on procurement logic.
    if invoice_qty <= 0:
        return {"outcome": "MANUAL_REVIEW", "flags": ["INVALID_INVOICE_QUANTITY"]}
    if invoice["currency"] != po["currency"]:
        return {"outcome": "MANUAL_REVIEW", "flags": ["CURRENCY_MISMATCH"]}
    if case["receipts"] is None:
        return {"outcome": "NEEDS_DATA", "flags": ["RECEIPT_DATA_UNAVAILABLE"]}

    # TODO 1: Sum receipt quantities as Decimal, starting from Decimal("0").
    # Subtract prior_invoiced_quantity to calculate available_received.
    total_received = None
    available_received = None
    if total_received is None or available_received is None:
        raise NotImplementedError("Complete TODO 1 in student_classifier.py")

    flags = []
    # TODO 2: Append MISSING_GR when total_received is zero.
    # Otherwise append QUANTITY_EXCEEDS_AVAILABLE_GR if invoice_qty exceeds availability.
    # Replace the next raise with your conditional statements.
    raise NotImplementedError("Complete TODO 2 in student_classifier.py")

    # TODO 3: Independently compare invoice and PO unit prices as Decimal.
    # Append PRICE_VARIANCE when they differ, including a lower invoice price.

    return {"outcome": "EXCEPTION" if flags else "MATCH", "flags": sorted(flags)}
