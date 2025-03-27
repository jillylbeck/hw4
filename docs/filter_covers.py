import json
import requests
import os
from requests.exceptions import RequestException
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_cover_exists(isbn13, session):
    """Check if a book cover exists on Open Library using a shared session."""
    cover_url = f"https://covers.openlibrary.org/b/isbn/{isbn13}-M.jpg"
    try:
        response = session.head(cover_url, timeout=3)
        return response.status_code == 200
    except RequestException as e:
        print(f"Error checking ISBN {isbn13}: {e}")
        return False

def filter_books_with_covers(input_path, output_path):
    print(f"Input path: {os.path.abspath(input_path)}")
    print(f"Output path: {os.path.abspath(output_path)}")
    
    # Loading all books
    with open(input_path, 'r') as f:
        books = json.load(f)
    
    print("First book:", books[0] if books else "No books")
    print(f"Total books in original: {len(books)}")
    
    # *** Removed the HEAD-check logic ***
    books_with_covers = books

    with open(output_path, 'w') as f:
        json.dump(books_with_covers, f, indent=2)
    
    print(f"Books with covers (not actually checked!): {len(books_with_covers)}")
    print(f"Output saved to: {output_path}")

if __name__ == "__main__":
    filter_books_with_covers(
        'data/json_output.json',
        'data/json_output_with_covers.json'
    )
