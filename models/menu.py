class Menu:
    def __init__(self, nama, kategori, harga):
        self.nama = nama
        self.kategori = kategori
        self.harga = harga

    def tampilkan_info(self):
        print(f"{self.nama} ({self.kategori}) - Rp{self.harga:,}")
    
    def apply_discount(self, discount_percent):
        harga_diskon = self.harga * (1 - discount_percent / 100)
        return f"Rp{int(harga_diskon):,}"