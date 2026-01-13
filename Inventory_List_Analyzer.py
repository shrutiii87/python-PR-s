print("Welcome to Inventory List Analyzer!\n")

items = []   

while True:
    name = input("Enter item name: ")
    category = input("Enter category: ")
    qty = int(input("Enter quantity: "))

    # dictionary
    items.append({
        "name": name,
        "category": category.lower(),
        "qty": qty
    })

    more = input("\nDo you want to add more items? (y/n): ")
    if more.lower() != 'y':
        break


print("\n=========== INVENTORY SUMMARY ===========\n")


print("Total Different Items:", len(items))
print("Explanation: You entered", len(items), "different items:", end=" ")

# names print by loop
names = []
for it in items:
    names.append(it["name"])
print(", ".join(names))

# total quantity
total_qty = 0
for it in items:
    total_qty += it["qty"]

print("\nTotal Quantity in Stock:", total_qty)
print("Explanation: Sum of all quantities =", total_qty)

# average quantity
avg = total_qty / len(items)
print("\nAverage Quantity per Item:", avg)
print("Explanation: Average =", total_qty, "total /", len(items), "items")


#items print most and least

most_item = items[0]
least_item = items[0]

for it in items:
    if it["qty"] > most_item["qty"]:
        most_item = it
    if it["qty"] < least_item["qty"]:
        least_item = it

print("\nMost Stocked Item:", most_item["name"], "(", most_item["qty"], "units )")
print("Explanation:", most_item["name"], "has the highest quantity among all items.")
print("")
print("Least Stocked Item:", least_item["name"], "(", least_item["qty"], "units )")
print("Explanation:", least_item["name"], "has the lowest quantity.")
print("")
print("------------------------------------------------------------------------------------")

#unique categories

categories = []
for it in items:
    if it["category"] not in categories:
        categories.append(it["category"])
print("\nUnique Categories in Inventory:", categories)
print("Explanation: Categories are taken from user input and converted to lowercase.")
print("No duplicates are shown here.")
print("")
print("-----------------------------------------------------------------------------")


#item sorting

sorted_items = items[:]
for i in range(len(sorted_items)):
    for j in range(i+1, len(sorted_items)):
        if sorted_items[i]["qty"] < sorted_items[j]["qty"]:
            sorted_items[i], sorted_items[j] = sorted_items[j], sorted_items[i]


print("\nItems Sorted by Quantity (High to Low):")
print("")
for idx, it in enumerate(sorted_items, 1):
    print(idx, ".", it["name"], "-", it["qty"], "units")
print("")
print("Explanation: Items are sorted using the quantity field from highest to lowest.")
print("")
print("-------------------------------------------------------------------------------")

#categories

for i in range(len(categories)):
    for j in range(i+1, len(categories)):
        if categories[i] > categories[j]:
            categories[i], categories[j] = categories[j], categories[i]
print("")

print("\nCategories in Alphabetical Order:")
print("")
for idx, c in enumerate(categories, 1):
    print(idx, ".", c)
print("")
print("Explanation: The set of unique categories was sorted alphabetically for display.")

print("\n=========== END OF REPORT ===========")

