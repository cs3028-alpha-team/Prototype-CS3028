import unittest
import sys

sys.path.append("..")
from objects.student import Student
from objects.internship import Internship
from business.database_interface import DatabaseInterface


class DatabaseInterfaceTest(unittest.TestCase):

    def setUp(self):
        self.database = DatabaseInterface("dev_db")
        self.database.reset_table("students")
        self.database.reset_table("internships")

    # test add_student and student_exists method
    def test_student_creation(self):
        mattia = Student("Mattia Di Profio", "Computing Science", 70, "nursing")
        self.database.add_student(mattia)
        self.assertTrue(self.database.student_exists(mattia))

    # test delete_student and student_exists method
    def test_student_deletion(self):
        mattia = Student("John John", "Computing Science", 80, "nursing")
        self.database.add_student(mattia)
        self.database.delete_student(mattia)
        self.assertFalse(self.database.student_exists(mattia))

    # test add_internship and internship_exists method
    def test_internship_creation(self):
        UoA = Internship("Software Enginnering Placement", "University of Aberdeen", "surgery", 70)
        self.database.add_internship(UoA)
        self.assertTrue(self.database.internship_exists(UoA))

    # test add_internship and internship_exists method
    def test_internship_deletion(self):   
        UoA = Internship("Software Enginnering Internship", "University of Edinburgh", "surgery", 70)
        self.database.add_internship(UoA)
        self.database.delete_internship(UoA)
        self.assertFalse(self.database.internship_exists(UoA))

    # Test to ensure that the 'field' value does not exceed the column size
    def test_field_length(self):
        long_field_value = "a" * 100  # Adjust the length according to your column size
        internship = Internship("Title", "Company", long_field_value, 70)
        print("Internship Data:", internship.get_title(), internship.get_company(), internship.get_field(), internship.get_minscore())
        with self.assertRaises(Exception):  # Adjust Exception type according to what your code raises
            self.database.add_internship(internship)

    # Clean up the database after each test case
    def tearDown(self):
        self.database.reset_table("students")
        self.database.reset_table("internships")


if __name__ == "__main__":
    unittest.main()
