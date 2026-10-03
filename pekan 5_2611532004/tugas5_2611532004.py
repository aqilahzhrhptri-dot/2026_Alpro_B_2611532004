print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_2004 = int(input("Masukkan ukuran skala jam pasir (N): "))

print("#", end="")
for garis_2004 in range(4 * n_2004 + 5):
    print("=", end="")
print("#", end="")
print()

for baris_2004 in range(n_2004, 0, -1):
    print("| ", end="")
    for spasi_kiri_2004 in range(2 * (n_2004 - baris_2004)):
        print(" ", end="")
    for angka_2004 in range(baris_2004, 0, -1):
        print(angka_2004, end=" ")
    print("<*>", end="")
    for angka_2004 in range(1, baris_2004 + 1):
        print(" ", end="")
        print(angka_2004, end="")
    for spasi_kanan_2004 in range(2 * (n_2004 - baris_2004)):
        print(" ", end="")
    print(" |", end="")
    print()

print("|", end="")
for spasi_kiri_2004 in range(2 * n_2004 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_kanan_2004 in range(2 * n_2004 + 1):
    print(" ", end="")
print("|", end="")
print()

for baris_2004 in range(1, n_2004 + 1):
    print("| ", end="")
    for spasi_kiri_2004 in range(2 * (n_2004 - baris_2004)):
        print(" ", end="")
    for angka_2004 in range(baris_2004, 0, -1):
        print(angka_2004, end=" ")
    print("<*>", end="")
    for angka_2004 in range(1, baris_2004 + 1):
        print(" ", end="")
        print(angka_2004, end="")
    for spasi_kanan_2004 in range(2 * (n_2004 - baris_2004)):
        print(" ", end="")
    print(" |", end="")
    print()

print("#", end="")
for garis_2004 in range(4 * n_2004 + 5):
    print("=", end="")
print("#", end="")
print()