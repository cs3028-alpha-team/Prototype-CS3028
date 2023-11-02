from mysql.connector.errors import *
from mysql.connector import *
from business.database_interface import DatabaseInterface
from business.database_populator import DatabasePopulator
from business.mysql_workbench import MySQLWorkbenchInterface
from matcher import Matcher

from objects.internship import Internship
from objects.student import Student

if __name__ == "__main__":
    workbench = MySQLWorkbenchInterface()
    # Reset database to ensure fewer errors occur
    workbench.destroy_db("dev_db")
    workbench.create_db("dev_db")

    # Set up populator and database
    populator = DatabasePopulator()
    db = DatabaseInterface("dev_db")

    # Reset database tables to make sure fewer errors occur
    print(" RESETTING DB...\n")
    db.reset_table("students")
    db.reset_table("internships")

    # Populate database with data passed via CSV
    populator.upload_data("students.txt", "internships.txt")

    # Display contents of tables in the console
    print(" POPULATING DB...\n")
    print("\n - STUDENTS - \n", db.get_table("students"))
    print()
    print("\n - INTERNSHIPS - \n", db.get_table("internships"))

    # Fetch students and internships from the database
    student_records = db.get_table("students")
    internship_records = db.get_table("internships")

    # Create instances of Student and Internship from the fetched records
    students = [Student(record[0], record[2], record[3], record[4]) for record in student_records]
    internships = [Internship(record[0], record[2], record[3], record[4]) for record in internship_records]

    # Create an instance of the Matcher class
    matcher = Matcher()

    # Match students with internships
matches, unmatched_students = matcher.filter_matches(students, internships)

# Display the matched students and internships
for student, internship in matches.items():
    print(f"{student.get_fullname()} matched with {internship.get_title()} at {internship.get_company()}")

# Display unmatched students
print("\nUnmatched Students:")
for student in unmatched_students:
    print(f"{student.get_fullname()} does not have a matching internship.")

    # Download data from database tables into CSV files
    #populator.dowload_data()