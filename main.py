# -*- coding: utf-8 -*-


import requests
from scraper import Scraper

# count = 99999999
count = 2


def main():
    for i in range(1, count):
        scraped_url = "http://drks-neu.uniklinik-freiburg.de/drks_web/navigate.do?navigationId=trial.HTML&TRIAL_ID=DRKS" + str(i).zfill(8)
        website = requests.get(scraped_url)
        my_scraper = Scraper()
        line = my_scraper.feed(website.text)
        print(line)
        #if line == "DRKS-ID":




if __name__ == "__main__":
    main()
