# Import built-in modules
import mysql.connector
from mysql.connector.errors import *
from mysql.connector import connect
import sys
import random
import csv

# Import business-related classes
sys.path.append("../")
from objects.student import Student
from objects.admins import Admin
from objects.internship import Internship
from .mysql_workbench import MySQLWorkbenchInterface
from .database_interface import DatabaseInterface
from objects.populator_data import populator_data

# Class allows for automated population of database
class DatabasePopulator:
    
    def __init__(self):
        # Set up auxiliary interfaces for database manipulation
        self.workbench = MySQLWorkbenchInterface()
        self.database = DatabaseInterface("alpha_db")
        # Checks if database is non-empty
        self.populated = len(self.database.get_table("students")) >= 10

    # Populate database using data from 'objects/populator_data.py'
    def random_populate(self):
        if self.populated: 
            return False

        # Extract fake data
        student_data, internship_data = populator_data["student_data"], populator_data["internship_data"]

        # Populate 'students' table with 100 student entries
        for i in range(0, 100):

            fullname = student_data["fullname"][i]
            degree = student_data["degree"][random.randint(0, 14)]
            score = random.randint(50, 100)
            experience = student_data["experience"][random.randint(0, 3)]
            study_mode = ["online", "on-campus"][random.randint(0, 1)]
            study_pattern = ["PT", "FT"][random.randint(0, 1)]

            # Construct and insert the Student instance
            student = Student(fullname, degree, score, experience, study_mode, study_pattern)
            self.database.add_student(student)

        # Populate 'internships' table with 15 internship listings
        for i in range(0, 15):

            title = internship_data["title"][random.randint(0, 9)]
            company = internship_data["company"][random.randint(0, 9)]
            field = internship_data["field"][random.randint(0, 3)]
            min_score = random.randint(50, 100)

            # Construct and insert the Internship instance
            internship = Internship(title, company, field, min_score)
            self.database.add_internship(internship)

        self.populated = True
        return True

    # Populate database via CSV file uplodad
    def populate_via_csv(self, students, internships):
        try :
            with open(students, 'r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    # Create a Student object for every row in file
                    student = Student(row[0], row[1], row[2], row[3], row[4], row[5])
                    self.database.add_student(student)

            with open(internships, 'r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    # Create an Internship object for every row in file
                    internship = Internship(row[0], row[1], row[2], row[3])
                    self.database.add_internship(internship)
            return True 

        except Error as error:
            raise Exception(error)
            return False
    
    # Download database into a CSV file
    def dowload_db_to_csv(self):
        try:
            # Store path where 'students' output file will be located
            students_data_path = 'C:\\Users\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\output\\studentsdata.csv'
            with open(students_data_path, 'w', newline='') as f:
                writer = csv.writer(f)

                # Extract all students in 'students' table 
                all_students = list(self.database.get_table("students"))

                # Write each student entry into CSV file
                for row in all_students:
                    writer.writerow(row)

            # Store path where 'internships' output file will be located
            internships_data_path = 'C:\\Users\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\output\\internshipsdata.csv'
            with open(internships_data_path, 'w', newline='') as f:
                writer = csv.writer(f)

                # Extract all internships in 'internships' table
                all_internships = list(self.database.get_table("internships"))

                # Write each internship entry into the CSV file
                for row in all_internships:
                    writer.writerow(row)

            return True
        except Error as error:
            raise Exception(error)
            return False