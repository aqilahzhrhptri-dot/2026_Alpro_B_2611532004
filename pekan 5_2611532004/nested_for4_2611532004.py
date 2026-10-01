# Buat file dengan nama nested_for4_2611532004.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_2004
# Program ini menggunakan fungsi input()

tinggi_2004 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2004 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2004 = tinggi_2004
    c_2004 = a_2004
    lebar_2004 = (2 * tinggi_2004 + 1)

    for i_2004 in range(1, tinggi_2004 + 1):
        b_2004 = c_2004 + 1

        for j_2004 in range(1, lebar_2004 + 1):

            # Baris atas dan bawah
            if i_2004 == 1 or i_2004 == tinggi_2004:
                if j_2004 == 1 or j_2004 == lebar_2004:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_2004 == 1 or j_2004 == lebar_2004:
                    print("|", end="")
                else:
                    if j_2004 == c_2004:
                        print("<", end="")
                    elif j_2004 == b_2004:
                        print(">", end="")
                    elif j_2004 == (lebar_2004 - c_2004):
                        print("<", end="")
                    elif j_2004 == (lebar_2004  - c_2004 + 1):
                        print(">", end="")
                    elif j_2004 > b_2004 and j_2004 < (lebar_2004 - c_2004):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_2004 -= 2

        if a_2004 <= 0:
            c_2004 = (-a_2004) + 2
        else:
            c_2004 = a_2004