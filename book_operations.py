# book_operations.py

import json

def add_book(book_collection, book):
    """Add a new book to the collection."""
    book_collection.append(book)

def remove_book(book_collection, book_id):
    """Remove a book from the collection by its unique ID."""
    for book in book_collection:
        if book['id'] == book_id:
            book_collection.remove(book)
            return

def update_book(book_collection, book_id, new_details):
    """Modify the details of an existing book."""
    for book in book_collection:
        if book['id'] == book_id:
            book.update(new_details)
            return

def retrieve_book(book_collection, book_id):
    """Get the details of a book by its unique ID."""
    for book in book_collection:
        if book['id'] == book_id:
            return book
    return None

def save_books_to_json(file_path, book_collection):
    """Save the current collection of books to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(book_collection, file, indent=4)

def load_books_from_json(file_path):
    """Load books from a JSON file and populate the book collection."""
    try:
        with open(file_path, 'r') as file:
            book_collection = json.load(file)
    except FileNotFoundError:
        book_collection = []
    return book_collection

def display_books(book_collection):
    """Display all books in the collection."""
    for book in book_collection:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
