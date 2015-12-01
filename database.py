# -- coding: utf-8 --

import MySQLdb


class Database():
    def __init__(self, address, username, password, db_name):
        self.db = MySQLdb.connect(address, username, password, db_name)
        self.db_cursor = self.db.cursor()
        self.db_cursor.execute('DROP TABLE data')
        self.db_cursor.execute(
            'CREATE TABLE data(trial_title LONGTEXT, trial_acronym LONGTEXT,trial_url LONGTEXT,summary_lay LONGTEXT,summary_sci LONGTEXT,org_data LONGTEXT,secondary_id LONGTEXT,health_condition LONGTEXT,characteristics LONGTEXT,outcome_primary LONGTEXT,outcome_secondary LONGTEXT,recruitment_countries LONGTEXT,recruitment_locations LONGTEXT,recruitment LONGTEXT,criteria_inclusion LONGTEXT,criteria_inclusion_add LONGTEXT,criteria_exclusion LONGTEXT)')

    def insert_data(self, data):
        keys = data.val.keys()
        sql = unicode("INSERT INTO data(")
        for key in keys:
            if key == keys[-1]:
                sql += unicode(key)
            else:
                sql += unicode(key + ", ")
        sql += ") VALUES ("
        for key in keys:
            escaped_key = unicode(data.val[key].encode('utf-8'), errors='ignore')
            sql += unicode('"' + MySQLdb.escape_string(escaped_key) + '"')
            if key != keys[-1]:
                sql += unicode(', ')
        sql += unicode(')')

        self.db_cursor.execute(sql)
        self.db.commit()

    @staticmethod
    def escape_special_characters(text):
        special_characters = ["'", '"', "%"]
        for character in special_characters:
            print(character, unicode("\\" + character))
            text = text.replace(character, unicode('\\' + character))
        return text
