# Nesne Yönelimli Programlama (OOP) prensiplerini kullanarak modüler bir konsol uygulaması oluşturacağız:
## 1) Book Sınıfı : Her bir kitabın özelliklerini tanımlar
## 2) title, author ve isbn niteliklerine sahip bir __init__ metodu olmalıdır
## 3) __str__metodunu override ederek kitabı "Ulysses by james Joyce(ISBN: 978-0199535675)" şeklinde yazdıracağız

# Library Sınıfı: Tüm kütüphane operasyonlarını yönetecek.
## __init__ içinde, verilerin saklanacağı dosya adını (library.json) almalı ve kitapları tutacak boş bir liste oluşturmalıyız
## Uygulama başlar başlamaz load_books metodunu çağırarak mevcut verileri yüklemeliyiz

import json
import httpx # import işlemi

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f'"{self.title}" by {self.author} (ISBN: {self.isbn})'

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """library.json dosyasından kitapları yükler."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
                if not content.strip():
                    self.books = []
                    return
                book_data = json.loads(content)
                self.books = [Book(**book) for book in book_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    
    def add_book_by_isbn(self, isbn):
        """Verilen ISBN ile Open Library API'sinden kitap verilerini çeker ve kütüphaneye ekler."""
        api_url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(api_url, follow_redirects=True)
            
            if response.status_code != 200:
                print(f"Hata: ISBN {isbn} ile kitap bulunamadı. API Durum Kodu: {response.status_code}")
                return False

            book_data = response.json()
            title = book_data.get("title", "Başlık Bilgisi Yok")
            
            # Yazarlar bir liste olarak gelsin
            authors_data = book_data.get("authors", [])
            authors = ", ".join([self.get_author_name(author['key']) for author in authors_data])

            new_book = Book(title, authors, isbn)
            self.books.append(new_book)
            self.save_books()
            print(f"Başarıyla Eklendi: {new_book}")
            return True

        except httpx.RequestError as e:
            print(f"API isteği sırasında bir hata oluştu: {e}")
            return False
        except json.JSONDecodeError:
            print("API'den gelen yanıt geçerli bir JSON formatında değil.")
            return False

    def get_author_name(self, author_key):
        """Yazar key'i ile yazarın adını çeken yardımcı fonksiyon."""
        try:
            author_url = f"https://openlibrary.org{author_key}.json"
            response = httpx.get(author_url)
            if response.status_code == 200:
                return response.json().get("name", "Bilinmeyen Yazar")
            return "Bilinmeyen Yazar"
        except:
            return "Bilinmeyen Yazar"

    def save_books(self):
        """Tüm kitap listesini library.json dosyasına yazar."""
        # Book nesnelerini sözlük (dictionary) formatına çevirerek kaydetmek için
        with open(self.filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)

    def remove_book(self, isbn):
        """ISBN'e göre bir kitabı siler ve dosyayı günceller."""
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()

    def list_books(self):
        """Kütüphanedeki tüm kitapları listeler."""
        if not self.books:
            print("Kütüphanede hiç kitap yok.")
        for book in self.books:
            print(book)

    def find_book(self, isbn):
        """ISBN ile bir kitabı bulur ve Book nesnesini döndürür."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None