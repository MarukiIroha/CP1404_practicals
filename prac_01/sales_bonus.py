"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_MAX = 0.15
BONUS_MIN = 0.1
SALES_EDGE = 1000

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= SALES_EDGE:
        bonus = sales * BONUS_MAX
    else:
        bonus = sales * BONUS_MIN
    print(bonus)
    sales = float(input("Enter sales: $"))
print(f"Thank you")
