# -*- coding: utf-8 -*-

import requests
from trials import Trials
from bs4 import BeautifulSoup
from database import Database
import sys


# count = 99999999
count = 100000


def main():
    db = Database()
    for i in range(0, count):
        scraped_url = "http://drks-neu.uniklinik-freiburg.de/drks_web/navigate.do?navigationId=trial.HTML&TRIAL_ID=DRKS" + str(i).zfill(8)
        request = requests.get(scraped_url, stream=True)
        request.encoding = 'utf-8'
	
        my_scraper = BeautifulSoup(request.text, "lxml")

        if not (my_scraper.find('ul', class_="error") or my_scraper.find('ul', class_="errors")):
            # if true webpage contains valid data of study
            Trials(my_scraper, db)

        sys.stdout.write("\r" + str(i) + " of " + str(count) + " data processed" + "\t\t" + str(i*100/count) + " percent")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
