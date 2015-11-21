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

        # instance of trials
        my_trials = Trials()

        # walk line per line through html
        for j in range(0, len(my_scraper.list)):
            my_scraper.list[j] = my_scraper.list[j].strip()
            if my_scraper.list[j] == "":
                continue
            elif my_scraper.list[j] == "DRKS-ID:":
                j += 1
                my_trials.trial_id = my_scraper.list[j]
            elif my_scraper.list[j] == "Title":
                j += 1
                while my_scraper.list[j] != "end of 1:1-Block title":
                    my_trials.trial_title += my_scraper.list[j]
                    j += 1
                my_trials.trial_title = my_trials.trial_title.strip("\n")
            elif my_scraper.list[j] == "Trial Acronym":
                j += 1
                my_trials.trial_acronym = my_scraper.list[j]
            elif my_scraper.list[j] == "URL of the Trial":
                j += 1
                my_trials.trial_acronym = my_scraper.list[j]
            elif my_scraper.list[j] == "Brief Summary in Lay Language":
                j += 1
                while my_scraper.list[j] != "end of 1:1-Block public summary":
                    my_trials.summary_lay += my_scraper.list[j]
                    j += 1
                my_trials.summary_lay = my_trials.trial_title.strip("\n")
            elif my_scraper.list[j] == "Brief Summary in Scientific Language":
                j += 1
                while my_scraper.list[j] != "end of 1:1-Block scientific synopsis":
                    my_trials.summary_sci += my_scraper.list[j]
                    j += 1
                my_trials.summary_sci = my_trials.trial_title.strip("\n")
            elif my_scraper.list[j] == "Organizational Data":
                j += 1
                while my_scraper.list[j] != "end of 1:1-Block organizational data":
                    if my_scraper.list[j+1][-1] == ":" and my_trials.org_data:
                        my_trials.org_data += my_scraper.list[j]
                    else:
                        my_trials.org_data += my_scraper.list[j].strip()
                    j += 1
            elif my_scraper.list[j] == "Secondary IDs":
                j += 1
                while my_scraper.list[j] != "end of 1:n-Block secondary IDs":
                    if my_scraper.list[j+1][-1] == ":" and my_trials.secondary_ids:
                        my_trials.secondary_ids += my_scraper.list[j]
                    else:
                        my_trials.secondary_ids += my_scraper.list[j].strip()
                    j += 1
            elif my_scraper.list[j] == "Health Condition or Problem studied":
                j += 1
                while my_scraper.list[j] != "end of 1:N-Block indications":
                    if my_scraper.list[j+1][-1] == ":" and my_trials.health_Condition:
                        my_trials.health_Condition += my_scraper.list[j]
                    else:
                        my_trials.health_Condition += my_scraper.list[j].strip()
                    j += 1
            elif my_scraper.list[j] == "Interventions/Observational Groups":
                j += 1
                while my_scraper.list[j] != "end of 1:N-Block interventions":
                    if my_scraper.list[j+1][-1] == ":" and my_trials.interventions:
                        my_trials.interventions += my_scraper.list[j]
                    else:
                        my_trials.interventions += my_scraper.list[j].strip()
                    j += 1
            elif my_scraper.list[j] == "Characteristics":
                j += 1
                while my_scraper.list[j] != "end of 1:1-Block design":
                    if my_scraper.list[j+1][-1] == ":" and my_trials.characteristics:
                        my_trials.characteristics += my_scraper.list[j]
                    else:
                        my_trials.characteristics += my_scraper.list[j].strip()
                    j += 1
            elif my_scraper.list[j] == "Primary Outcome":
                j += 1
                while my_scraper.list[j] != "end of 1:1-Block primary endpoint":
                    if my_scraper.list[j][0] == "-" and my_trials.outcome_prim:
                        my_trials.outcome_prim += "\n" + my_scraper.list[j].strip()
                    else:
                        my_trials.outcome_prim += my_scraper.list[j].strip()
                    j += 1
            elif my_scraper.list[j] == "Secondary Outcome":
                j += 1
                while my_scraper.list[j] != "end of 1:1-Block secondary endpoint":
                    if my_scraper.list[j][0] == "-" and my_trials.outcome_sec:
                        my_trials.outcome_sec += "\n" + my_scraper.list[j].strip()
                    else:
                        my_trials.outcome_sec += my_scraper.list[j].strip()
                    j += 1
            elif my_scraper.list[j] == "Countries of Recruitment":
                j += 1
                while my_scraper.list[j] != "end of 1:n-Block recruitment countries":
                    if my_scraper.list[j+1][-1] == ":" and my_trials.countries_recruitment:
                        my_trials.countries_recruitment += my_scraper.list[j]
                    else:
                        my_trials.countries_recruitment += my_scraper.list[j].strip()
                    j += 1
            elif my_scraper.list[j] == "Locations of Recruitment":
                j += 1
                while my_scraper.list[j] != "end of 1:n-Block recruitment locations":
                    if my_scraper.list[j+1][-1] == ":" and my_trials.locations_recruitment:
                        my_trials.locations_recruitment += my_scraper.list[j]
                    else:
                        my_trials.locations_recruitment += my_scraper.list[j].strip()
                    j += 1

            else:
                # print(my_scraper.list[j])
                pass

if __name__ == "__main__":
    main()
