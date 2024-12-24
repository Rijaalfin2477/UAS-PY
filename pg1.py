# Import module
from tabulate import tabulate
import datetime

# Assign data
mydata_harga = [
    ["Suoetra", 18500],
    ["Fiesta", 20000],
    ["Molto", 10500],
    ["Rinso", 5000]
]

# Create header
head = ["Produk", "Harga"]

# Display table
print(tabulate(mydata_harga, headers=head, tablefmt="grid"))

pemesanan = {}

def tambah_pesanan():
    # Input data pembeli
    nama = input("Masukkan nama pembeli: ")

    # Menampilkan daftar produk yang tersedia
    print("\nPilih Produk:")
    for i, (produk, harga) in enumerate(mydata_harga, start=1):
        print(f"{i}. {produk} - Rp{harga:,}")

    # Memilih produk berdasarkan input pengguna
    try:
        produk_terpilih = int(input("Masukkan nomor pilihan produk: "))
        if 1 <= produk_terpilih <= len(mydata_harga):
            pilprod, harga_produk = mydata_harga[produk_terpilih - 1]
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            return  # Mengakhiri fungsi jika pilihan tidak valid
    except ValueError:
        print("Input tidak valid. Silakan masukkan nomor yang benar.")
        return

    # Membuat nomor pesanan unik menggunakan datetime
    nomor_pesanan = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Menyimpan data pesanan
    pemesanan[nomor_pesanan] = (nama, pilprod, harga_produk)

    # Menampilkan informasi pesanan
    print("=" * 20)
    print(f"Pemesanan berhasil! Nomor pesanan Anda adalah: {nomor_pesanan}")
    print(f"Pembeli: {nama}")
    print(f"Produk: {pilprod}, Harga: Rp{harga_produk:,}")
    print("=" * 20)

# Contoh penggunaan fungsi tambah_pesanan
tambah_pesanan()

# riski kontol
