from bs4 import BeautifulSoup


class ResultPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def results(self):
        pass
    