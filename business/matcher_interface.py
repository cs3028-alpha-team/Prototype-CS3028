from mysql.connector.errors import *
from mysql.connector import *
from .database_interface import DatabaseInterface
from .database_populator import DatabasePopulator
from .mysql_workbench import MySQLWorkbenchInterface
from .matcher import Matcher
from objects.internship import Internship
from objects.student import Student

class MatcherInterface:

    def __init__(self):
        self.workbench = MySQLWorkbenchInterface()
        self.matcher = Matcher()
        # Reset database to ensure fewer errors occur
        self.workbench.destroy_db("alpha_db")
        self.workbench.create_db("alpha_db")

        # Set up populator and database
        self.populator = DatabasePopulator()
        self.db = DatabaseInterface("alpha_db")

        # Reset database tables to make sure fewer errors occur
        self.db.reset_table("students")
        self.db.reset_table("internships")

        # Populate database with data passed via CSV
        self.populator.upload_data("inputs/studentsdata.csv", "inputs/internshipsdata.csv")

        # Fetch students and internships from the database
        student_records = self.db.get_table("students")
        internship_records = self.db.get_table("internships")

        # Create instances of Student and Internship from the fetched records
        students = [Student(record[0], record[2], record[3], record[4]) for record in student_records]
        internships = [Internship(record[0], record[2], record[3], record[4]) for record in internship_records]

        # Match students with internships
        matches, unmatched_students = self.matcher.filter_matches(students, internships)

        # Display the matched students and internships
        for student, internship in matches.items():
            print(f"{student.get_fullname()} matched with {internship.get_title()} at {internship.get_company()}")

        # Display unmatched students
        print("\nUnmatched Students:")
        for student in unmatched_students:
            print(f"{student.get_fullname()} does not have a matching internship.")

            # Download data from database tables into CSV files
            # populator.dowload_data()