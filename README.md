# 📚 Python 202 Library Project

Bu proje, **Global AI Hub Python 202 Bootcamp** kapsamında geliştirilmiş bir kütüphane yönetim sistemidir.
**FastAPI** ve **SQLite** kullanarak kitap ekleme, listeleme, güncelleme ve silme işlemlerini yapan bir REST API’dir.  
Ayrıca HTML/JS tabanlı basit bir arayüz ile görsel kullanım sağlar. 

## 🚀 Özellikler

- ISBN ile kitap ekleme (Open Library API entegrasyonu)
- Kitap listeleme
- Kitap bilgilerini güncelleme
- Kitap silme
- SQLite veri tabanı
- HTML/JS arayüz
- Docker desteği
- Pytest ile otomatik testler

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

### Aşama 1 ve 2: Terminal Uygulaması

```bash
python main.py
```

### Aşama 3: API Sunucusunu Başlatma

```bash
uvicorn api:app --reload
```

Sunucu çalıştıktan sonra Swagger UI arayüzüne şu adresten erişebilirsiniz:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🖥 HTML Arayüzü

index.html dosyasını tarayıcıda açarak API’yi görsel olarak kullanabilirsiniz.

---

## ✅ Test Senaryoları

```bash
python test_library.py
```

## 🧪 Test Çalıştırma

'''bash
pytest -v
'''

---

Testler şunları kapsar:
- Kitap ekleme/silme
- JSON dosyasına kaydetme/yükleme
- ISBN ile doğru eşleşme

---

## 🐳 Docker ile Çalıştırma

'''bash
docker build -t kutuphane-api .
docker run -p 8000:8000 kutuphane-api
'''

---


## Lisans  
MIT Lisansı altında dağıtılmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

