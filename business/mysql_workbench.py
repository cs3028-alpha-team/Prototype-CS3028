# Import built-in modules
from mysql.connector.errors import *
from mysql.connector import *
import sys

# Class used to connect to MySQL software on local machine
class MySQLWorkbenchInterface():

    def __init__(self):
        # Intitialise connection to database and set up cursor to execute SQL queries
        self.connection = connect(host = "localhost", user = "root", password = "LanaBanana100?")
        self.cursor = self.connection.cursor(buffered=True)

    # Create database instance
    def create_db(self, db_name) :
        if not self.db_exists(db_name): 
            self.cursor.execute(f"CREATE DATABASE {db_name}")
        else:
            error_msg = f"Database {db_name} already exists!"
            raise Exception(error_msg)

    # Delete database instance
    def destroy_db(self, db_name) :
        if self.db_exists(db_name): 
            deletion_query = f"DROP DATABASE {db_name}"
            self.cursor.execute(deletion_query)
        else:
            error_msg = f"Database {db_name} not found!"
            raise Exception(error_msg)

    # Check whether a database already exists
    def db_exists(self, db_name):
        try:
            # Search 'db_name' against all databases stored on MySQL Workbench
            self.cursor.execute("SHOW DATABASES")
            return True if db_name in [ db[0] for db in list(self.cursor)] else False
        except Error as e:
            raise Exception("Error occured while searching for database!")
