from locators.books_locators import BooksLocators


class BooksParser:
    """
    Give one specific Book products article, get the data about
    Books ( title, ratings, price)
    """
    __TXTNUM__ = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Books {self.title} at {self.price} rated {self.ratings} starts>'

    @property
    def title(self):
        locator = BooksLocators.TITLE
        return self.parent.select_one(locator).attrs['title']

    @property
    def href(self):
        locator = BooksLocators.HREF
        return self.parent.select_one(locator).attrs['href']

    @property
    def ratings(self):
        locator = BooksLocators.RATINGS
        return self.__TXTNUM__[self.parent.select_one(locator).attrs['class'][1]]  # Txt "One" to Num "1"

    @property
    def price(self):
        locator = BooksLocators.PRICE
        return float(self.parent.select_one(locator).string[1:])
