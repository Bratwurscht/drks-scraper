# -*- coding: utf-8 -*-

import requests
import sys
from bs4 import BeautifulSoup
from trials import Trials
from database import Database
from config import Config

count = 99999999


def main():
    conf = Config()
    db = Database(conf.address, conf.username, conf.password, conf.database_name)

    for i in range(0, count):
        scraped_url = "http://drks-neu.uniklinik-freiburg.de/drks_web/navigate.do?navigationId=trial.HTML&TRIAL_ID=DRKS" + str(
            i).zfill(8)
        request = requests.get(scraped_url, stream=True)
        request.encoding = 'utf-8'

        my_scraper = BeautifulSoup(request.text.encode('utf8'), "lxml")

        if not (my_scraper.find('ul', class_="error") or my_scraper.find('ul', class_="errors")):
            # if true webpage contains valid data of study
            Trials(my_scraper, db)

        sys.stdout.write(
            "\r" + str(i) + " of " + str(count) + " data processed" + "\t\t" + str(i * 100 / count) + " percent")
        sys.stdout.flush()

    db.close_connection()


if __name__ == "__main__":
    main()
