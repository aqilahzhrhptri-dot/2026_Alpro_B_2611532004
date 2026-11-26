<<<<<<< HEAD
menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        row.append(int(input("Day " + str(day) + ", " + menu + ": ")))
    sales.append(row)

print("Total per day:")
for i in range(len(sales)):
    day_total = 0
    for j in range(len(sales[i])):
        day_total += sales[i][j]
    print("Day " + str(i + 1) + ":", day_total)

menu_totals = []
for j in range(len(menus)):
    menu_total = 0
    for i in range(len(sales)):
        menu_total += sales[i][j]
    menu_totals.append((menus[j], menu_total))
print("Total per menu:", menu_totals)

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]
for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total
=======
menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        row.append(int(input("Day " + str(day) + ", " + menu + ": ")))
    sales.append(row)

print("Total per day:")
for i in range(len(sales)):
    day_total = 0
    for j in range(len(sales[i])):
        day_total += sales[i][j]
    print("Day " + str(i + 1) + ":", day_total)

menu_totals = []
for j in range(len(menus)):
    menu_total = 0
    for i in range(len(sales)):
        menu_total += sales[i][j]
    menu_totals.append((menus[j], menu_total))
print("Total per menu:", menu_totals)

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]
for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total
>>>>>>> origin/main
print(f"Best seller: {best_name} ({best_total})")