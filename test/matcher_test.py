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
from business.matcher import Matcher

# Class set-up to run unit tests on the DatabasePopulator class methods
class MatcherTest(unittest.TestCase):

    # Test defualt matching algorithm against small dataset
    def test_default_match(self):

        db = DatabaseInterface("alpha_db")

        # Fetch students and internships from the database
        student_records = db.get_table("students")
        internship_records = db.get_table("internships")

        # Create instances of Student and Internship from the fetched records
        students = [Student(record[0], record[2], record[3], record[4], record[5], record[6]) for record in student_records]
        internships = [Internship(record[0], record[2], record[3], record[4], record[5]) for record in internship_records]

        # Run default matching algorithm
        matcher = Matcher()
        matcher.default_match(students, internships)        

        acceptable_matches = 0 # Store number of matches which satisfy the criterias
        acceptability_threshold = 0 # Algorithm acceptable if 75% of matches are valid (% can be changed)
        matches_path = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\output\\matches.csv'

        try:
            with open(matches_path, 'r') as f:
                reader = csv.reader(f)
                matches = [ match[1:] for match in list(reader) ]
                acceptability_threshold = round((0.50 * len(matches) - 1))
                
                for match in matches:
                    if (len(match) < 2):
                        continue
                    student_score = match[2]
                    student_experience = match[3]
                    internship_minscore = match[6]
                    internship_field = match[5]

                    if student_score >= internship_minscore or student_experience == internship_field:
                       acceptable_matches += 1

        except FileNotFoundError as error:
            print(error)

        self.assertGreaterEqual(acceptable_matches, acceptability_threshold)

        # Default algorithm should fail for acceptability threshold higher than 50%
        acceptability_threshold = round((0.60 * len(matches) - 1))
        self.assertLessEqual(acceptable_matches, acceptability_threshold)

    # Test custom matching algorithm against small dataset
    def test_custom_match(self):
        
        db = DatabaseInterface("alpha_db")

        # Fetch students and internships from the database
        student_records = db.get_table("students")
        internship_records = db.get_table("internships")

        # Create instances of Student and Internship from the fetched records
        students = [Student(record[0], record[2], record[3], record[4], record[5], record[6]) for record in student_records]
        internships = [Internship(record[0], record[2], record[3], record[4], record[5]) for record in internship_records]

        # Run custom matching algorithm with test settings
        matcher = Matcher()
        test_settings = {
            'degree' : {'selected' : 1,'priority' : 3},
            'score' : {'selected' : 1,'priority' : 2},
            'experience' : {'selected' : 1,'priority' : 1},
            'study_mode' : {'selected' : 0,'priority' : 0},
            'study_pattern' : {'selected' : 0,'priority' : 0}
        }        

        matcher.custom_match(students, internships, test_settings)

        acceptable_matches = 0 # Store number of matches which satisfy the criterias
        acceptability_threshold = 0 # Algorithm acceptable if 75% of matches are valid (% can be changed)
        matches_path = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\output\\matches.csv'

        try:
            with open(matches_path, 'r') as f:
                reader = csv.reader(f)
                matches = [ match[1:] for match in list(reader) ]
                acceptability_threshold = round((0.70 * len(matches) - 1))
                
                for match in matches:
                    if (len(match) < 2):
                        continue
                    student_score = match[2]
                    student_experience = match[3]
                    internship_minscore = match[6]
                    internship_field = match[5]

                    if student_score >= internship_minscore or student_experience == internship_field:
                       acceptable_matches += 1

        except FileNotFoundError as error:
            print(error)

        self.assertGreaterEqual(acceptable_matches, acceptability_threshold)

        # Custom algorithm should fail for acceptability threshold higher than 75%
        acceptability_threshold = round((0.75 * len(matches) - 1))
        self.assertLessEqual(acceptable_matches, acceptability_threshold)

if __name__ == "__main__":
    unittest.main()