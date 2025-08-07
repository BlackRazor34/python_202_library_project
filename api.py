# api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library import Library # Aşama 1 ve 2'de yazdığımız sınıfı kullanıyoruz

# FastAPI uygulamasını başlat
app = FastAPI(
    title="Kütüphane API",
    description="Global AI Hub Python 202 Bootcamp Projesi için API",
    version="1.0"
)

# Kütüphane nesnesini oluştur
lib = Library()

# Pydantic ile veri modelleri oluşturma [cite: 95]
class ISBNModel(BaseModel):
    isbn: str

# API Endpoint'leri
@app.get("/books", summary="Tüm Kitapları Listele")
def get_all_books():
    """Kütüphanedeki tüm kitapların listesini JSON olarak döndürür.""" [cite: 91]
    return {"books": lib.books}

@app.post("/books", summary="ISBN ile Kitap Ekle")
def add_book_by_isbn(isbn_model: ISBNModel):
    """
    Request body'sinde bir ISBN alır, Open Library'den verileri çeker
    ve kitabı kütüphaneye ekler.
    """ [cite: 91]
    success = lib.add_book(isbn_model.isbn)
    if not success:
        raise HTTPException(status_code=404, detail=f"ISBN {isbn_model.isbn} ile kitap bulunamadı veya eklenemedi.")
    
    # Başarılı olursa eklenen son kitabı döndür
    added_book = lib.find_book(isbn_model.isbn)
    return {"message": "Kitap başarıyla eklendi", "book": added_book} [cite: 92]

@app.delete("/books/{isbn}", summary="Kitabı ISBN ile Sil")
def delete_book_by_isbn(isbn: str):
    """Belirtilen ISBN'e sahip kitabı kütüphaneden siler.""" [cite: 93]
    book = lib.find_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail=f"ISBN {isbn} ile silinecek kitap bulunamadı.")
    
    lib.remove_book(isbn)
    return {"message": f"ISBN {isbn} olan kitap başarıyla silindi."}