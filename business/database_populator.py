import mysql.connector
from mysql.connector.errors import *
from mysql.connector import connect
import sys
sys.path.append("../")
from objects.student import Student
from objects.admins import Admin
from objects.internship import Internship
import random
from .mysql_workbench import MySQLWorkbenchInterface
from .database_interface import DatabaseInterface
from objects.populator_data import populator_data
import csv

class DatabasePopulator:
    
    def __init__(self):
        self.workbench = MySQLWorkbenchInterface()
        self.database = DatabaseInterface("alpha_db")
        self.populated = len(self.database.get_table("students")) >= 25 #checks if populator already been used previously

    def populate(self):
        if self.populated: return True
        student_data, internship_data = populator_data["student_data"], populator_data["internship_data"]

        for i in range(0, 100):

            fullname = student_data["fullname"][i]
            degree = student_data["degree"][random.randint(0, 14)]
            score = random.randint(50, 100)
            experience = student_data["experience"][random.randint(0, 3)]
            study_mode = ["online", "on-campus"][random.randint(0, 1)]
            study_pattern = ["PT", "FT"][random.randint(0, 1)]

            student = Student(fullname, degree, score, experience, study_mode, study_pattern)
            self.database.add_student(student)

        for i in range(0, 10):

            title = internship_data["title"][random.randint(0, 9)]
            company = internship_data["company"][random.randint(0, 9)]
            field = internship_data["field"][random.randint(0, 3)]
            min_score = random.randint(50, 100)

            internship = Internship(title, company, field, min_score)
            self.database.add_internship(internship)

        self.populated = True
        return True

    def upload_data_from_csv(self, students, internships):
        try :
            with open(students, 'r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    student = Student(row[0], row[1], row[2], row[3])
                    self.database.add_student(student)

            with open(internships, 'r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    internship = Internship(row[0], row[1], row[2], row[3])
                    self.database.add_internship(internship)

            return True 

        except Error as error:
            raise Exception(error)
            return False
    
    def dowload_db_to_csv(self):
        try:
            students_data_path = 'C:\\Users\matti\\OneDrive\\Desktop\\CS3028 Project\\output\\studentsdata.csv'
            with open(students_data_path, 'w', newline='') as f:
                writer = csv.writer(f)
                all_students = list(self.database.get_table("students"))

                for row in all_students:
                    writer.writerow(row)

            internships_data_path = 'C:\\Users\matti\\OneDrive\\Desktop\\CS3028 Project\\output\\internshipsdata.csv'
            with open(internships_data_path, 'w', newline='') as f:
                writer = csv.writer(f)
                all_internships = list(self.database.get_table("internships"))
                for row in all_internships:
                    writer.writerow(row)

            return True
        except Error as error:
            raise Exception(error)
            return False