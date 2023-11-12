# Import built-in modules
import unittest
import sys

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
        pass

    # Test population via csv dump
    def test_csv_upload(self):
        pass

    # Test downloading database to csv
    def test_db_download(self):
        pass

if __name__ == "__main__":
    unittest.main()