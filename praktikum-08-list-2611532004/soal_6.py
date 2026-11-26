<<<<<<< HEAD
LAST_DIGIT = 4  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for day in range(1, 8):
    expenses.append(int(input("Day " + str(day) + ": ")))

total = 0
highest = expenses[0]
highest_day = 1
days_above = 0
for i in range(len(expenses)):
    total += expenses[i]
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1
    if expenses[i] > daily_limit:
        days_above += 1

print("Daily limit:", daily_limit)
print("Total:", total)
print(f"Average: {total / len(expenses):.1f}")
print(f"Highest: day {highest_day} ({highest})")
=======
LAST_DIGIT = 4  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for day in range(1, 8):
    expenses.append(int(input("Day " + str(day) + ": ")))

total = 0
highest = expenses[0]
highest_day = 1
days_above = 0
for i in range(len(expenses)):
    total += expenses[i]
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1
    if expenses[i] > daily_limit:
        days_above += 1

print("Daily limit:", daily_limit)
print("Total:", total)
print(f"Average: {total / len(expenses):.1f}")
print(f"Highest: day {highest_day} ({highest})")
>>>>>>> origin/main
print("Days above limit:", days_above)