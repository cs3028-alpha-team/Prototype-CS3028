# Import built-in modules
import unittest
import sys

# Import related classes
sys.path.append("..")
from objects.student import Student
from objects.internship import Internship
from business.database_interface import DatabaseInterface

# Class set-up to run unit tests on the DatabaseInterface class methods
class DatabaseInterfaceTest(unittest.TestCase):

    # Test add_student and student_exists method
    def test_student_creation(self):
        pass

    # Test delete_student and student_exists method
    def test_student_deletion(self):
        pass

    # Test add_internship and internship_exists method
    def test_internship_creation(self):
        pass

    # Test add_internship and internship_exists method
    def test_internship_deletion(self):   
        pass

if __name__ == "__main__":
    unittest.main()