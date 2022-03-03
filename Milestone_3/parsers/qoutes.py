from locators.quotes_locators import  QuotesLocators


class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about the quote
    (quote content, author, tags)
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quotes {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuotesLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuotesLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuotesLocators.TAGS
        return [ele.string for ele in self.parent.select(locator)]
