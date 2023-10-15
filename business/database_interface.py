from mysql.connector.errors import *
from mysql.connector import *
import sys
sys.path.append("./")
from objects.student import Student
from objects.admins import Admin
from objects.employer import Employer
from admin import DBPASSWORD, DBUSERNAME, DEVPASSWORD

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
            query = f"SELECT * FROM students WHERE fullname='{student.get_fullname()}'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return len(rows) == 1
        except ProgrammingError as error:
            raise Exception("Error while checking for student presence")

    # returns True if the employer is already in the table, False otherwise
    def employer_exists(self, employer : Employer):
        try:
            query = f"SELECT * FROM employers WHERE name='{employer.get_company_name()}'"
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
            query = f"DELETE FROM students WHERE fullname='{student.get_fullname()}'"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to delete student from database")
            print(error)

    # delete entry from the employers table
    def delete_employer(self, employer : Employer):
        if not self.employer_exists(employer) : raise Exception("Employer does not exist")
        try:
            query = f"DELETE FROM employers WHERE name='{employer.get_company_name()}'"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to delete employer from database")
            print(error)

    # prints the contents of the given table
    def show_table_rows(self, table_name):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            return [ row for row in list(self.cursor) ]
        except ProgrammingError as error:
            print("Error while trying to display table data. Make sure table exists")       
            print(error)

    # deletes all the contents of a given table
    def reset_table(self, table_name):
        try:
            password = str(input("Enter development password : "))
            if password == DEVPASSWORD:
                self.cursor.execute(f"DELETE FROM {table_name}")
                return True
            raise Exception("Missing credentials")
            return False
        except ProgrammingError as error:
            message = f"Failed to reset {table_name} table"
            raise Exception(message)
            return False
        