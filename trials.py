from address import Address


class Trials(object):
    def __init__(self, trial_id, trial_title, trial_acronym, trial_url, summary_lay, summary_sci, org_data,
                 secondary_ids, health_condition, interventions, characteristics, outcome_prim, outcome_sec,
                 countries_recruitment, locations_recruitment, recruitment, criteria_inclusion, criteria_inclusion_add,
                 criteria_exclusion, add_prim_sponsor, add_sci_queries, add_pub_queries, add_mat_support, status,
                 publications):
        self.trial_id = trial_id
        self.trial_title = trial_title
        self.trial_acronym = trial_acronym
        self.trial_url = trial_url
        self.summary_lay = summary_lay
        self.summary_sci = summary_sci
        self.org_data = org_data
        self.secondary_ids = secondary_ids
        self.health_Condition = health_condition
        self.interventions = interventions
        self.characteristics = characteristics
        self.outcome_prim = outcome_prim
        self.outcome_sec = outcome_sec
        self.countries_recruitment = countries_recruitment
        self.locations_recruitment = locations_recruitment
        self.recruitment = recruitment
        self.criteria_inclusion = criteria_inclusion
        self.criteria_inclusion_add = criteria_inclusion_add
        self.criteria_exclusion = criteria_exclusion
        self.add_prim_sponsor = add_prim_sponsor
        self.add_sci_queries = add_sci_queries
        self.add_pub_queries = add_pub_queries
        self.add_mat_support = add_mat_support
        self.status = status
        self.publications = publications
