# Import necessary libraries
import datetime

# List of books in the library
library_books = []

# Dictionary to store borrowed books
borrowed_books = {}

# Function to add a new book to the library
def add_book(book_id, title, author):
    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "available": True  # Fixed typo from "avavaible"
    }
    library_books.append(book)
    print(f"Book '{title}' by {author} added to the library.")

# Function to print all books in the library
def print_all_books():
    if not library_books:
        print("\nNo books available in the library.")
        return
    
    print("\n📚 Available Books in the Library 📚")
    for book in library_books:
        status = "Available ✅" if book["available"] else "Borrowed ❌"
        print(f"ID: {book['book_id']} | Title: {book['title']} | Author: {book['author']} | Status: {status}")

# Function to search for a book
def search_book(title):
    found_books = [book for book in library_books if title.lower() in book["title"].lower()]

    if found_books:
        print("\n🔍 Search Results:")
        for book in found_books:
            status = "Available ✅" if book["available"] else "Borrowed ❌"
            print(f"ID: {book['book_id']} | Title: {book['title']} | Author: {book['author']} | Status: {status}")
    else:
        print("No books found with the given title.")

# Function to borrow a book
def borrow_book(book_id, user):
    for book in library_books:
        if book["book_id"] == book_id:
            if book["available"]:  
                book["available"] = False  
                borrowed_books[book_id] = {
                    "user": user,
                    "borrowed_date": datetime.datetime.now()
                }
                print(f"✅ Book '{book['title']}' borrowed by {user} successfully.")
                return
            else:
                print(f"❌ Book '{book['title']}' is already borrowed.")
                return

    print("⚠️ Book not available in the library or does not exist.")

# Function to return a book
def return_book(book_id):
    if book_id in borrowed_books:
        for book in library_books:
            if book["book_id"] == book_id:
                book["available"] = True  
                borrowed_books.pop(book_id)  
                print(f"✅ Book '{book['title']}' returned successfully.")
                return
    print(f"⚠️ Book with ID {book_id} is not borrowed or does not exist.")

# Main function to interact with the user
def main():
    while True:
        print("\n📖 Library Management System 📖")
        print("1. Add a new book")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = int(input("Enter the book ID (number): "))  
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            add_book(book_id, title, author)

        elif choice == "2":
            title = input("Enter the book title to search for: ")
            search_book(title)

        elif choice == "3":
            print_all_books()  # Print all books before prompting the user
            book_id = int(input("\nEnter the book ID to borrow: "))  
            user = input("Enter your name: ")
            borrow_book(book_id, user)

        elif choice == "4":
            book_id = int(input("Enter the book ID to return: "))  
            return_book(book_id)

        elif choice == "5":
            print("📚 Exiting the Library Management System. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

# Start the program
main()
