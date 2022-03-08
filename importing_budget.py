from budget import Budget

mya = Budget(650)
mya.income(1200)
mya.rent(200)
mya.utilities(90)
mya.council_tax(20)
mya.bonus(50)
print("Mya has", mya.closing_balance())
