import csv

def export_csv(filename, rows):
    """
    rows: list of (id, nama, kategori, harga) dari database
    """
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nama", "kategori", "harga"])
        writer.writerows(rows)

def import_csv(filename):
    """
    Return: list of (nama, kategori, harga) untuk dimasukkan ke database
    CSV wajib punya header: nama,kategori,harga (kolom id boleh ada, tapi tidak dipakai)
    """
    menus = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            nama = row["nama"].strip()
            kategori = row["kategori"].strip()
            harga = int(row["harga"])
            menus.append((nama, kategori, harga))
    return menus
