from models.menu import Menu # type: ignore

def tampilkan_menu(daftar_menu):
    print("\n=== Daftar Menu ===")
    for menu in daftar_menu:
        menu.tampilkan_info()

def rekomendasi_menu(daftar_menu, kategori_pilihan):
    print(f"\n=== Rekomendasi untuk kategori: {kategori_pilihan} ===")
    ditemukan = False
    for menu in daftar_menu:
        if menu.kategori.lower() == kategori_pilihan.lower():
            menu.tampilkan_info()
            ditemukan = True
    if not ditemukan:
        print("Maaf, kategori tidak ditemukan.")

def cari_menu_by_harga(daftar_menu, harga_maksimal):
    """Function tambahan: cari menu berdasarkan harga"""
    hasil = []
    for menu in daftar_menu:
        if menu.harga <= harga_maksimal:
            hasil.append(menu)
    return hasil