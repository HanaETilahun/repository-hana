# Variables
bank_balance = 100
savings_goal = 500
weekly_savings = 75

# While loop
while bank_balance < savings_goal:

    # Add weekly savings
    bank_balance += weekly_savings

    # 75% of goal logic
    if bank_balance >= savings_goal * 0.75:
        bank_balance -= 20
        print(f"So close! After treating myself, my balance is up to {bank_balance}.")

    # Halfway logic
    elif bank_balance > savings_goal / 2:
        print(f"Almost there! This week my balance is up to {bank_balance}.")

    # Normal message
    else:
        print(f"This week my balance increased to {bank_balance}.")

# Goal met message
print(f"Goal met! My current balance is {bank_balance}.")