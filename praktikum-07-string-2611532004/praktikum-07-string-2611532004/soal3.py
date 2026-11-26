# Name: Aqilah Zhahirah Putri
# NIM: 2611532004
# Question 3
# Bagian A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# Bagian B
text = "Aqilah Zhahirah Putri"
count = 0
for char in text:
    if char in "aiueoAIUEO":
        count += 1
print("Vowels:", count)
