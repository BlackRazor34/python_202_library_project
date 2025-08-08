
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library import Library

app = FastAPI(
    title="Kütüphane API",
    description="Global AI Hub Python 202 Bootcamp Projesi için API",
    version="1.0"
)


lib = Library()

class ISBNModel(BaseModel):
    isbn: str


@app.get("/books", summary="Tüm Kitapları Listele")
def get_all_books():
    return {"books": lib.books}

@app.post("/books", summary="ISBN ile Kitap Ekle")
def add_book_by_isbn(isbn_model: ISBNModel):
    success = lib.add_book_by_isbn(isbn_model.isbn)
    if not success:
        raise HTTPException(status_code=404, detail=f"ISBN {isbn_model.isbn} ile kitap bulunamadı veya eklenemedi.")
    
    
    added_book = lib.find_book(isbn_model.isbn)
    return {"message": "Kitap başarıyla eklendi", "book": added_book} [cite: 92]

@app.delete("/books/{isbn}", summary="Kitabı ISBN ile Sil")
def delete_book_by_isbn(isbn: str):
    book = lib.find_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail=f"ISBN {isbn} ile silinecek kitap bulunamadı.")
    
    lib.remove_book(isbn)
    return {"message": f"ISBN {isbn} olan kitap başarıyla silindi."}