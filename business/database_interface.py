from mysql.connector.errors import *
from mysql.connector import *
import sys
sys.path.append("../")
from objects.student import Student
from objects.admins import Admin
from objects.internship import Internship

class DatabaseInterface() :
    def __init__(self, db_name) :
        # intitialise connection to database and set up cursor to execute SQL queries
        self.connection = connect(host = "localhost", user = "root", password = "LanaBanana100?", database = db_name)
        self.cursor = self.connection.cursor(buffered=True)

        # create the 'students' table, if already exist then command is ignored
        try: self.cursor.execute("CREATE TABLE students (fullname VARCHAR(100), studentID VARCHAR(36) , degree VARCHAR(100), score TINYINT(100), experience ENUM('surgery', 'dentistry', 'nursing', 'nutrition', 'medicine'), study_mode VARCHAR(100), study_pattern VARCHAR(2))")
        except ProgrammingError as error: pass

        # create the 'employers' table, if already exist then command is ignored
        try: self.cursor.execute("CREATE TABLE internships (title VARCHAR(50), internshipID VARCHAR(36), company VARCHAR(50), field ENUM('surgery', 'dentistry', 'nursing', 'nutrition','medicine'), minScore INT(100))")
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
    def internship_exists(self, internship : Internship):
        try:
            query = f"SELECT * FROM internships WHERE title='{internship.get_title()}' AND company='{internship.get_company()}'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return len(rows) == 1
        except ProgrammingError as error:
            raise Exception("Error while checking for internship presence")


    # create new entry into the student table
    def add_student(self, student : Student):
        if self.student_exists(student) : raise Exception("Student with given credentials already exists")
        try:
            query = f"""
            INSERT INTO students (fullname, studentID, degree, score, experience, study_mode, study_pattern)
            VALUES ('{student.get_fullname()}', '{student.get_id()}', '{student.get_degree()}', 
                    '{student.get_score()}', '{student.get_experience()}', '{student.get_study_mode()}', 
                    '{student.get_study_pattern()}')
            """
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to create new student entry")
            print(error)

    # create new entry into the employers table
    def add_internship(self, internship : Internship):
        if self.internship_exists(internship) : raise Exception("Internship with given credentials already exists")
        try:
            query = f"INSERT INTO internships (title, internshipID, company, field, minScore) VALUES ('{internship.get_title()}', '{internship.get_id()}', '{internship.get_company()}', '{internship.get_field()}', '{internship.get_minscore()}')"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to create new internship entry")
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
    def delete_internship(self, internship : Internship):
        if not self.internship_exists(internship) : raise Exception("Internship does not exist")
        try:
            query = f"DELETE FROM internships WHERE title='{internship.get_title()}' AND company='{internship.get_company()}'"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to delete internship from database")
            print(error)


    # prints the contents of the given table
    def get_table(self, table_name):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            return [ row for row in list(self.cursor) ]
        except ProgrammingError as error:
            print("Error while trying to display table data. Make sure table exists")       
            print(error)

    # deletes all the contents of a given table
    def reset_table(self, table_name):
        try:
            self.cursor.execute(f"DELETE FROM {table_name}")
            self.connection.commit()
            return True
        except ProgrammingError as error:
            message = f"Failed to reset {table_name} table"
            raise Exception(message)
            return False
        