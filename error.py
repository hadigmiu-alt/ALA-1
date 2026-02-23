print("Inventory System")

items = ["Pen","Book","Bag"]
stock = [10,5,2]

name = input("Enter item name: ")
qty = input("Enter quantity: ")   # ❌ qty is string (should be int)

index = items.index(name)   # ❌ if item not found → program will crash

if stock[index] >= qty      # ❌ Missing colon (:) and comparing int with string
    stock[index] = stock[index] - qty
else
    print("Out of stock")

print("Remaining:", stock)

for i in range(3)   # ❌ Missing colon (:)
print("Updated")    # ❌ Indentation error

print("Finished")