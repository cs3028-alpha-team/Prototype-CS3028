import mysql.connector
from mysql.connector.errors import *
from mysql.connector import connect

import sys, os
sys.path.append('./') #allows for usage of 'admin.py' contents
from admin import DBPASSWORD, DBUSERNAME

class MySQLWorkbenchInterface():
    def __init__(self):
        # intitialise connection to database and set up cursor to execute SQL queries
        self.connection = connect(host = "localhost", user = DBUSERNAME, password = DBPASSWORD)
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
            self.cursor.execute(f"DROP DATABASE {db_name}")
        else:
            error_msg = f"Database {db_name} not found!"
            raise Exception(error_msg)

    def show_dbs(self):
        try:
            self.cursor.execute("SHOW DATABASES")
            print("Databases : ", [ db[0] for db in list(self.cursor) ])
        except Error as e:
            raise Exception("Error occured while showing database!")

    def db_exists(self, db_name):
        try:
            self.cursor.execute("SHOW DATABASES")
            return True if db_name in [ db[0] for db in list(self.cursor)] else False
        except Error as e:
            raise Exception("Error occured while searching for database!")

class DatabaseInterface() :
    def __init__(self) :
        # intitialise connection to database and set up cursor to execute SQL queries
        self.connection = connect(host = "localhost", user = DBUSERNAME, password = DBPASSWORD, database = "alpha_db")
        self.cursor = self.connection.cursor(buffered=True)

        # create the 'students' table, if already exist then command is ignored
        try: self.cursor.execute("CREATE TABLE users (fullname VARCHAR(50), email VARCHAR(60), username VARCHAR(30), password VARCHAR(30))")
        except ProgrammingError: raise Exception("Error occured while creating 'students' table")

        # create the 'employers' table, if already exist then command is ignored
        try: self.cursor.execute("CREATE TABLE employers (name VARCHAR(50), email VARCHAR(60)")
        except ProgrammingError: raise Exception("Error while creating the 'employers' table")
