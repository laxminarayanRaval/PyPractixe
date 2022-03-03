import requests
from pages.books_page import BooksPage

url = 'https://books.toscrape.com/'
page_content = requests.get(url).content
page = BooksPage(page_content)

# print(page_content)
# print(page.books)
for book in page.books:
    print(book)
