NUMBER_WHEN_HAVE_DISCOUNT = 100
DISCOUNT = 0.1

total_price = 0
number_of_item = int(input("Number of items:"))
for i in range(0, number_of_item):
    price = float(input("Price of item:"))
    while price < 0:
        print("Invalid number")
        price = float(input("Price of item:"))
    total_price += price
if total_price > NUMBER_WHEN_HAVE_DISCOUNT:
    total_price *= (1 - DISCOUNT)
print(f"Total price for {number_of_item} items is ${total_price:.2f}")