import sys

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_pengunjung_2004 = input("Masukkan Nama Pengunjung :")
umur_2004 = int(input("Input Umur Anda :"))
sim_2004 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].lower()

print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba          (Rp 50,000)")
print(" 2. Arung Jeram           (Rp 75,000)")
print(" 3. Motor ATV Ekstrim     (Rp 120,000)")
print(" 4. Roller Coaster Kilat  (Rp 100,000)")
print(" 5. All-Access VIP        (RP 220,000)")
paket_2004 = int(input("Masukkan nomor paket (1-5) :"))

match paket_2004:
    case 1:
        nama_wahana_2004 = "Wahana Safari Rimba"
        harga_satuan_2004 = 50000
    case 2:
        nama_wahana_2004 = "Wahana Arung Jeram"
        harga_satuan_2004 = 75000
    case 3:
        nama_wahana_2004 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2004 = 120000
    case 4:
        nama_wahana_2004 = "Wahana Roller Coaster Kilat"
        harga_satuan_2004 = 100000
    case 5:
        nama_wahana_2004 = "Wahana All-Access VIP"
        harga_satuan_2004 = 220000
    case _:
        print("Paket wahana tidak valid!")
        sys.exit()

jumlah_tiket_2004 = int(input("Masukkan jumlah tiket :"))
if jumlah_tiket_2004 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")
is_member_2004 = input("Apakah Anda member? (y/t) : ").strip().lower()
kode_promo_valid_2004 = input("Apakah kode promo valid? (y/t) : ").strip().lower()

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if paket_2004 == 3 and umur_2004 >= 17 and sim_2004 == 'y':
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif paket_2004 == 3 and umur_2004 >= 17 and sim_2004 != 'y':
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
elif paket_2004 == 3 and umur_2004 < 17 and sim_2004 == 'y':
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif paket_2004 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
elif umur_2004 >= 10:
    print("Status Akses: Anda memenuhi syarat umur untuk memiliki wahana ini.")
else:
    print("Status Akses: Anda belum memenuhi syarat umur untuk menaiki wahana ini.")

subtotal_2004 = harga_satuan_2004 * jumlah_tiket_2004
total_diskon_persen_2004 = 0
if subtotal_2004 >= 200000:
    total_diskon_persen_2004 += 10 # Diskon Belanja Besar
if is_member_2004 in ['y', 'ya']:
    total_diskon_persen_2004 += 5 # Diskon member
if kode_promo_valid_2004 in ['y', 'ya']:
    total_diskon_persen_2004 += 15 # Diskon Voucher Promo
if jumlah_tiket_2004 >= 5:
    total_diskon_persen_2004 += 5 # Diskon Tambahan Rombongan
nominal_diskon_2004 = subtotal_2004 * (total_diskon_persen_2004 / 100)
total_bayar_2004 = subtotal_2004 - nominal_diskon_2004
if total_bayar_2004 > 300000:
    catatan_layanan_2004 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_2004 = "Terimakasih telah berkunjung"

print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_2004:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_2004}% (RP {nominal_diskon_2004:,.0f})")
print(f"Total Bayar      :Rp {total_bayar_2004:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_2004}")
print("Program Selesai")