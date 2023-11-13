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
        db = DatabaseInterface("alpha_db")
        student = Student("John", "Medicine", 80, "nursing", "online", "FT")

        # Remove student if already in database
        try: db.delete_student(student)
        except Exception: pass

        db.add_student(student)
        self.assertTrue(db.student_exists(student))

    # Test delete_student and student_exists method
    def test_student_deletion(self):
        db = DatabaseInterface("alpha_db")
        student = Student("Kate", "Midwifery", 90, "surgery", "oncampus", "FT")

        # Remove student if already in database
        try: db.delete_student(student)
        except Exception: pass

        db.add_student(student)
        db.delete_student(student)
        self.assertFalse(db.student_exists(student)) 

    # Test add_internship and internship_exists method
    def test_internship_creation(self):
        db = DatabaseInterface("alpha_db")
        internship = Internship("Junior Doctor Placement", "NHS", "medicine", 90)

        # Remove internship if already in database
        try: db.delete_internship(internship)
        except Exception: pass

        db.add_internship(internship)
        self.assertTrue(db.internship_exists(internship)) 

    # Test delete_internship and internship_exists method
    def test_internship_deletion(self):   
        db = DatabaseInterface("alpha_db")
        internship = Internship("Junior Doctor Placement", "NHS", "medicine", 90)

        # Remove internship if already in database
        try: db.delete_internship(internship)
        except Exception: pass

        db.add_internship(internship)
        db.delete_internship(internship)
        self.assertFalse(db.internship_exists(internship))     

if __name__ == "__main__":
    unittest.main()