# Program perulangan for untuk membuat segitiga

tinggi_2004 = int(input("Masukkan tinggi segitiga: "))
for i_2004 in range(1, tinggi_2004 + 1):
    for j_2004 in range(1, tinggi_2004 - i_2004 + 1):
        print(" ", end=" ")
    for k_2004 in range(1, 2 * i_2004):
        print("*", end=" ")
    print()