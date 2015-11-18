from HTMLParser import HTMLParser


class Scraper(HTMLParser):
    def error(self, message):
        pass

    def handle_data(self, data):
        self.data = data.strip()



