# Buat file dengan nama Konstanta_2611532004.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variable ditambah 4 digit nim terakhir contoh: jari_2004

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2004 = float(input('Masukkan nilai jari-jari: '))
luas_2004 = PI * jari_2004 * jari_2004
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2004, luas_2004))