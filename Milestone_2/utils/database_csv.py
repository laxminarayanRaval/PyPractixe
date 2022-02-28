"""
Concerned with storing and retrieving books from a list.
"""

books_file = "Books.txt"
# books = list()


def create_table_book():
    with open(books_file, 'w'):
        pass


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f"{name},{author},0\n")
    # books.append({"name": name, "author": author, "read": False})


def get_all_books():
    with open(books_file) as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]
    # return books


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
            book["read"] = '1'
            break
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")
