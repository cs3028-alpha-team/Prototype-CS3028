import unittest
import sys

sys.path.append("./")
from business.db_interfaces import DatabaseInterface
from objects.student import Student
from objects.employer import Employer

class DatabaseInterfaceTest(unittest.TestCase):

    # test add_student and student_exists method
    def test_student_creation(self):
        database = DatabaseInterface("alpha_db")
        mattia = Student("Mattia", "Di Profio", "CS3028", "mattia.diprofio@gmail.com", "StrongPassword123")
        database.add_student(mattia)
        self.assertEqual(database.student_exists(mattia), True)

    # test delete_student and student_exists method
    def test_student_deletion(self):
        database = DatabaseInterface("alpha_db")
        mattia = Student("Mattia", "Di Profio", "CS3028", "mattia.diprofio@gmail.com", "StrongPassword123")
        database.add_student(mattia)
        database.delete_student(mattia)
        self.assertEqual(database.student_exists(mattia), False)

    # test add_employer and employer_exists method
    def test_employer_creation(self):
        database = DatabaseInterface("alpha_db")
        NHS = Employer("NHS", "nhs.recruitment@yahoo.com", "StrongPassword10")
        database.add_employer(NHS)
        self.assertEqual(database.employer_exists(NHS), True)

    # test add_employer and employer_exists method
    def test_employer_deletion(self):   
        database = DatabaseInterface("alpha_db")
        NHS = Employer("NHS", "nhs.recruitment@yahoo.com", "StrongPassword10")
        database.add_employer(NHS)
        database.delete_employer(NHS)
        self.assertEqual(database.employer_exists(NHS), False)


if __name__ == "__main__":
    unittest.main()