![Lisans](https://img.shields.io/badge/lisans-MIT-mavi)
![Versiyon](https://img.shields.io/badge/versiyon-1.0.0-turuncu)


# 📚 Python 202 Library Project

Bu proje, **Global AI Hub Python 202 Bootcamp** kapsamında geliştirilmiş bir kütüphane yönetim sistemidir.
**FastAPI** ve **SQLite** kullanarak kitap ekleme, listeleme, güncelleme ve silme işlemlerini yapan bir REST API’dir.  
Ayrıca HTML/JS tabanlı basit bir arayüz ile görsel kullanım sağlar. 

## 📋 İçindekiler  
- [Özellikler](#Özellikler)  
- [Kurulum](#kurulum)  
- [kullanım](#Kullanım) 
- [HTML Arayüzü](#HTML-Arayüzü)  
- [Test Senaryoları](#Test Senaryoları) 
- [Test Çalıştırma](#Test Çalıştırma) 
- [Docker ile Çalıştırma](#Docker ile Çalıştırma)
- [Lisans](#Lisans)

---


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

API ile etkileşimli bir arayüz için `index.html` dosyasını bir web tarayıcısında açabilirsiniz. Bunun için:

1. Proje dizinindeki `index.html` dosyasını bulun.
2. Dosyayı doğrudan tarayıcınızda açın (örneğin, `file://<proje-yolu>/index.html`).
3. API sunucusunun çalıştığından emin olun (`uvicorn api:app --reload`).

**Not**: HTML arayüzü, API ile iletişim kurar; bu nedenle API sunucusunun çalıştığından emin olun.

---

## ✅ Test Senaryoları

```bash
python test_library.py
```

---


## 🧪 Test Çalıştırma

Proje, aşağıdaki senaryoları kapsayan otomatik testler içerir:
- Kitap ekleme ve silme
- JSON dosyasına kaydetme ve yükleme
- ISBN ile doğru eşleşme

Testleri çalıştırmak için aşağıdaki komutu kullanın:
```bash
pytest -v
```

---

## 🐳 Docker ile Çalıştırma

Aşağıdaki komutlarla projeyi Docker kullanarak çalıştırabilirsiniz:

```bash
# Docker imajını oluştur
docker build -t kutuphane-api .


# Docker konteynerini başlat (API 8000 portunda çalışır)
docker run -p 8000:8000 kutuphane-api
```

---

## Lisans  
MIT Lisansı altında dağıtılmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

