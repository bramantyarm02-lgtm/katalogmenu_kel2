from models.menu import Menu

def buat_data_sample():
    return [
        Menu("Nasi Goreng Spesial", "Makanan", 25000),
        Menu("Mie Ayam", "Makanan", 20000),
        Menu("Es Teh Manis", "Minuman", 8000),
        Menu("Jus Alpukat", "Minuman", 12000),
        Menu("Pisang Goreng Keju", "Dessert", 15000),
        Menu("Brownies", "Dessert", 18000),
        Menu("Bakso", "Makanan", 16000),
    ]