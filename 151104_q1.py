class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} hasn't borrowed '{book.title}'.")

    def list_borrowed_books(self):
        print(f"{self.name} has borrowed:")
        for book in self.borrowed_books:
            print(f"- {book.title} by {book.author}")


# Interactive code
if __name__ == "__main__":
    # Sample books
    book1 = Book("Python Basics", "John Doe")
    book2 = Book("Data Science", "Jane Smith")
    books = [book1, book2]

    member = LibraryMember("Alice", "M001")

    while True:
        print("\n1. Borrow Book\n2. Return Book\n3. List Borrowed Books\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print("Available books:")
            for i, book in enumerate(books):
                if not book.is_borrowed:
                    print(f"{i+1}. {book.title} by {book.author}")
            idx = int(input("Enter book number to borrow: ")) - 1
            if 0 <= idx < len(books):
                member.borrow_book(books[idx])
        elif choice == "2":
            member.list_borrowed_books()
            title = input("Enter title to return: ")
            for book in member.borrowed_books:
                if book.title == title:
                    member.return_book(book)
                    break
            else:
                print("Book not found in borrowed list.")
        elif choice == "3":
            member.list_borrowed_books()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
