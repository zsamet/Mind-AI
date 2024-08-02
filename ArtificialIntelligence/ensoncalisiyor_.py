import sqlite3
import openai
import time

# API anahtarınızı ve diğer bilgileri burada saklayın
OPEN_AI_API_KEY = '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'
ASSISTANT_ID = 'asst_nsPYyB9V7aFV2plIrm6R3qwJ'
openai.api_key = OPEN_AI_API_KEY

def veri_al():
    # Kullanıcıdan veri al
    ad = input("Adınızı girin: ")
    soyad = input("Soyadınızı girin: ")
    yas = int(input("Yaşınızı girin: "))
    email = input("Emailinizi girin: ")
    soru = input("Size bir yol haritası oluşturabilmem için ilgilenmek istediğiniz alan hakkında sorunuzu yazınız (Çıkmak için 'q' girin): ")
    return ad, soyad, yas, email, soru

def veri_kaydet(ad, soyad, yas, email, soru, yanit):
    # Veritabanına veri ekle
    conn = sqlite3.connect('son0208.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO ensondeneme1 (ad, soyad, yas, email, soru, yanit)
                      VALUES (?, ?, ?, ?, ?, ?)''', (ad, soyad, yas, email, soru, yanit))
    conn.commit()
    conn.close()
    print("Kullanıcı, soru ve yanıt eklendi.")

def main():
    # Kullanıcıdan veri al
    ad, soyad, yas, email, soru = veri_al()
    
    # OpenAI API ile yanıt al
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": soru}
            ]
        )
        response_text = response['choices'][0]['message']['content'].strip()
        print(f"Yanıt: {response_text}")
    except Exception as e:
        print(f"API çağrısında bir hata oluştu: {e}")
        response_text = "Yanıt alınamadı."

    # Veriyi veritabanına kaydet
    veri_kaydet(ad, soyad, yas, email, soru, response_text)

if __name__ == "__main__":
    main()

