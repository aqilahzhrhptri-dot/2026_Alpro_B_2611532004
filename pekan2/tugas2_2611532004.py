from typing import Final

BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTER PRATIKAN ALPRO 2026 ===")

nama_2004 = input("Masukkan Nama Mahasiswa")
jenis_kelamin_2004 = input("Masukkan Jenis Kelamin (L/P): ")
umur_2004 = int(input("Masukkan Umur : "))
nilai_2004 = float(input("Masukkan Skor Tes Awal : "))
alamat_2004 = """
   Lakitan
   Kec. Lengayang
   Kab. Pesisir Selatan
"""

id_token_2004 = 100 + 3j

status_lulus_2004 = nilai_2004 >= BATAS_LULUS

print()
print("=== DATA PRAKTIKUM & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_2004, "| Tipe:", type(nama_2004))
print("Jenis Kelamin :", jenis_kelamin_2004,"| Tipe:", type(jenis_kelamin_2004))
print("Alamat Domisili:")
print(alamat_2004, "| Tipe:", type(alamat_2004))
print("Umur :", umur_2004, "| Tipe:", type(umur_2004))
print("Skor Tes Awal :", nilai_2004, "| Tipe:", type(nilai_2004))
print("ID Token Sinyal:", id_token_2004, "| Tipe:", type(id_token_2004))

print()
print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", status_lulus_2004, "| Tipe:", type(status_lulus_2004))
