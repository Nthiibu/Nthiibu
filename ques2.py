#overtime calculator
regular_hours = float(input("Enter total regular hours worked: "))
overtime_hours = float(input("Enter total overtime hours worked: "))
hourly_wage = float(input("Enter hourly wage rate: "))
regular_pay = regular_hours * hourly_wage
overtime_pay = overtime_hours * hourly_wage * 1.5
weekly_pay = regular_pay + overtime_pay
print(f"Weekly pay owing: ${weekly_pay:.2f}")