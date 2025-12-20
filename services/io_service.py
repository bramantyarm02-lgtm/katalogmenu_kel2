import csv

def export_jsonl(filename, rows):
    """
    rows: list of (id, nama, kategori, harga) dari database
    """
    with open(filename, "w", newline="", encoding="utf-8") as f:
        for row in rows:
            # Mengonversi setiap baris data menjadi dictionary dan menulisnya sebagai JSON
            json.dump({
                "id": row[0],
                "nama": row[1],
                "kategori": row[2],
                "harga": row[3]
            }, f, ensure_ascii=False)
            f.write("\n")  # Setiap JSON objek pada baris baru

def import_jsonl(filename):
    """
    Return: list of (nama, kategori, harga) untuk dimasukkan ke database
    JSONL wajib punya format seperti:
    {"nama": "Nasi Goreng Spesial", "kategori": "Makanan", "harga": 25000}
    """
    menus = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line.strip())  # Mengonversi setiap baris JSONL ke dictionary
            nama = data["nama"]
            kategori = data["kategori"]
            harga = data["harga"]
            menus.append((nama, kategori, harga))
    return menus
