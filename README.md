# MindAI


<p align="center">
  <img src="(https://github.com/user-attachments/assets/27b211bf-c5ae-48ae-b636-8361255227d0)" alt="MindDI Logo" width="200" />
</p>

MindAI, eğitimde yapay zeka kullanarak öğrenme süreçlerini optimize eden ve kişiselleştirilmiş öğrenme deneyimleri sunan bir mobil uygulamadır. Bu proje, kullanıcıların öğrenme stillerini analiz ederek, onlara özel öğrenme yolları oluşturan ve içerikleri kişiselleştiren bir sistem geliştirmeyi amaçlamaktadır.

## Takım: DATAIN R&D

## İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Proje Hakkında

MindAI, psikolojik olarak doğrulanmış öğrenme stilleri ve yapay zeka destekli kişiselleştirilmiş öğrenme yolları oluşturur. Uygulama, psikolojik testler kullanarak öğrenme stillerini belirler ve son teknoloji yapay zeka modelleri ile bu verileri işler.

### Temel Teknolojiler
- Backend: Django
- Database: SQLite3
- Mobil Uygulama: Dart ve Flutter
- Yapay Zeka: OpenAI GPT Modelleri
- İçerik Kişiselleştirme: OpenAI GPT Modelleri
- Gerçek Zamanlı Bildirimler: RESTful API

## Özellikler

- **Kişiselleştirilmiş Öğrenme Yolları:** Kullanıcıların öğrenme stillerine göre optimize edilmiş öğrenme yolları sunar.
- **Yapay Zeka Destekli İçerik Kişiselleştirme:** Kullanıcıya özel içerik önerileri sunar.
- **Psikolojik Testler:** Öğrenme stillerini belirlemek için çeşitli testler sunar.
- **Gerçek Zamanlı Bildirimler:** Kullanıcıları motive etmek ve bilgilendirmek için gerçek zamanlı bildirimler gönderir.
- **Veri Analizi ve Raporlama:** Kullanıcı verilerini analiz eder ve detaylı raporlar sunar.

## Kurulum

MindAI uygulamasını yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

### Gereksinimler
- Python 3.8+
- Flutter SDK

### Adımlar

1. **Depoyu klonlayın:**
    ```bash
    git clone https://github.com/DATAIN-RD/MindAI.git
    cd MindAI
    ```

2. **Backend Kurulumu:**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # Windows için venv\Scripts\activate
    pip install -r requirements.txt
    flask run
    ```

3. **Mobil Uygulama Kurulumu:**
    ```bash
    cd ../mobile
    flutter pub get
    flutter run
    ```

## Kullanım

MindDI uygulamasını başlattıktan sonra, kullanıcı arayüzü üzerinden kayıt olabilir ve öğrenme stillerinizi belirlemek için testleri tamamlayabilirsiniz. Uygulama, öğrenme stilinize göre size özel içerik ve öğrenme yolları sunacaktır.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

1. Bu depoyu fork'layın.
2. Yeni bir dal (branch) oluşturun: `git checkout -b yeni-özellik`
3. Değişikliklerinizi commit'leyin: `git commit -m 'Yeni özellik ekle'`
4. Dalınıza push'layın: `git push origin yeni-özellik`
5. Bir Pull Request oluşturun.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına göz atabilirsiniz.
