#from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup


class Scraper(HTMLParser):
    #def handle_starttag(self, tag, attrs):
    #    print("Encountered a start tag:", tag)

    #def handle_endtag(self, tag):
    #    print("Encountered an end tag :", tag)

    state = "ERR"

    def get_starttag_text (self, data):
        data = data.strip()
        print(data)
        if data == "":
            return 1
        else:
            return data