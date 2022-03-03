import requests
from pages.books_page import BooksPage

url = 'https://books.toscrape.com/'
page_content = requests.get(url).content
books = BooksPage(page_content).books

# print(page_content)
# print(page.books)
# for book in books:
#     print(book.title, "\n\tIn just", book.price, "pound\n\tRated", book.ratings, "starts",  "\n\tClick here:", url+book.href)

