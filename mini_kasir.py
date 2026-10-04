print("=== MINI KASIR ===")

pembeli = input("Nama pembeli: ")
barang = input("Nama barang: ")
harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah barang: "))

total = harga * jumlah

print("\n=== STRUK PEMBELIAN ===")
print(f"Nama pembeli: {pembeli}")
print(f"Nama barang: {barang}")
print(f"Harga barang: Rp{harga}")
print(f"Jumlah barang: {jumlah}")
print(f"Total belanja: Rp{total}")

bayar = int(input("Uang pembayaran: Rp"))

if bayar >= total:
    kembalian = bayar - total
    print(f"Kembalian: Rp{kembalian}")
    print("Terima kasih sudah berbelanja!")
else:
    print("Uang pembayaran tidak mencukupi.")
