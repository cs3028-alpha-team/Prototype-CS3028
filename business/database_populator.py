import mysql.connector
from mysql.connector.errors import *
from mysql.connector import connect
import sys
sys.path.append("./")
from objects.student import Student
from objects.admins import Admin
from objects.employer import Employer
from admin import DBPASSWORD, DBUSERNAME, DEVPASSWORD

from .mysql_workbench import MySQLWorkbenchInterface

from .database_interface import DatabaseInterface
from objects.populator_data import students_data, employers_data

class DatabasePopulator:
    
    def __init__(self):
        self.workbench = MySQLWorkbenchInterface()
        self.database = DatabaseInterface("alpha_db")
        self.populated = len(self.database.show_table_rows("students")) >= 25 #checks if populator already been used previously

    def populate(self):

        # if entries already in database ignore command
        if self.populated:
            return True

        dev_password = str(input("Enter development password : "))
        if (dev_password != DEVPASSWORD):
            raise Exception("Missing credentials")
            return False

        #populate database with 50 students and 15 employers
        
        for i in range(0, 30):
            name = students_data["firstnames"][i]
            surname = students_data["surnames"][i]
            course_code = students_data["course_codes"][i]
            email = f"{name}{surname}@email.com"
            password = "FakePassword123?"
            student = Student(name, surname, course_code, email, password)
            self.database.add_student(student)

        for i in range(0, 10):
            company_name = employers_data["company_names"][i]
            email = f"{''.join(company_name.split())}@corporate.com"
            password = "CorporateWeapon123!"
            employer = Employer(company_name, email, password)
            self.database.add_employer(employer)

        self.populated = True
        return True
