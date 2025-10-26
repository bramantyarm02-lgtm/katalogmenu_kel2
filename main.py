from models.menu import Menu
from services.menu_service import tampilkan_menu, rekomendasi_menu, cari_menu_by_harga
from data import buat_data_sample

def main():
    daftar_menu = buat_data_sample()
    
    while True:
        print("\n=== Aplikasi Rekomendasi Menu ===")
        print("1. Lihat semua menu")
        print("2. Rekomendasi berdasarkan kategori")
        print("3. Cari menu berdasarkan harga")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            tampilkan_menu(daftar_menu)

        elif pilihan == "2":
            kategori = input("Masukkan kategori (Makanan/Minuman/Dessert): ")
            rekomendasi_menu(daftar_menu, kategori)

        elif pilihan == "3":
            try:
                harga_maks = int(input("Masukkan harga maksimal: "))
                hasil_pencarian = cari_menu_by_harga(daftar_menu, harga_maks)
                if hasil_pencarian:
                    print(f"\nMenu di bawah Rp{harga_maks:,}:")
                    for menu in hasil_pencarian:
                        menu.tampilkan_info()
                else:
                    print("Tidak ada menu dengan harga tersebut.")
            except ValueError:
                print("Input harga harus angka!")

        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()