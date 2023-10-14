import mysql.connector
from mysql.connector.errors import *
from mysql.connector import connect
import sys
sys.path.append("./")
from objects.student import Student
from objects.admins import Admin
from objects.employer import Employer

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
            deletion_query = f"DROP DATABASE {db_name}"
            self.cursor.execute(deletion_query)
        else:
            error_msg = f"Database {db_name} not found!"
            raise Exception(error_msg)

    def show_dbs(self):
        try:
            self.cursor.execute("SHOW DATABASES")
            all_dbs = [ db[0] for db in list(self.cursor) ]
            print("Databases : ", all_dbs)
            return all_dbs
        except Error as e:
            raise Exception("Error occured while showing database!")

    def db_exists(self, db_name):
        try:
            self.cursor.execute("SHOW DATABASES")
            return True if db_name in [ db[0] for db in list(self.cursor)] else False
        except Error as e:
            raise Exception("Error occured while searching for database!")

class DatabaseInterface() :
    def __init__(self, db_name) :
        # intitialise connection to database and set up cursor to execute SQL queries
        self.connection = connect(host = "localhost", user = DBUSERNAME, password = DBPASSWORD, database = db_name)
        self.cursor = self.connection.cursor(buffered=True)

        # create the 'students' table, if already exist then command is ignored
        try: self.cursor.execute("CREATE TABLE students (fullname VARCHAR(50), studentID VARCHAR(36) ,email VARCHAR(60), password VARCHAR(30))")
        except ProgrammingError as error: pass

        # create the 'employers' table, if already exist then command is ignored
        try: self.cursor.execute("CREATE TABLE employers (name VARCHAR(50), employerID VARCHAR(36), email VARCHAR(60))")
        except ProgrammingError as error: pass

        # returns True if the student is already in the table, False otherwise
    
    def student_exists(self, student : Student):
        try:
            query = f"SELECT * FROM students WHERE studentID='{student.get_id()}'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return len(rows) == 1
        except ProgrammingError as error:
            raise Exception("Error while checking for student presence")

    # returns True if the employer is already in the table, False otherwise
    def employer_exists(self, employer : Employer):
        try:
            query = f"SELECT * FROM employers WHERE employerID='{employer.get_id()}'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return len(rows) == 1
        except ProgrammingError as error:
            raise Exception("Error while checking for employer presence")


    # create new entry into the student table
    def add_student(self, student : Student):
        if self.student_exists(student) : raise Exception("Student with given credentials already exists")
        try:
            query = f"INSERT INTO students (fullname, studentID, email, password) VALUES ('{student.get_fullname()}', '{student.get_id()}', '{student.get_email()}', '{student.get_password()}')"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to create new student entry")
            print(error)

    # create new entry into the employers table
    def add_employer(self, employer : Employer):
        if self.employer_exists(employer) : raise Exception("Employer with given credentials already exists")
        try:
            query = f"INSERT INTO employers (name, employerID, email) VALUES ('{employer.get_company_name()}', '{employer.get_id()}', '{employer.get_email()}')"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to create new employer entry")
            print(error)

    # delete entry from the student table
    def delete_student(self, student : Student) :
        if not self.student_exists(student) : raise Exception("Student does not exist")
        try:
            query = f"DELETE FROM students WHERE studentID='{student.get_id()}'"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to delete student from database")
            print(error)

    # delete entry from the employers table
    def delete_employer(self, employer : Employer):
        if not self.employer_exists(employer) : raise Exception("Employer does not exist")
        try:
            query = f"DELETE FROM employers WHERE employerID='{employer.get_id()}'"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to delete employer from database")
            print(error)

    def show_table_rows(self, table_name):
        # prints the contents of the given table
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            return [ row for row in list(self.cursor) ]
        except ProgrammingError as error:
            print("Error while trying to display table data. Make sure table exists")       
            print(error)


# populate database given that user calling method is authorised (only the dev team)
# returns True if method was successfully executed else False
def populate_db(db_name) :
    dev_password = str(input("Enter development password : "))
    if (dev_password != "AlphaTeamBestTeam!"):
        raise Exception("Missing credentials")
        return False

    # set up interfaces and reset working environment
    workbench = MySQLWorkbenchInterface()
    database = DatabaseInterface("alpha_db")
    workbench.destroy_db("alpha_db") 
    workbench.create_db("alpha_db")
    
    # populate students table with 50 dummy entries
    for i in range(0, 50):
        pass

    #populate employers table with 15 dummy entries
    for i in range(0, 15):
        pass

    # NOTE : populate process will have a 'for loop' for each entity in the final DB schema

if __name__ == "__main__":
    w = MySQLWorkbenchInterface()
    w.show_dbs()

    db = DatabaseInterface("alpha_db")
    db.show_table_rows("students")
    print("----------")
    db.show_table_rows("employers")
