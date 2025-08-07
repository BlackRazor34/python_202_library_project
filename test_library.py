from library import Library
import os
import time

def test_full_flow():
    # Test için geçici bir dosya adı ve bilinen bir ISBN kullanacağız
    # Bu test, Open Library API'sini kullanarak kitap ekleme, bulma ve silme işlemlerini test edecek.
    # Test dosyası adı
    test_filename = "test_library.json"
    test_isbn = "978-0321765723"  # "The C++ Programming Language"
    
   
    lib = Library(test_filename)
    
    # 1. Kitap Ekleme Testi (API'yi kullanacak)
    success = lib.add_book_by_isbn(test_isbn)
    assert success is True
    assert len(lib.books) == 1
    
    # 2. Kitap Bulma Testi
    found_book = lib.find_book(test_isbn)
    assert found_book is not None
    assert found_book.isbn == test_isbn
    
    # 3. Kitap Silme Testi
    lib.remove_book(test_isbn)
    assert len(lib.books) == 0
    
    # Test sonrası temizlik
    if os.path.exists(test_filename):
        os.remove(test_filename)