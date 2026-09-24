# Buat file dengan nama multi_if2_26115320004.py
# Buat program untuk kondisional if
# Nama variabel ditambaha 4 digit nim terakihir contoh: total belanja_2004
# Program ini manggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_2004 = float(input("Masukkan total belanja (Rp): "))

# Input status member(mengecek apakah user mengecek 'y' atau "ya)"
input_member_2004 = input("Apakah Anda Member (y/t): ").strip().lower()
is_member_2004 = input_member_2004 in ["y", "t"]

# Input status kode promo (mengecek apakah user mengetik 'y atau t')
input_promo_2004 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2004 = input_promo_2004 in ["y", "t"]

total_diskon_persen_2004 = 0

# Multi-if terpisah: Setiap kondisi diperiksa secara independen
# Disko bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_2004 > 1000000: 
    total_diskon_persen_2004 += 10 # Diskon belanja besar

if is_member_2004:
    total_diskon_persen_2004 += 5 # Diskon member

if kode_promo_valid_2004:
    total_diskon_persen_2004 += 15 # Diskon voucher 

# Menghitung nominal diskon dan total bayar
nominal_diskon_2004 = total_belanja_2004 * (total_diskon_persen_2004 / 100)
total_bayar_2004 = total_belanja_2004 - nominal_diskon_2004

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Totsl Diskon : {total_diskon_persen_2004}% (Rp {nominal_diskon_2004:,.0f})")
print(f"Total Bayar  : Rp {total_bayar_2004:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_2004}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid