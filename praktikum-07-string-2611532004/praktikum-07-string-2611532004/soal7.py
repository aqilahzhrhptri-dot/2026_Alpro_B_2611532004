# Name: Aqilah Zahirah Putri
# NIM: 2611532004
# Question 7
name = "aqilah zahirah putri"
nim = "2611532004"

space = name.find(" ")
if space == -1:
    first_name = name
else:
    first_name = name[:space]
username = first_name + nim[-3:]

intake = "20" + nim[:2]

print("=" * 30)
print(f"{'STUDENT CARD':^30}")
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)