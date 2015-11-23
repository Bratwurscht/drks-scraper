# -*- coding: utf-8 -*-

from address import Address


class Trials(object):
    def __init__(self):
        self.trial_id = ""
        self.trial_title = ""
        self.trial_acronym = ""
        self.trial_url = ""
        self.summary_lay = ""
        self.summary_sci = ""
        self.org_data = ""
        self.secondary_ids = ""
        self.health_Condition = ""
        self.interventions = ""
        self.characteristics = ""
        self.outcome_prim = ""
        self.outcome_sec = ""
        self.countries_recruitment = ""
        self.locations_recruitment = ""
        self.recruitment = ""
        self.criteria_inclusion = ""
        self.criteria_inclusion_add = ""
        self.criteria_exclusion = ""
        self.add_prim_sponsor = ""
        self.add_sci_queries = ""
        self.add_pub_queries = ""
        self.add_mat_support = ""
        self.status = ""
        self.publications = ""

    def get_data(self, scraper):
        self.scraper = scraper

        # preprocessing for handling linebreaks within field
        for linebreak in self.scraper.find_all('br'):
            linebreak.replace_with('\n')

        self.get_trial_id()
        self.get_trial_title()
        self.get_trial_acronym()
        self.get_trial_url()
        self.get_summary_lay()
        self.get_org_data()

        # postprocessing for handling linebreaks within field

        print(vars(self))

    def get_trial_id(self):
        tag = self.scraper.find('div', class_="drks_id")
        self.trial_title = tag.get_text(strip=True).replace("DRKS-ID:", "")

    def get_trial_title(self):
        tag = self.scraper.find('p', class_="title")
        self.trial_title = tag.get_text()

    def get_trial_acronym(self):
        tag = self.scraper.find('p', class_="acronym")
        self.trial_acronym = tag.get_text(strip=True)

    def get_trial_url(self):
        tag = self.scraper.find('p', class_="trial_url")
        self.trial_url = tag.get_text(strip=True)

    def get_summary_lay(self):
        tag = self.scraper.find('p', class_="publicSummary")
        self.summary_lay = tag.get_text(strip=True)

    def get_summary_sci(self):
        tag = self.scraper.find('p', class_="scientificSynopsis")
        self.summary_sci = tag.get_text(strip=True)

    def get_org_data(self):
        tags = self.scraper.find_all('ul', class_="organizational-data")
        for tag in tags:
            print(tag.get_text())


    def get_recruitment(self):
        tags = self.scraper.find('div', class_="drks_id")
        #for tag in tags:
        print(tags.get_text().encode('utf-8'))
         #   print("***")
