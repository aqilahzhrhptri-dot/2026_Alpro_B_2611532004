# Buat file dengan nama perulangan_for3_2611532004.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_2004
# Program ini menggunakan fungsi input()

ulang_2004 = int(input("Masukkan jumlah perulangan: "))

jumlah_2004 = 0
for i_2004 in range(1, ulang_2004 + 1):
    print(i_2004, end=" ")
    jumlah_2004 = jumlah_2004 + i_2004

    if i_2004 < ulang_2004:
        print(" + ", end="")
    else:
        print(" = ", jumlah_2004, end="")
print()
print("Jumlah =", jumlah_2004)