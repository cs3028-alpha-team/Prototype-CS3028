import mysql.connector
from mysql.connector.errors import *
from mysql.connector import connect
import sys
sys.path.append("./")
from objects.student import Student
from objects.admins import Admin
from objects.internship import Internship
from admin import DBUSERNAME
import random

from .mysql_workbench import MySQLWorkbenchInterface

from .database_interface import DatabaseInterface
from objects.populator_data import populator_data

class DatabasePopulator:
    
    def __init__(self):
        self.workbench = MySQLWorkbenchInterface()
        self.database = DatabaseInterface("dev_db")
        self.populated = len(self.database.show_table_rows("students")) >= 25 #checks if populator already been used previously

    def populate(self):
        if self.populated: return True
        student_data, internship_data = populator_data["student_data"], populator_data["internship_data"]

        for i in range(0, 30):

            fullname = student_data["fullname"][i]
            degree = student_data["degree"][random.randint(0, 14)]
            score = random.randint(50, 100)
            experience = student_data["experience"][random.randint(0, 3)]

            student = Student(fullname, degree, score, experience)
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
