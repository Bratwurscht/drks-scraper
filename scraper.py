from HTMLParser import HTMLParser


class Scraper(HTMLParser):
    def handle_data (self, data):
        data = data.strip()
        print(data)



