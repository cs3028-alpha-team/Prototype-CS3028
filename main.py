from objects.student import Student
from objects.internship import Internship
from business.matcher import Matcher
from business.database_interface import DatabaseInterface
from business.database_populator import DatabasePopulator
from business.mysql_workbench import MySQLWorkbenchInterface

if __name__ == "__main__":

    #create and populate the database
    #run the matcher class 
    pass

    workbench = MySQLWorkbenchInterface()
    matcher = Matcher()
        
    # Reset database to ensure fewer errors occur
    workbench.destroy_db("alpha_db")
    workbench.create_db("alpha_db")

    # Set up populator and database
    populator = DatabasePopulator()
    db = DatabaseInterface("alpha_db")

    # Reset database tables to make sure fewer errors occur
    db.reset_table("students")
    db.reset_table("internships")

    # Populate database with data passed via CSV
    populator.populate()

    # Fetch students and internships from the database
    student_records = db.get_table("students")
    internship_records = db.get_table("internships")

    # Create instances of Student and Internship from the fetched records
    students = [Student(record[0], record[2], record[3], record[4], record[5], record[6]) for record in student_records]
    internships = [Internship(record[0], record[2], record[3], record[4]) for record in internship_records]

    # Match students with internships
    matches, unmatched_students = matcher.filter_matches(students, internships)

    # Display the matched students and internships
    for student, internship in matches.items():
        print(f"{student.get_fullname()} matched with {internship.get_title()} at {internship.get_organization()}")

    # Display unmatched students
    print("\nUnmatched Students:")
    for student in unmatched_students:
        print(f"{student.get_fullname()} does not have a matching internship.")
