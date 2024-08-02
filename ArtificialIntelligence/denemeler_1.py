import sqlite3

def tablo_oluştur():
    # Veritabanına bağlan
    con = sqlite3.connect("28son.db")
    cursor = con.cursor()
    
    # Tabloyu oluştur
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        ad TEXT,
        soyad TEXT,
        yas INTEGER,
        mail TEXT
    )
    ''')
    
    # Değişiklikleri kaydet
    con.commit()
    
    # Bağlantıyı kapat
    con.close()

tablo_oluştur()
