import sqlite3

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            address TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_message(data, address):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (data, address) VALUES (?, ?)",
        (data, address)
    )

    conn.commit()
    conn.close()