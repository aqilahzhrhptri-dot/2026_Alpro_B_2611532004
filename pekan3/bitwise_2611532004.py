# Buat file dengan nama bitwise_2611532004.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_2004
# Program ini menggunakan fungsi input()

print("\n===================================")
print("3. OPERATOR BITWISE")
print("===================================")

angka1_2004 = int(input("Masukkan angka bitwise-1: "))
angka2_2004 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_2004 =", "| biner =", bin(angka1_2004))
print("angka2_2004 =", "| biner =", bin(angka2_2004))

# Bitwise AND
hasil = angka1_2004 & angka2_2004
print("\nBitwise AND (&)")
print(angka1_2004, "&", angka2_2004, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise OR
hasil = angka1_2004 | angka2_2004
print("\nBitwise OR (|)")
print(angka1_2004, "|", angka2_2004, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise XOR
hasil = angka1_2004 ^ angka2_2004
print("\nBitwise XOR (^)")
print(angka1_2004, "^", angka2_2004, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise NOT
hasil = ~angka1_2004
print("\nBitwise NOT (~)")
print("~", angka1_2004, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1_2004 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1_2004, "<<", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kanan
hasil = angka1_2004 >> angka2_2004
print("\nBitwise geser kanan (>>)")
print(angka1_2004, ">>", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit)")