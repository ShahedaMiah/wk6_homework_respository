from budget import Budget

mya = Budget(650)
mya.add_income(1200)
mya.minus_rent(200)
mya.minus_utilities(90)
mya.minus_council_tax(20)
mya.add_bonus(50)
print("Mya has", mya.closing_balance())