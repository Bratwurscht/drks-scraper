# -*- coding: utf-8 -*-

import requests
from scraper import Scraper

# count = 99999999
count = 2


def main():
    for i in range(1, count):
        scraped_url = "http://drks-neu.uniklinik-freiburg.de/drks_web/navigate.do?navigationId=trial.HTML&TRIAL_ID=DRKS" + str(i).zfill(8)
        website = requests.get(scraped_url).text.encode('utf-8')
        website = website.split('\n')
        my_scraper = Scraper()
        for i in range(0, len(website)):
            my_scraper.feed(website[i])

if __name__ == "__main__":
    main()
