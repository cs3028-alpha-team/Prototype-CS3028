import unittest
import sys

sys.path.append("./")
from business.db_interfaces import *

class DatabaseInterfacesTest(unittest.TestCase):

    def test_db_creation(self):
        workbench = MySQLWorkbenchInterface()
        workbench.create_db("test_db")
        self.assertEqual(workbench.db_exists("test_db"), True)

    def test_db_destruction(self):
        workbench = MySQLWorkbenchInterface()
        workbench.destroy_db("test_db")
        self.assertEqual(workbench.db_exists("test_db"), False)

    def test_student_creation(self):
        database = DatabaseInterface("alpha_db")
        mattia = Student("Mattia", "Di Profio", "CS3028", "mattia.diprofio@gmail.com", "StrongPassword123")
        database.add_student(mattia)
        self.assertEqual(database.student_exists(mattia), True)

    def test_student_deletion(self):
        database = DatabaseInterface("alpha_db")
        mattia = Student("Mattia", "Di Profio", "CS3028", "mattia.diprofio@gmail.com", "StrongPassword123")
        database.add_student(mattia)
        database.delete_student(mattia)
        self.assertEqual(database.student_exists(mattia), False)

    def test_employer_creation(self):
        database = DatabaseInterface("alpha_db")
        NHS = Employer("NHS", "nhs.recruitment@yahoo.com", "StrongPassword10")
        database.add_employer(NHS)
        self.assertEqual(database.employer_exists(NHS), True)

    def test_employer_deletion(self):   
        database = DatabaseInterface("alpha_db")
        NHS = Employer("NHS", "nhs.recruitment@yahoo.com", "StrongPassword10")
        database.add_employer(NHS)
        database.delete_employer(NHS)
        self.assertEqual(database.employer_exists(NHS), False)


if __name__ == "__main__":
    unittest.main()