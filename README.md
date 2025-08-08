# 📚 Python 202 Library Project

Bu proje, **Global AI Hub Python 202 Bootcamp** kapsamında geliştirilmiş bir kütüphane yönetim sistemidir. Proje 3 aşamadan oluşur:

1. **Kitap nesnesi ve temel işlemler** (ekleme, silme, listeleme)
2. **JSON dosyası ile veri kalıcılığı**
3. **FastAPI ile RESTful API** sunumu

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

## 🔌 API Dokümantasyonu

### GET /books
Kütüphanedeki tüm kitapları JSON olarak listeler.

### POST /books
Girilen ISBN'e göre kitap ekler (Open Library'den veri çeker).

**Body örneği:**
```json
{
  "isbn": "9780140328721"
}
```

### DELETE /books/{isbn}
Girilen ISBN’e sahip kitabı siler.

---

## ✅ Test Senaryoları

```bash
python test_library.py
```

Testler şunları kapsar:
- Kitap ekleme/silme
- JSON dosyasına kaydetme/yükleme
- ISBN ile doğru eşleşme

---

