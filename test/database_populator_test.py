# Import built-in modules
import unittest
import sys
import csv 

# Import business-related classes
sys.path.append("..")
from objects.student import Student
from objects.internship import Internship
from business.database_interface import DatabaseInterface
from business.database_populator import DatabasePopulator

# Class set-up to run unit tests on the DatabasePopulator class methods
class DatabasePopulatorTest(unittest.TestCase):
    
    # Test population with randomly generated entries
    def test_random_populator(self):
        db = DatabaseInterface("alpha_db")
        # Reset database
        db.reset_table("students")
        db.reset_table("internships")

        # Populate database
        populator = DatabasePopulator()
        populator.random_populate()

        student_table = db.get_table("students")
        internship_table = db.get_table("internships")  

        self.assertEqual(len(student_table), 100)
        self.assertEqual(len(internship_table), 15)

    # Test population via csv dump
    def test_csv_upload(self):
        db = DatabaseInterface("alpha_db")

        # Reset database
        db.reset_table("students")
        db.reset_table("internships")

        # Populate database
        populator = DatabasePopulator()
        student_input_path = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\inputs\\studentsdata.csv'
        internship_input_path = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\inputs\\internshipsdata.csv'
        populator.populate_via_csv(student_input_path, internship_input_path)

        student_table = db.get_table("students")
        internship_table = db.get_table("internships")  

        self.assertEqual(len(student_table), 100)
        self.assertEqual(len(internship_table), 15)

    # Test downloading database to csv
    def test_db_download(self):
        db = DatabaseInterface("alpha_db")

        # Reset database
        db.reset_table("students")
        db.reset_table("internships")

        # Populate database
        populator = DatabasePopulator()
        student_input_path = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\inputs\\studentsdata.csv'
        internship_input_path = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\inputs\\internshipsdata.csv'
        populator.populate_via_csv(student_input_path, internship_input_path)

        # Download database to csv
        populator.dowload_db_to_csv()
        students_output_path = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\output\\studentsdata.csv'
        internships_output_path = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\output\\internshipsdata.csv'
        
        line_count = 0
        with open(students_output_path, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                line_count += 1

        self.assertEqual(line_count, 100)

        line_count = 0
        with open(internships_output_path, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                line_count += 1

        self.assertEqual(line_count, 15)

if __name__ == "__main__":
    unittest.main()