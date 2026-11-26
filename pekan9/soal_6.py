schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a: hari dengan mata kuliah terbanyak
busiest_day = ""
most = 0
for day, courses in schedule.items():
    if len(courses) > most:
        busiest_day = day
        most = len(courses)
print("Busiest day: " + busiest_day + " (" + str(most) + " courses)")

# 6b: jumlah hari sebuah mata kuliah muncul
course = input("Course: ")
count = 0
for day, courses in schedule.items():
    if course in courses:
        count = count + 1
print(course + ": " + str(count) + " days")