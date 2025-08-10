![Lisans](https://img.shields.io/badge/lisans-MIT-mavi)
![Versiyon](https://img.shields.io/badge/versiyon-1.0.0-turuncu)

# 📚 Python 202 Library Project

Bu proje, **Global AI Hub Python 202 Bootcamp** kapsamında geliştirilmiş bir **Kütüphane Yönetim Sistemi**’dir.  
**FastAPI** ve **SQLite** kullanarak kitap ekleme, listeleme, güncelleme ve silme işlemlerini yapan bir REST API sağlar.  
Ayrıca HTML/JS tabanlı basit bir arayüz ile görsel kullanım imkânı sunar.

---

## 📋 İçindekiler
- [🚀 Özellikler](#özellikler)  
- [📡 API Endpointleri](#api-endpointleri)  
- [🚀 Kurulum](#kurulum)  
- [⚙️ Kullanım](#kullanım)  
- [🖥 HTML Arayüzü](#html-arayüzü)  
- [📷 Ekran Görüntüleri](#ekran-görüntüleri)  
- [✅ Test Senaryoları](#test-senaryoları)  
- [🧪 Test Çalıştırma](#test-çalıştırma)  
- [🐳 Docker ile Çalıştırma](#docker-ile-çalıştırma)  
- [📌 Sistem Mimarisi](#sistem-mimarisi)  
- [🤝 Katkıda Bulunma](#katkıda-bulunma)  
- [📄 Lisans](#lisans)

---

## 🚀 Özellikler
- 📖 ISBN ile kitap ekleme (**Open Library API** entegrasyonu)
- 📋 Kitap listeleme
- ✏️ Kitap bilgilerini güncelleme
- ❌ Kitap silme
- 💾 **SQLite** veri tabanı
- 🖥 HTML/JS arayüz
- 🐳 Docker desteği
- 🧪 **Pytest** ile otomatik testler

---

## 📡 API Endpointleri

| Metod  | URL               | Açıklama                   |
|--------|-------------------|----------------------------|
| GET    | `/books`          | Tüm kitapları listeler     |
| POST   | `/books/{isbn}`   | ISBN ile kitap ekler       |
| PUT    | `/books/{isbn}`   | ISBN ile kitabı günceller  |
| DELETE | `/books/{isbn}`   | ISBN ile kitabı siler      |

Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🚀 Kurulum
```bash
# Reponun klonlanması
git clone https://github.com/BlackRazor34/python_202_library_project.git
cd python_202_library_project

# Bağımlılıkların kurulması
pip install -r requirements.txt
```

---

## ⚙️ Kullanım

### Aşama 1: Terminal Uygulaması
```bash
python main.py
```

### Aşama 2: API Sunucusunu Başlatma
```bash
uvicorn api:app --reload
```
Sunucu çalıştıktan sonra Swagger UI arayüzüne erişin:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🖥 HTML Arayüzü
API ile etkileşimli bir arayüz için `index.html` dosyasını tarayıcıda açabilirsiniz.

1. `index.html` dosyasını bulun.
2. Tarayıcıda açın (ör. `file://<proje-yolu>/index.html`).
3. API sunucusunun çalıştığından emin olun.

**Not:** HTML arayüzü, API ile iletişim kurar; bu nedenle API açık olmalıdır.

---

## 📷 Ekran Görüntüleri

### Swagger UI
![Swagger UI](Pic\resim1.png)

### HTML Arayüz
![HTML UI](Pic\resim2.png)

---

## ✅ Test Senaryoları
Proje, aşağıdaki senaryoları kapsayan otomatik testler içerir:
- Kitap ekleme ve silme
- SQLite veritabanına kaydetme ve yükleme
- ISBN ile doğru eşleşme
- Kitap bilgilerini güncelleme

---

## 🧪 Test Çalıştırma
```bash
pytest -v
```

---

## 🐳 Docker ile Çalıştırma
```bash
# Docker imajını oluştur
docker build -t kutuphane-api .

# Docker konteynerini başlat
docker run -p 8000:8000 kutuphane-api
```

---

## 📌 Sistem Mimarisi
```
[HTML UI]  -->  [FastAPI]  -->  [SQLite DB]
                         ↳  [Open Library API]
```

---

## 🤝 Katkıda Bulunma
1. Reponunuzu fork’layın.
2. Yeni bir branch oluşturun (`git checkout -b feature/yenilik`).
3. Değişikliklerinizi commit’leyin (`git commit -m 'Açıklama'`).
4. Branch’i push’layın (`git push origin feature/yenilik`).
5. Pull Request açın.

---

## 📄 Lisans
MIT Lisansı altında dağıtılmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

