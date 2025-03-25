import json
import requests
import os

def check_cover_exists(isbn13):
    """Check if a book cover exists on Open Library"""
    cover_url = f"https://covers.openlibrary.org/b/isbn/{isbn13}-M.jpg"
    try:
        response = requests.head(cover_url, timeout=3)
        return response.status_code == 200
    except:
        return False

def filter_books_with_covers(input_path, output_path):
    print(f"Input path: {os.path.abspath(input_path)}")
    print(f"Output path: {os.path.abspath(output_path)}")
    
    # load books
    with open(input_path, 'r') as f:
        books = json.load(f)
    
    print("First book:", books[0] if books else "No books")
    
    # filter books with valid covers
    books_with_covers = [
        book for book in books 
        if book.get('isbn13') and check_cover_exists(book['isbn13'])
    ]
    
    with open(output_path, 'w') as f:
        json.dump(books_with_covers, f, indent=2)
    
    print(f"Total books: {len(books)}")
    print(f"Books with covers: {len(books_with_covers)}")
    print(f"Output saved to: {output_path}")

# Run the filter
filter_books_with_covers('data/json_output.json', 'data/json_output_with_covers.json')