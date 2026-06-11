# Library Management System with File Handling

BOOK_FILE = "library_book_issue.txt"

# ---------------- Helper Functions ----------------
def load_books():
    books = {}
    try:
        with open(BOOK_FILE, "r") as f:
            for line in f:
                bid, title, qty = line.strip().split(",")
                books[bid] = {"title": title, "qty": int(qty)}
    except FileNotFoundError:
        print("books.txt not found!")
    return books

def save_books(books):
    with open(BOOK_FILE, "w") as f:
        for bid, info in books.items():
            f.write(f"{bid},{info['title']},{info['qty']}\n")

# ---------------- Operations ----------------
def display_all(books):
    for bid, info in books.items():
        print(bid, ":", info)

def search_book(books, bid):
    return books.get(bid, "Not Found")

def issue_book(books, bid):
    if bid in books and books[bid]["qty"] > 0:
        books[bid]["qty"] -= 1
        save_books(books)
        return f"{books[bid]['title']} issued successfully!"
    else:
        return "Book not available!"

def return_book(books, bid):
    if bid in books:
        books[bid]["qty"] += 1
        save_books(books)
        return f"{books[bid]['title']} returned successfully!"
    else:
        return "Book ID not found!"

def unavailable_books(books):
    return {bid: info for bid, info in books.items() if info["qty"] == 0}

def restock_books(books):
    return {bid: info for bid, info in books.items() if info["qty"] < 2}

# ---------------- Menu Driven ----------------
def main():
    books = load_books()

    while True:
        print("\n--- Library Menu ---")
        print("1. Display all books")
        print("2. Search book by ID")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. Display unavailable books")
        print("6. Display books requiring restocking")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_all(books)

        elif choice == "2":
            bid = input("Enter Book ID: ")
            print(search_book(books, bid))

        elif choice == "3":
            bid = input("Enter Book ID to issue: ")
            print(issue_book(books, bid))

        elif choice == "4":
            bid = input("Enter Book ID to return: ")
            print(return_book(books, bid))

        elif choice == "5":
            print("Unavailable Books:", unavailable_books(books))

        elif choice == "6":
            print("Books requiring restocking:", restock_books(books))

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
