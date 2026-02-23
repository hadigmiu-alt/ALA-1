print("Inventory System")

items = ["Pen", "Book", "Bag"]
stock = [10, 5, 2]

name = input("Enter item name: ")
qty = int(input("Enter quantity: "))   # Convert to integer

if name in items:
    index = items.index(name)

    if stock[index] >= qty:
        stock[index] = stock[index] - qty
    else:
        print("Out of stock")
else:
    print("Item not found")

print("Remaining:", stock)

for i in range(3):   # Added colon
    print("Updated")

print("Finished")