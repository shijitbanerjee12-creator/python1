def calculate_remaining_due(total_bill_amount, amount_paid):
    """
    Calculates the remaining amount the customer owes.
    
    Args:
        total_bill_amount: The initial total amount of the bill (float or int).
        amount_paid: The amount the customer has paid so far (float or int).
        
    Returns:
        The remaining due amount (float).
    """
    if amount_paid >= total_bill_amount:
        return 0.0
    else:
        remaining_amount = total_bill_amount - amount_paid
        return round(remaining_amount, 2)

# --- Example Usage ---
bill = 150.75
paid = 50.00

amount_due = calculate_remaining_due(bill, paid)

print(f"Total Bill Amount: ${bill:.2f}")
print(f"Amount Paid:       ${paid:.2f}")
print(f"Remaining Due:     ${amount_due:.2f}")

# Example of overpayment
bill_2 = 75.00
paid_2 = 100.00
amount_due_2 = calculate_remaining_due(bill_2, paid_2)
print(f"\nTotal Bill Amount: ${bill_2:.2f}")
print(f"Amount Paid:       ${paid_2:.2f}")
print(f"Remaining Due:     ${amount_due_2:.2f} (Note: Result is 0.0 as they overpaid)")
