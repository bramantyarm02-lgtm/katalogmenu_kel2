import sqlite3

DB_NAME = "katalog_menu.db"

def get_connection():
    # file katalog_menu.db akan dibuat otomatis jika belum ada
    return sqlite3.connect(DB_NAME)

def setup_database():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            kategori TEXT NOT NULL,
            harga INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()
