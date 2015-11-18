# -*- coding: utf-8 -*-

import requests
from scraper import Scraper
from trials import Trials

# count = 99999999
count = 2


def main():
    for i in range(1, count):
        scraped_url = "http://drks-neu.uniklinik-freiburg.de/drks_web/navigate.do?navigationId=trial.HTML&TRIAL_ID=DRKS" + str(i).zfill(8)
        website = requests.get(scraped_url).text.encode('utf-8')
        # website = website.split('\n')
        my_scraper = Scraper()
        my_scraper.feed(website)
        print(my_scraper.list)
        for i in range(0, len(my_scraper.list)):
            my_scraper.list[i]=my_scraper.list[i].strip()
            if not my_scraper.list[i]:
                continue
            else:
                print(my_scraper.list[i])


if __name__ == "__main__":
    main()
