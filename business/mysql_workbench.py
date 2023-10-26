from mysql.connector.errors import *
from mysql.connector import *

import sys
sys.path.append('./') #allows for usage of 'admin.py' contents
from admin import DBUSERNAME

class MySQLWorkbenchInterface():
    def __init__(self):
        # intitialise connection to database and set up cursor to execute SQL queries
        self.connection = connect(host = "localhost", user = DBUSERNAME, password = "Aberdeen123")
        self.cursor = self.connection.cursor(buffered=True)

    #create database instance
    def create_db(self, db_name) :
        if not self.db_exists(db_name): 
            self.cursor.execute(f"CREATE DATABASE {db_name}")
        else:
            error_msg = f"Database {db_name} already exists!"
            raise Exception(error_msg)

    #delete database instance
    def destroy_db(self, db_name) :
        if self.db_exists(db_name): 
            deletion_query = f"DROP DATABASE {db_name}"
            self.cursor.execute(deletion_query)
        else:
            error_msg = f"Database {db_name} not found!"
            raise Exception(error_msg)

    def db_exists(self, db_name):
        try:
            self.cursor.execute("SHOW DATABASES")
            return True if db_name in [ db[0] for db in list(self.cursor)] else False
        except Error as e:
            raise Exception("Error occured while searching for database!")
