# 1. Nomor 1 sampai 100 -> for
for i in range(1, 101):
    print(i)

# 2 Input sampai "exit" -> while
text = input("Enter text: ")
while text != "exit":
    text = input("Enter text: ")

# 3. Jumlahkan n bilangan -> for
n = int(input("How many numbers?" ))
total = 0
for i in range(n):
    total += int(input("Enter a number: "))

# 4. Gandakan saldo sampai melebihi target -> while
balance = 100
target = 1000
while balance <= target:
    balance *= 2