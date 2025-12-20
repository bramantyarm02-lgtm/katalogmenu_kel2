from models.menu import Menu
from services.menu_service import tampilkan_menu, rekomendasi_menu, cari_menu_by_harga
from services.io_service import export_jsonl, import_jsonl

from data import buat_data_sample
from db.database import setup_database
from db.menu_repository import get_all_menu, insert_many, count_menu, delete_all_menu

def seed_if_empty():
    """
    Mengisi database dengan data sample hanya jika database masih kosong.
    Ini membuat program tetap punya data awal tanpa hardcode permanen.
    """
    if count_menu() == 0:
        sample = buat_data_sample()
        data_db = [(m.nama, m.kategori, m.harga) for m in sample]
        insert_many(data_db)

def rows_to_objects(rows):
    """
    rows: list (id, nama, kategori, harga)
    -> list Menu object agar kompatibel dengan service Anda yang lama
    """
    daftar = []
    for (_, nama, kategori, harga) in rows:
        daftar.append(Menu(nama, kategori, harga))
    return daftar

def main():
    setup_database()
    seed_if_empty()

    while True:
        # Selalu baca data terbaru dari DB
        rows = get_all_menu()
        daftar_menu = rows_to_objects(rows)

        print("\n=== Aplikasi Rekomendasi Menu (SQLite3 + JSONL) ===")
        print("1. Lihat semua menu")
        print("2. Rekomendasi berdasarkan kategori")
        print("3. Cari menu berdasarkan harga")
        print("4. Export menu ke JSONL")
        print("5. Import menu dari JSONL")
        print("6. Reset data (hapus semua lalu isi sample)")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ").strip()

        if pilihan == "1":
            tampilkan_menu(daftar_menu)

        elif pilihan == "2":
            kategori = input("Masukkan kategori (Makanan/Minuman/Dessert): ").strip()
            rekomendasi_menu(daftar_menu, kategori)

        elif pilihan == "3":
            try:
                harga_maks = int(input("Masukkan harga maksimal: ").strip())
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
            filename = input("Nama file output (contoh: menu.jsonl): ").strip()
            try:
                rows = get_all_menu()
                export_jsonl(filename, rows)
                print(f"Export berhasil ke: {filename}")
            except Exception as e:
                print(f"Export gagal: {e}")

        elif pilihan == "5":
            filename = input("Nama file input JSONL: ").strip()
            try:
                menus = import_jsonl(filename)  # (nama,kategori,harga)
                insert_many(menus)
                print(f"Import berhasil. Data ditambahkan: {len(menus)}")
            except FileNotFoundError:
                print(f"File tidak ditemukan: {filename}")
            except KeyError as e:
                print(f"Kolom JSONL tidak sesuai. Kolom yang hilang: {e}")
            except ValueError:
                print("Kolom harga harus angka.")
            except Exception as e:
                print(f"Import gagal: {e}")

        elif pilihan == "6":
            konfirmasi = input("Yakin reset? (y/n): ").strip().lower()
            if konfirmasi == "y":
                delete_all_menu()
                seed_if_empty()
                print("Data direset ke data sample.")
            else:
                print("Batal reset.")

        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()