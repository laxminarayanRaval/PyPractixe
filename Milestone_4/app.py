import requests
import logging
from pages.books_page import BooksPage

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    filename='AllBooks.log',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG
)

# for only one page
"""
url = 'https://books.toscrape.com/'
page_content = requests.get(url).content
books = BooksPage(page_content).books
"""

# for Multiple pages (eg.: 50)
total_pages = 50
books = list()
# url = 'https://books.toscrape.com/catalogue/page-1.html'
logging.info("Started Scraping")
for i in range(1, total_pages + 1):
    logging.debug(f"Scraping Page No.{i}")
    page_content = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html").content
    books += BooksPage(page_content).books
# print(books)
logging.info("Scraping Done")
print(len(books))

# print(page_content)

# for book in books:
#      print(book.title, "\n\tIn just", book.price, "pound\n\tRated", book.ratings, "starts",  "\n\tClick here:", url+book.href)
