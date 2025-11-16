class Menu:
    def __init__(self, nama, kategori, harga):
        self.nama = nama
        self.kategori = kategori
        self.harga = harga

    def tampilkan_info(self):
        print(f"{self.nama} ({self.kategori}) - Rp{self.harga:,}")