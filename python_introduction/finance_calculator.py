mon_income = int(input("Enter your monthly income: "))
mon_exp = int(input("Enter your total monthly expenses: "))
mon_saving = mon_income - mon_exp
R  = 0.05
Projected_saving  = mon_saving * 12 + (mon_saving * 12 * R)
print(f"Your monthly savings are ${mon_saving}.")
print(f"Projected saving after one year, with interest, is: ${int(Projected_saving)}.")
