from library import Book, Library
import os

def test_add_and_list_books():
    # Test için geçici bir dosya adı kullanalım
    test_filename = "test_library.json"
    lib = Library(test_filename)
    
    # Yeni bir kitap ekle
    book = Book("Test Başlık", "Test Yazar", "12345")
    lib.add_book(book)

    # Kitabın eklendiğini kontrol et
    assert len(lib.books) == 1
    assert lib.books[0].title == "Test Başlık"

    # Test sonrası temizlik
    if os.path.exists(test_filename):
        os.remove(test_filename)