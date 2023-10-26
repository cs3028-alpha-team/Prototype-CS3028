import unittest
import sys

sys.path.append("..")
from objects.student import Student
from objects.internship import Internship
from business.database_interface import DatabaseInterface


class DatabaseInterfaceTest(unittest.TestCase):

    # test add_student and student_exists method
    def test_student_creation(self):
        database = DatabaseInterface("dev_db")
        database.reset_table("students")
        mattia = Student("Mattia Di Profio", "Computing Science", 70, "nursing")
        database.add_student(mattia)
        self.assertEqual(database.student_exists(mattia), True)

    # test delete_student and student_exists method
    def test_student_deletion(self):
        database = DatabaseInterface("dev_db")
        mattia = Student("John John", "Computing Science", 80, "nursing")
        database.add_student(mattia)
        database.delete_student(mattia)
        self.assertEqual(database.student_exists(mattia), False)

    # test add_internship and internship_exists method
    def test_internship_creation(self):
        database = DatabaseInterface("dev_db")
        database.reset_table("internships")
        UoA = Internship("Software Enginnering Placement", "University of Aberdeen", "surgery", 70)
        database.add_internship(UoA)
        self.assertEqual(database.internship_exists(UoA), True)

    # test add_internship and internship_exists method
    def test_internship_deletion(self):   
        database = DatabaseInterface("dev_db")
        UoA = Internship("Software Enginnering Internship", "University of Edinburgh", "surgery", 70)
        database.add_internship(UoA)
        database.delete_internship(UoA)
        self.assertEqual(database.internship_exists(UoA), False)

if __name__ == "__main__":
    unittest.main()