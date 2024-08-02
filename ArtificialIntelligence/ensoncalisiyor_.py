import sqlite3
import openai
import time

# API anahtarınızı ve diğer bilgileri burada saklayın
OPEN_AI_API_KEY = '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'
ASSISTANT_ID = 'asst_nsPYyB9V7aFV2plIrm6R3qwJ'
openai.api_key = OPEN_AI_API_KEY



    # Veritabanına bağlan ve tabloyu oluştur
conn = sqlite3.connect('son0208.db')
cursor = conn.cursor()

import sqlite3

def tablo_olustur():
    conn = sqlite3.connect('son0208.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ensondeneme1 (
                        id INTEGER PRIMARY KEY,
                        ad TEXT,
                        soyad TEXT,
                        yas INTEGER,
                        email TEXT,
                        yanit TEXT
                      )''')
    conn.commit()
    conn.close()

# Tabloyu oluştur
tablo_olustur()




def veri_al():
    # Kullanıcıdan veri al
    ad = input("Adınızı girin: ")
    soyad = input("Soyadınızı girin: ")
    yas = int(input("Yaşınızı girin: "))
    email = input("Emailinizi girin: ")
    text = input("Size bir yol haritası oluşturabilmem için ilgilenmek istediğiniz alan hakkında sorunuzu yazınız (Çıkmak için 'q' girin): ")
    return ad, soyad, yas, email, text

def veri_kaydet(ad, soyad, yas, email, yanit):
    # Veritabanına veri ekle
    conn = sqlite3.connect('son0208.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO ensondeneme1 (ad, soyad, yas, email, yanit)
                      VALUES (?, ?, ?, ?, ?)''', (ad, soyad, yas, email, yanit))
    conn.commit()
    conn.close()
    print("Kullanıcı ve yanıt eklendi.")

def main():

    
    ad, soyad, yas, email, text = veri_al()  # Kullanıcıdan veri al
    
    # OpenAI API ile yanıt al
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ]
        )
        response_text = response['choices'][0]['message']['content'].strip()
        print(f"Yanıt: {response_text}")
    except Exception as e:
        print(f"API çağrısında bir hata oluştu: {e}")
        response_text = "Yanıt alınamadı."

    veri_kaydet(ad, soyad, yas, email, response_text)  # Veriyi kaydet

if __name__ == "__main__":
    main()


def tablo_olustur():
    retries = 5
    for i in range(retries):
        try:
            conn = sqlite3.connect('son0208.db')
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS ensondeneme1 (
                                id INTEGER PRIMARY KEY,
                                ad TEXT,
                                soyad TEXT,
                                yas INTEGER,
                                email TEXT,
                                yanit TEXT
                              )''')
            conn.commit()
            conn.close()
            break
        except sqlite3.OperationalError as e:
            print(f"Veritabanı hatası, deneme {i + 1}/{retries}: {e}")
            time.sleep(1)  # 1 saniye bekle ve tekrar dene

tablo_olustur()

