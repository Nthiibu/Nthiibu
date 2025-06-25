
start_balance = float(input("Enter account balance at the beginning of the month: "))
total_withdrawals = float(input("Enter total withdrawals for the month: "))
total_deposits = float(input("Enter total deposits for the month: "))

total_transactions = total_withdrawals + total_deposits
federal_tax = total_transactions * 0.02

end_balance = start_balance - total_withdrawals + total_deposits - federal_tax

# Print the result
print(f"Balance at the end of the month: {end_balance:.0f}")