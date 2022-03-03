from bs4 import BeautifulSoup
from parsers.books import BooksParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = "article.product_pod"
        books_article = self.soup.select(locator)
        return [BooksParser(book) for book in books_article]
