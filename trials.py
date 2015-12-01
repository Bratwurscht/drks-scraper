# -*- coding: utf-8 -*-

from address import Address
import re

linebreak_string = "*{*LINEBREAK*}*"

class Trials:
    def __init__(self, scraper, database):
        self.val = dict()
        self.scraper = scraper
        self.database = database
	self.get_data()

    def get_data(self):
        # preprocessing for handling linebreaks within field
        for linebreak in self.scraper.find_all('br'):
            linebreak.replace_with(linebreak_string)

        self.get_trial_id()
        self.val["trial_title"] = self.get_p_data("title")
        self.val["trial_acronym"] = self.get_p_data("acronym")
        self.val["trial_url"] = self.get_p_data("trial_url")
        self.val["summary_lay"] = self.get_p_data("publicSummary")
        self.val["summary_sci"] = self.get_p_data("scientificSynopsis")
        self.val["org_data"] = self.get_colon_data('ul', "organizational-data")
        self.val["secondary_id"] = self.get_li_data("secondaryID")
        self.val["health_condition"] = self.get_li_data("health-condition")
        self.val["characteristics"] = self.get_colon_data('ul', "characteristica")
        self.val["outcome_primary"] = self.get_p_data("primaryEndpoint")
        self.val["outcome_secondary"] = self.get_p_data("secondaryEndpoints")
        self.val["recruitment_countries"] = self.get_li_data("country")
        self.val["recruitment_locations"] = self.get_li_data("location")
        self.val["recruitment"] = self.get_li_data("running")
        self.val["criteria_inclusion"] = self.get_colon_data('l', "inclusion")
        self.val["criteria_inclusion_add"] = self.get_p_data("inclusionAdd")
        self.val["criteria_exclusion"] = self.get_p_data("exclusion")
        #self.get_addresses()


        # postprocessing for handling linebreaks within field
        for key in self.val.itervalues():
            key = key.replace(linebreak_string, "\n")

        self.database.insert_data(self)

    def get_trial_id(self):
        tag = self.scraper.find('div', class_="drks_id")
        self.trial_title = tag.get_text(strip=True).replace("DRKS-ID:", "")

    def get_addresses(self):
        self.val["primary_sponsor"] = Address()
        self.val["contact_sci_queries"] = Address()
        self.val["contact_pub_queries"] = Address()

        institutions = self.scraper.find_all('li', class_="address-affiliation")
        self.distribute_data(institutions, "add_institution")
        streets = self.scraper.find_all('li', class_="address-street")
        self.distribute_data(streets, "add_street")
        cities = self.scraper.find_all('li', class_="address-city")
        self.distribute_data(cities, "add_city")
        countries = self.scraper.find_all('li', class_="address-land")
        self.distribute_data(countries, "add_country")
        phones = self.scraper.find_all('li', class_="address-telephone")
        self.distribute_data(phones, "add_phone")
        faxes = self.scraper.find_all('li', class_="address-fax")
        self.distribute_data(faxes, "add_fax")
        mails = self.scraper.find_all('li', class_="address-email")
        self.distribute_data(mails, "add_mail")
        urls =  self.scraper.find_all('li', class_="address-url")
        self.distribute_data(urls, "add_url")
        names = self.scraper.find_all('li', class_="address-name")
        self.distribute_data(names, "add_name")

    def distribute_data(self, keys, keyword):
        for key in keys:
            keyword = key.parent.parent.find('label').get_text()
            if keyword == "Primary Sponsor":
                self.val["primary_sponsor"].dic[keyword]
            elif keyword == "Contact for Scientific Queries":
                self.val["contact_sci_queries"].dic[keyword]
            elif keyword == "Contact for Public Queries":
                self.val["contact_pub_queries"].dic[keyword]


    def get_p_data(self, html_class):
        tag = self.scraper.find('p', class_=html_class)
        return tag.get_text(strip=True)

    def get_colon_data(self, html_tag, html_class):
        # 1:1 relationship -> values could be splitted up
        tags = self.scraper.find_all(html_tag, class_=html_class)
        result = ""
        for tag in tags:
            data = tag.get_text()
            temp = []
            stringbuilder = ""

            for i in range(0, len(data)):
                if data[i] == " " or data[i] == "\t":
                    continue
                if data[i] == '\n' and stringbuilder:
                    temp.append(stringbuilder)
                    stringbuilder = ""
                else:
                    stringbuilder += data[i].strip()

            string = ""
            for element in temp:
                if re.search(":$", element):
                    string += element
                else:
                    string += element + "\n"

            result += string
        return result

    def get_li_data(self, html_class):
        tags = self.scraper.find_all('li', class_=html_class)
        result = ""
        for tag in tags:
            if tag == tags[-1]:
                result += tag.get_text(strip=True).replace('\t', "")
            else:
                result += tag.get_text(strip=True).replace('\t', "") + "\n"
        return result


    @staticmethod
    def process_data_colon(data):
        temp = []
        stringbuilder = ""

        for i in range(0, len(data)):
            if data[i] == " " or data[i] == "\t":
                continue
            if data[i] == '\n' and stringbuilder:
                temp.append(stringbuilder)
                stringbuilder = ""
            else:
                stringbuilder += data[i].strip()

        string = ""
        for element in temp:
            if re.search(":$", element):
                string += element
            else:
                string += element + "\n"

        return string
