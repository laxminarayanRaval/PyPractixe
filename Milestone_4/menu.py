from app import books
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    filename='BookScraping.log',
    level=logging.DEBUG
)

books_generator = (x for x in books)
USER_CHOICE = """---------------------
Select Your Filter:
    'h' - 10 Highest Rated Books
    'c' - 10 Cheapest Price Books
    'b' - 10 Bestest Books (High Rated n Cheap Price)
    'n' - Book one by one
    'q' - Quit the Program
Inter Your Choice: """



def high_rated_books():  # sort By Ratings in Desc
    hrbooks = sorted(books, key=lambda x: x.ratings * -1)[:10]
    return hrbooks


def cheap_books():  # sort By Price
    cbooks = sorted(books, key=lambda x: x.price)[:10]
    return cbooks


def best_books():  # sort by High Ratings and Cheap Price
    # bsbooks = sorted(books, key=lambda x: x.price)
    # hrbooks = sorted(bsbooks, key=lambda x: x.ratings * -1)[:10]
    bbooks = sorted(books, key=lambda x: (x.ratings * -1, x.price))[:10]
    return bbooks


def get_next_book():
    return next(books_generator)


user_choices = {
    'h': high_rated_books,
    'c': cheap_books,
    'b': best_books
}


def menu():
    user_input = input(USER_CHOICE)
    logging.debug('User Started Running Program')
    while user_input != 'q':
        print('------------------------')
        if user_input == 'n':
            d = get_next_book()
            print(f"{d.title}\n\tRatings: {d.ratings} Stars\t Price: {d.price}")
        else:
            if user_input in ('h', 'c', 'b'):
                data = user_choices[user_input]()
            else:
                print("Unknown Command, Try Again")
                user_input = input(USER_CHOICE)
                continue

            for d in data:
                print(f"Title: {d.title}\n\tRatings: {d.ratings} Stars\t Price: {d.price}")
        user_input = input(USER_CHOICE)
    logging.info('User Ended Program')


menu()
