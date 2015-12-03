# -*- coding: utf-8 -*-

import requests
import sys
from bs4 import BeautifulSoup
from config import Config
from database import Database
from trials import Trials

count = 99999999


def main():
    conf = Config()
    db = Database(conf.address, conf.username, conf.password, conf.database_name)

    valid_studies_counter = 0

    for i in range(0, count):
        try:
            scraped_url = "http://drks-neu.uniklinik-freiburg.de/drks_web/navigate.do?navigationId=trial.HTML&TRIAL_ID=DRKS" + str(
                i).zfill(8)
            request = requests.get(scraped_url, stream=True)
            request.encoding = 'utf-8'

            my_scraper = BeautifulSoup(request.text.encode('utf8'), "lxml")

            if not (my_scraper.find('ul', class_="error") or my_scraper.find('ul', class_="errors")):
                # if true webpage contains valid data of study
                Trials(my_scraper, db)
                valid_studies_counter += 1

            sys.stdout.write(
                "\r Processing " + str(i) + "/" + str(count) + " => " + str(
                    i * 100 / count) + " percent\t\t" + str(valid_studies_counter) + " studies found")
            sys.stdout.flush()
        except AttributeError:
            print("\n[-] attribute error at " + str(i))
        except Exception:
            print("\n[-] unknown error at " + str(i))

    db.close_connection()


if __name__ == "__main__":
    main()
