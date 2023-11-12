# Import built-in modules
import unittest
import sys

# Import business-related classes
sys.path.append("..")
from objects.student import Student
from objects.internship import Internship
from business.database_interface import DatabaseInterface
from business.database_populator import DatabasePopulator
from business.matcher import Matcher

# Class set-up to run unit tests on the DatabasePopulator class methods
class DatabasePopulatorTest(unittest.TestCase):
    
    # Test defualt matching algorithm against small dataset
    def test_default_match(self):
        pass


    # Test custom matching algorithm against small dataset
    def test_custom_match(self):
        pass

if __name__ == "__main__":
    unittest.main()