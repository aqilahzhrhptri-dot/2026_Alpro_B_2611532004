print("=== SISTEM TRANSAKSI TOKO ===")

nama_2004 = input("Masukkan Nama Pelanggan : ")
status_2004 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_2004 = int(input("Masukkan Total Belanja : "))
jumlah_2004 = int(input("Masukkan Jumlah Barang : "))
promo_2004 = input("Masukkan Kode Promo : ")

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan   : {nama_2004}")
print(f"Status Pelanggan : {status_2004}")
print(f"Total Belanja    : Rp{total_2004}")
print(f"Jumlah Barang    : {jumlah_2004}")
print(f"Kode Promo       : {promo_2004}")

kode_promo_2004 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"] # list kode promo

promo_valid_2004 = promo_2004 in kode_promo_2004 # in -> cek promo terdaftar
promo_invalid_2004 = promo_2004 not in kode_promo_2004 # not in -> sek promo tidak terdaftar

syarat_total_2004 = total_2004 >= 200000 # apakah memenuhi syarat belanja
syarat_jumlah_2004 = jumlah_2004 >= 3 # apakah memenuhi syarat barang
status_valid_2004 = status_2004 == "member" # apakah user member (== membandingkan nilai)

diskon_member_2004 = status_valid_2004 and syarat_total_2004 # and -> diskon khusus member
dapat_promo_2004 = promo_valid_2004 and (syarat_jumlah_2004 or status_valid_2004) # and + or
tanpa_diskon_2004 = not diskon_member_2004 # not -> kebalikan kondisi

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {syarat_total_2004}")
print(f"Jumlah Barang >= 3         : {syarat_jumlah_2004}")
print(f"Status Member              : {status_valid_2004}")
print(f"Kode Promo Tersedia        : {promo_valid_2004}")
print(f"Mendapatkan Diskon Member  : {diskon_member_2004}")
print(f"Mendapatkan Promo          : {dapat_promo_2004}")
print(f"Tanpa Diskon (not)         : {tanpa_diskon_2004}")

if diskon_member_2004:
    persen_diskon_2004 = 10 # member + belanja >= 200rb
elif syarat_total_2004:
    persen_diskon_2004 = 5 # nonmember tapi belanja besar
else:
    persen_diskon_2004 = 0

diskon_member_2004 = total_2004 * persen_diskon_2004 // 100 # * dan // -> besar diskon
sisa_bagi_2004 = total_2004 % jumlah_2004 # % -> sisa pembagian

total_bayar_2004 = total_2004 # operator penugasan biasa (=)
total_bayar_2004 -= diskon_member_2004 # -= -> kurangi diskon dari total

biaya_admin_2004 = 2000
total_bayar_2004 += biaya_admin_2004 # += -> tambah biaya admin

poin_2004 = 0
poin_2004 += jumlah_2004 * 5 # += -> tiap barang menambah 5 poin
if dapat_promo_2004:
    poin_2004 *= 2 # *= -> poin digandakan bila dapat promo

rata_rata_2004 = total_bayar_2004 / jumlah_2004 # / -> harga rata-rata barang

promo_utama_2004 = kode_promo_2004 # menunjuk objek YANG SAMA
promo_salinan_2004 = list(kode_promo_2004)   # objek BARU, isi/nilai sama

id_sama_2004 = promo_utama_2004 is kode_promo_2004 # True -> objek sama
id_beda_2004 = promo_salinan_2004 is not kode_promo_2004 # True -> objek berbeda
nilai_sama_2004 = promo_salinan_2004 == kode_promo_2004 # True -> isi/nilai sama

print("\n=== HASIL PERHITUNGAN ===")
print(f"Persen Diskon               : {persen_diskon_2004}%")
print(f"Diskon                      : Rp{diskon_member_2004}")
print(f"Biaya Admin                 : Rp{biaya_admin_2004}")
print(f"Total Pembayaran            : Rp{total_bayar_2004}")
print(f"Rata-rata Harga Barang      : Rp{round(rata_rata_2004, 2)}")
print(f"Sisa Pembagian (%)          : {sisa_bagi_2004}")
print(f"Poin Pelanggan              : {poin_2004}")

print("\n=== HASIL OPERATOR IDENTITAS ===")
print(f"promo_utama is kode_promo        : {id_sama_2004}")
print(f"promo_salinan is not kode_promo  : {id_beda_2004}")
print(f"promo_salinan == kode_promo      : {nilai_sama_2004}")
print("-> is membandingkan identitas objek, == membandingkan nilai/isi objek")

bit_member_2004 = int(status_valid_2004) << 0
bit_belanja_2004 = int(syarat_total_2004) << 1
bit_barang_2004 = int(syarat_jumlah_2004) << 2
bit_promo_2004 = int(promo_valid_2004) << 3

kode_transaksi_2004 = bit_member_2004 | bit_belanja_2004 | bit_barang_2004 | bit_promo_2004 # OR -> gabungkan kondisi
kode_referensi_2004 = bit_member_2004 | bit_belanja_2004 | bit_promo_2004 # kode acuan (tanpa syarat barang)

cek_member_2004 = kode_transaksi_2004 & bit_member_2004 # AND -> cek bit member aktif
cek_promo_2004= kode_transaksi_2004 & bit_promo_2004 # AND -> cek bit promo aktif
akses_member_2004 = cek_member_2004 != 0
akses_promo_2004 = cek_promo_2004 != 0
akses_ongkir_2004 = (kode_transaksi_2004 & (bit_promo_2004 | bit_barang_2004)) == (bit_promo_2004 | bit_barang_2004)

beda_status_2004 = kode_transaksi_2004 ^ kode_referensi_2004 # XOR -> beda status dgn referensi
geser_kiri_2004 = kode_transaksi_2004 << 1 # shift kiri

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses              : {format(kode_transaksi_2004, '04b')}")
print(f"Member Access               : {akses_member_2004}")
print(f"Promo Access                : {akses_promo_2004}")
print(f"Free Shipping Access        : {akses_ongkir_2004}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(f"{format(bit_member_2004, '04b')} | {format(bit_belanja_2004, '04b')} | "
      f"{format(bit_barang_2004, '04b')} | {format(bit_promo_2004, '04b')}")
print(f"Kode Biner   : {format(kode_transaksi_2004, '04b')}")
print(f"Kode Desimal : {kode_transaksi_2004}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(kode_transaksi_2004, '04b')} & {format(bit_member_2004, '04b')}")
print(f"Hasil Biner   : {format(cek_member_2004, '04b')}")
print(f"Hasil Desimal : {cek_member_2004}")

print("\nCek Promo")
print(f"{format(kode_transaksi_2004, '04b')} & {format(bit_promo_2004, '04b')}")
print(f"Hasil Biner   : {format(cek_promo_2004, '04b')}")
print(f"Hasil Desimal : {cek_promo_2004}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(kode_transaksi_2004, '04b')}")
print(f"Kode Referensi : {format(kode_referensi_2004, '04b')}")
print(f"{format(kode_transaksi_2004, '04b')} ^ {format(kode_referensi_2004, '04b')}")
print(f"Hasil Biner   : {format(beda_status_2004, '04b')}")
print(f"Hasil Desimal : {beda_status_2004}")

print("\n=== Shift ===")
print(f"{format(kode_transaksi_2004, '04b')} << 1")
print(f"Hasil Biner   : {format(kode_transaksi_2004, 'b')}")
print(f"Hasil Desimal : {kode_transaksi_2004}")

print("\n=== SELESAI ===")