# Buat file dengan nama multi_if1_2611532004.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_2004
# Program ini menggunakan fungsi input()

umur_2004 = int(input("Input umur anda: "))
sim_2004 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_2004 >= 17 and sim_2004 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_2004 >= 17 and sim_2004 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_2004 < 17 and sim_2004 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_2004 < 17 and sim_2004 != 'y':
    print("Anda Belum Cukup Umur bawa motor")