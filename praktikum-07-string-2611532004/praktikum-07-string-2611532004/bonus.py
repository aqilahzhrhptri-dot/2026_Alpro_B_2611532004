# Name: Aqilah Zahirah Putri
# NIM: 2611532004
# Bonus
sentence = input("Sentence: ")

clean = sentence.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")