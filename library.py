# Nesne Yönelimli Programlama (OOP) prensiplerini kullanarak modüler bir konsol uygulaması oluşturmak.

## 1) Book Sınıfı : Her bir kitabın özelliklerini tanımlar.
## 2) title, author ve isbn niteliklerine sahip bir __init__ metodu olmalıdır.
## 3) __str__metodunu override ederek kitabı "Ulysses by james Joyce(ISBN: 978-0199535675)" şeklinde yazdıracağız.

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}(ISBN: {self.isbn})"
    

# Library Sınıfı: Tüm kütüphane operasyonlarını yönetecek.
## __init__ içinde, verilerin saklanacağı dosya adını (library.json) almalı ve kitapları tutacak boş bir liste oluşturmalı.
## Uygulama başlar başlamaz load_books metodunu çağırarak mevcut verileri yüklemeli.

import json
import httpx # import işlemi

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books() # Uygulama açıldığında kitapları yükle

    def load_books(self):
        """library.json dosyasından kitapları yükler."""
        try:
            with open(self.filename, 'r') as f:
                # JSON dosyasındaki her bir obje için bir Book nesnesi oluştur
                book_data = json.load(f)
                self.books = [Book(**book) for book in book_data]
        except FileNotFoundError:
            # Dosya yoksa, boş bir liste ile devam et
            self.books = []
    
    def add_book(self, isbn):
        """Verilen ISBN ile Open Library API'sinden kitap verilerini çeker ve kütüphaneye ekler."""
        api_url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(api_url)
            # API 404 (Not Found) dönerse veya başka bir hata olursa
            if response.status_code != 200:
                print(f"Hata: ISBN {isbn} ile kitap bulunamadı veya API'ye erişilemedi.")
                return False

            book_data = response.json()
            title = book_data.get("title", "Başlık Bilgisi Yok")
            
            # Yazarlar bir liste olarak gelebilir
            authors_data = book_data.get("authors", [])
            authors = ", ".join([self.get_author_name(author['key']) for author in authors_data])

            new_book = Book(title, authors, isbn)
            self.books.append(new_book)
            self.save_books()
            print(f"Başarıyla Eklendi: {new_book}")
            return True

        except httpx.RequestError as e:
            print(f"API isteği sırasında bir hata oluştu: {e}") # örn: internet yok
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
        # Book nesnelerini sözlük (dictionary) formatına çevirerek kaydet
        with open(self.filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)

    def add_book(self, book):
        """Yeni bir Book nesnesini kütüphaneye ekler ve dosyayı günceller."""
        self.books.append(book)
        self.save_books()

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