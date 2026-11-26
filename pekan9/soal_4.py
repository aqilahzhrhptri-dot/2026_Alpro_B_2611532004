students = input().split()
submitted = set(input().split())

not_submitted = set(students) - submitted

print("Submitted:", len(submitted), "students")
print("Not submitted:", len(not_submitted), "students")

for number in students:
    if number not in submitted:
        print(number)