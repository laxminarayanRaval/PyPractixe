from utils import database

USER_CHOICE = """
-------------------------------
Enter:
      'a' : add a new book
      'l' : list all books
      'r' : mark a book as read
      'd' : delete a book
      'q' : Quit Program
Your CHOICE : """


def menu():
    usr_inpt = input(USER_CHOICE)
    database.create_table_book()

    while usr_inpt != 'q':
        if usr_inpt == 'a':
            prompt_add_book()
        elif usr_inpt == 'l':
            list_books()
        elif usr_inpt == 'r':
            prompt_read_book()
        elif usr_inpt == 'd':
            prompt_delete_book()
        else:
            print("Unknown Command, Try Again")
        usr_inpt = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter New Book Name   : ")
    author = input("Enter Book Author Name: ")
    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = "Yes" if int(book['read']) else "No"
        print(f"{book['name']} by {book['author']} | Readed : {read}")


def prompt_delete_book():
    name = input("Name of Book you want to Delete: ")
    database.remove_book(name)


def prompt_read_book():
    name = input("Enter Book name You readed : ")
    database.mark_readed_book(name)

menu()
