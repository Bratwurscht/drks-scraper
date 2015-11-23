from HTMLParser import HTMLParser


class Scraper(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.list = [""]

    def error(self, message):
        pass

    def handle_data(self, data):
        print(data)
        self.list.append(data)



