# -- coding: utf-8 --

import MySQLdb

string_create_table = """
    CREATE TABLE data(
        trial_id LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        trial_title LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        trial_acronym LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        trial_url LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        summary_lay LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        summary_sci LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        org_data LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        secondary_id LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        health_condition LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        characteristics LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        outcome_primary LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        outcome_secondary LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        recruitment_countries LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        recruitment_locations LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        recruitment LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        criteria_inclusion LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        criteria_inclusion_add LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        criteria_exclusion LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        primary_sponsor_add_institution LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        primary_sponsor_add_street LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        primary_sponsor_add_city LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        primary_sponsor_add_country LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        primary_sponsor_add_phone LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        primary_sponsor_add_fax LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        primary_sponsor_add_mail LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        primary_sponsor_add_url LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        primary_sponsor_add_name LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_sci_queries_add_institution LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_sci_queries_add_street LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_sci_queries_add_city LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_sci_queries_add_country LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_sci_queries_add_phone LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_sci_queries_add_fax LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_sci_queries_add_mail LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_sci_queries_add_url LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_sci_queries_add_name LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_pub_queries_add_institution LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_pub_queries_add_street LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_pub_queries_add_city LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_pub_queries_add_country LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_pub_queries_add_phone LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_pub_queries_add_fax LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_pub_queries_add_mail LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_pub_queries_add_url LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci,
        contact_pub_queries_add_name LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci
    )
"""


class Database:
    def __init__(self, address, username, password, db_name):
        self.db = MySQLdb.connect(address, username, password, db_name, charset='utf8', init_command='SET NAMES UTF8', use_unicode=True)
        self.db_cursor = self.db.cursor()
        self.db_cursor.execute('DROP TABLE IF EXISTS data')
        self.db_cursor.execute(string_create_table)

    def insert_data(self, data):
        keys = data.val.keys()
        sql = str("INSERT INTO data(")
        type(sql)
        for key in keys:
            sql += key
            if key != keys[-1]:
                sql += str(", ")
        sql += str(") VALUES (")
        for key in keys:
            escaped_key = data.val[key].encode("utf-8")
            sql += str('"' + MySQLdb.escape_string(escaped_key) + '"')
            if key != keys[-1]:
                sql += str(', ')
        sql += str(')')

        self.db_cursor.execute(sql)
        self.db.commit()

    def close_connection(self):
        self.db.close()
