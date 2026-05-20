def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")


def add_numbers(*numbers):
    total = sum(numbers)
    expression = " + ".join(str(num) for num in numbers)
    print(f"{expression} = {total}")


def display_receipt(total_due, amount_paid):
    change_due = amount_paid - total_due

    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if amount_paid >= total_due:
        print(f"Change Due: ${change_due:.2f}")
    else:
        remaining_balance = total_due - amount_paid
        print(f"Remaining Balance: ${remaining_balance:.2f}")


display_mailing_label("Hana Tilahun", "123 Main Street", "Silver Spring", "MD", "20910")
print()
display_mailing_label("Sara Smith", "456 Oak Avenue", "Washington", "DC", "20001")

print()
add_numbers(5)
add_numbers(5, 10)
add_numbers(2, 4, 6, 8)

print()
display_receipt(25.00, 30.00)
print()
display_receipt(25.00, 25.00)
print()
display_receipt(25.00, 20.00)