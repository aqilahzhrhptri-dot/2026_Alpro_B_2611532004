# Buat file dengan assignment_2611532004.py
# Nama varibel ditambah 4 digit nim terakhir contoh: angka1_2004
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_2004 = int(input("Input angka-1: "))
angka2_2004 = int(input("Input angka-2: "))

print("\nNilai awal angka1_2004 =", angka1_2004)
print("Nilai angka2_2004 =", angka2_2004)

# Assignment biasa
hasil = angka1_2004
print("\nAssignment biasa (=)")
print("Hasil =", hasil)

# Assignment penambahan
hasil = angka1_2004
hasil += angka2_2004
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1_2004
hasil -= angka2_2004
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil)

# Assignment perkalian
hasil = angka1_2004
hasil *= angka2_2004
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2004 != 0:
    hasil = angka1_2004
    hasil /= angka2_2004
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil)
    # Operator tambahan
    hasil = angka1_2004
    hasil //= angka2_2004
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_2004
    hasil %= angka2_2004
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assingment perpangkatan
hasil = angka1_2004
hasil **= angka2_2004
print("\nAssignmnet perpangkatan (**=)")
print("Hasil =", hasil)