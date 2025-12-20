from db.database import get_connection

def insert_one(menu):
    """
    menu: tuple (nama, kategori, harga)
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO menu (nama, kategori, harga) VALUES (?, ?, ?)",
        menu
    )
    conn.commit()
    conn.close()


def insert_many(menus):
    """
    menus: list of tuple (nama, kategori, harga)
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.executemany(
        "INSERT INTO menu (nama, kategori, harga) VALUES (?, ?, ?)",
        menus
    )
    conn.commit()
    conn.close()

def get_all_menu():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nama, kategori, harga FROM menu ORDER BY id ASC")
    rows = cur.fetchall()
    conn.close()
    return rows

def count_menu():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM menu")
    (n,) = cur.fetchone()
    conn.close()
    return n

def delete_all_menu():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM menu")
    conn.commit()
    conn.close()
