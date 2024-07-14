# book_management_system.py

import json
from book_operations import add_book, remove_book, update_book, retrieve_book, save_books_to_json, load_books_from_json, display_books

def main():
    book_collection = load_books_from_json('books.json')

    while True:
        print("\nBook Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book")
        print("4. Retrieve Book")
        print("5. Display All Books")
        print("6. Save Books to File")
        print("7. Load Books from File")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year: ")
            add_book(book_collection, {'id': book_id, 'title': title, 'author': author, 'year': year})
        elif choice == '2':
            book_id = input("Enter book ID to remove: ")
            remove_book(book_collection, book_id)
        elif choice == '3':
            book_id = input("Enter book ID to update: ")
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            year = input("Enter new year: ")
            update_book(book_collection, book_id, {'title': title, 'author': author, 'year': year})
        elif choice == '4':
            book_id = input("Enter book ID to retrieve: ")
            book = retrieve_book(book_collection, book_id)
            if book:
                print(book)
            else:
                print("Book not found.")
        elif choice == '5':
            display_books(book_collection)
        elif choice == '6':
            save_books_to_json('books.json', book_collection)
        elif choice == '7':
            book_collection = load_books_from_json('books.json')
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
