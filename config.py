import configparser
import os
import sys


class Config:
    def __init__(self):
        config = configparser.ConfigParser()

        # check whether config file exists, else write example file
        if os.path.isfile('config.ini'):
            config.read('config.ini')
            if 'DATABASE' in config:
                self.address = config['DATABASE']['address']
                self.username = config['DATABASE']['username']
                self.password = config['DATABASE']['password']
                self.database_name = config['DATABASE']['database_name']
            else:
                sys.exit(0)
        else:
            print("No config file found, please fill config.ini with your properties")
            config['DATABASE'] = {
                'address': 'address-to-database',
                'username': 'your-username',
                'password': 'your-password',
                'database_name': 'name-of-database-for-data'}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            sys.exit(0)
