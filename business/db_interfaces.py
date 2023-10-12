import mysql.connector
from mysql.connector.errors import *
from mysql.connector import connect

# import Object Classes from folder to allow for testing

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
        try: self.cursor.execute("CREATE TABLE users (fullname VARCHAR(50), studentID VARCHAR(36) ,email VARCHAR(60), password VARCHAR(30))")
        except ProgrammingError: pass

        # create the 'employers' table, if already exist then command is ignored
        try: self.cursor.execute("CREATE TABLE employers (name VARCHAR(50), employerID VARCHAR(36), email VARCHAR(60)")
        except ProgrammingError: pass

    # create new entry into the student table
    def add_student(self, student : Student):
        try:
            query = f"INSERT INTO students (fullname, studentID, email, username, password) VALUES ('{student.get_fullname()}', '{student.get_id()}', '{student.get_email()}', '{student.get_password()}')"
            self.cursor.execute(query)
            self.db.commit()
        except ProgrammingError as error:
            raise Exception("Failed to create new student entry")
            print(error)

    # create new entry into the employers table
    def add_employer(self, employer : Employer):
        try:
            query = f"INSERT INTO employers (name, employerID, email) VALUES ('{employer.get_company_name()}', '{employer.get_id()}', '{employer.get_email()}')"
            self.cursor.execute(query)
            self.db.commit()
        except ProgrammingError as error:
            raise Exception("Failed to create new employer entry")
            print(error)

    # delete entry from the student table
    def delete_student(self, student : Student) :
        query = f"DELETE FROM students WHERE stduentID='{student.get_id()}'"
        self.cursor.execute(query)
        self.db.commit()

    # delete entry from the employers table
    def delete_employer(self, employer : Employer):
        query = f"DELETE FROM employers WHERE employerID='{employer.get_id()}'"
        self.cursor.execute(query)
        self.db.commit()

#
def populate_db() :
    pass