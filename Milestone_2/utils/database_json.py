import json
"""
Concerned with storing and retrieving books from a list.
[ "Books":
    {
        'name': 'Book Name',
        'author': 'Author Name'
    }
]
"""
books_file = "Books.json"
# books = list()


def create_table_book():
    with open(books_file, 'w') as file:
        json.dump([], file, indent=3)


def add_book(name, author):
    books = get_all_books()
    books.append({"name": name, "author": author, "read": False})
    _save_all_books(books)


def get_all_books():
    try:
        with open(books_file) as file:
            return json.load(file)
    except Exception:
        create_table_book()
        get_all_books()


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file, indent=3)


def remove_book(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            books.remove(book)
            break
    _save_all_books(books)
#     global books
#     books = [book for book in books if book['name'] != name]


def mark_readed_book(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = True
            break
    _save_all_books(books)
