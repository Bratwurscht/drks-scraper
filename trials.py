from address import Address


class Trials(object):
    def __init__(self, trial_id, trial_title, trial_acronym, trial_url, summary_lay, summary_sci, org_data,
                 secondary_ids, health_condition, interventions, characteristics, outcome_prim, outcome_sec,
                 countries_recruitment, locations_recruitment, recruitment, criteria_inclusion, criteria_inclusion_add,
                 criteria_exclusion, add_prim_sponsor, add_sci_queries, add_pub_queries, add_mat_support, status,
                 publications):
        self.Trial_id = trial_id
        self.Trial_title = trial_title
        self.Trial_acronym = trial_acronym
        self.Trial_url = trial_url
        self.Summary_lay = summary_lay
        self.Summary_sci = summary_sci
        self.Org_data = org_data
        self.Secondary_ids = secondary_ids
        self.Health_Condition = health_condition
        self.Interventions = interventions
        self.Characteristics = characteristics
        self.Outcome_prim = outcome_prim
        self.Outcome_sec = outcome_sec
        self.Countries_recruitment = countries_recruitment
        self.Locations_recruitment = locations_recruitment
        self.Recruitment = recruitment
        self.Criteria_inclusion = criteria_inclusion
        self.Criteria_inclusion_add = criteria_inclusion_add
        self.Criteria_exclusion = criteria_exclusion
        self.Add_prim_sponsor = add_prim_sponsor
        self.Add_sci_queries = add_sci_queries
        self.Add_pub_queries = add_pub_queries
        self.Add_mat_support = add_mat_support
        self.Status = status
        self.Publications = publications