# Buat file dengan nama logika_2611532004.py
# Nama varibel ditambah 4 digit nim terakhir contoh: a1_2004
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_2004 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_2004 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_2004)
print("A2 =", a2_2004)

# Konjungsi: bernilai True jika keduanya True
hasil = a1_2004 and a2_2004 
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)

# Disjungsi: bernilai True jika salah satunya True
hasil = a1_2004 or a2_2004
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil)

# Negasi A1: membalik nilai A1
hasil = not a1_2004
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2_2004
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

# XOR: bernilai True jika kedua nilai berbeda
hasil = a1_2004 != a2_2004
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2 =", hasil)