income = int(input())

if income < 15528:
    tax = 0
elif income < 42708:
    tax = 15
elif income < 132407:
    tax = 25
else:
    tax = 28

calc = income * tax/100
# 0 — 15,527: 0% tax

# 15,528 — 42,707: 15% tax

# 42,708 — 132,406: 25% tax

# 132,407 and more: 28% tax

print(f'The tax for {income} is {tax}%. That is {calc:.0f} dollars!')
