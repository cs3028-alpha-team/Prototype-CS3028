# Import built-in modules
import sys
import csv

# Import business-related classes
sys.path.append("../")
from objects.student import Student
from objects.internship import Internship

# Class to execute default and custom matching algorithms
class Matcher:
    
    def __init__(self, score_threshold=5):
        self.score_threshold = score_threshold

    def match_quality(self, student, internship):
        total = 0
        if student.get_score() >= internship.get_minscore():
            total += 1
        if student.get_experience() == internship.get_field():
            total += 1

        return "HIGH   " if total == 2 else "MEDIUM   "

    # Execute defaul matching algorithm
    def default_match(self, students, internships):
        valid_matches = {}
        unmatched_students = []

        # Keep track of free internship positions
        positions_left = { internship.get_id() : internship.get_candidates_wanted() for internship in internships }

        for student in students:
            student_interests = student.get_experience()  
            student_score = student.get_score()  
            
            # Filter internships based on student's interests and fields
            matching_internships = [
                internship for internship in internships 
                if internship.get_field() in student_interests
                and positions_left[internship.get_id()] > 0
            ]
            
            # Find internships with minimum score requirements met
            eligible_internships = [
                internship for internship in matching_internships
                if student_score >= internship.get_minscore() - self.score_threshold
            ]

            if eligible_internships:
                # Choose the internship with the highest minimum score requirement (closest to student's score)
                best_match = max(eligible_internships, key=lambda internship: internship.get_minscore())
                valid_matches[student] = best_match
                positions_left[best_match.get_id()] -= 1

            else:
                unmatched_students.append(student)
        
        # Sort valid matches by the student's score in descending order
        valid_matches = {k: v for k, v in sorted(valid_matches.items(), key=lambda item: item[0].get_score(), reverse=True)}

        # Write valid_matches and unmatched_students to a csv file in 'output' folder   
        try:
            # Store path of output CSV file
            matches_data_path = 'C:\\Users\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\output\\matches.csv'
            with open(matches_data_path, 'w', newline='') as f:
                writer = csv.writer(f)

                # Write found matches to CSV
                for student, internship in valid_matches.items():
                    writer.writerow([
                        self.match_quality(student, internship),
                        student.get_fullname(), 
                        student.get_degree(), 
                        student.get_score(), 
                        student.get_experience(), 
                        f" --> {internship.get_title()}", 
                        internship.get_field(), 
                        internship.get_minscore(), 
                        internship.get_organization()
                    ])

                # Separate the two batches of matches with a new line
                writer.writerow([])

                # Write names of unmatched students to CSV
                for student in unmatched_students:
                    writer.writerow([student.get_fullname()])

        except FileNotFoundError as error:
            raise Exception(error)

        return valid_matches, unmatched_students

    def custom_match(self, students, internships, user_settings):

        matches = {}
        unmatched_students = students.copy()

        # Keep track of free positions left per internship
        positions_left = { internship.get_id() : internship.get_candidates_wanted() for internship in internships }

        # Convert user_settings to a list of (criterion, priority) tuples with integer priorities
        sorted_criteria = sorted([(criterion, settings['priority']) for criterion, settings in user_settings.items() if settings['selected'] == 1], key=lambda x : x[1])

        for criterion, settings in sorted_criteria:
            temp_unmatched = unmatched_students.copy()
            for student in temp_unmatched:
                for internship in internships:
                    if self.is_match(student, internship, criterion) and positions_left[internship.get_id()] > 0:
                        matches[student] = internship
                        positions_left[internship.get_id()] -= 1
                        unmatched_students.remove(student)
                        break

        # Write valid_matches and unmatched_students to a csv file in 'output' folder   
        try:
            # Store path of output CSV file
            matches_data_path = 'C:\\Users\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\output\\matches.csv'
            with open(matches_data_path, 'w', newline='') as f:
                writer = csv.writer(f)

                # Write found matches to CSV
                for student, internship in matches.items():
                    writer.writerow([
                        self.match_quality(student, internship),
                        student.get_fullname(), 
                        student.get_degree(), 
                        student.get_score(), 
                        student.get_experience(), 
                        f" --> {internship.get_title()}",
                        internship.get_field(), 
                        internship.get_minscore(), 
                        internship.get_organization()
                    ])

                # Separate the two batches of matches with a new line
                writer.writerow([])

                # Write names of unmatched students to CSV
                for student in unmatched_students:
                    writer.writerow([student.get_fullname()])

        except FileNotFoundError as error:
            raise Exception(error)

        return matches, unmatched_students

    def is_match(self, student, internship, criterion):
        if criterion == "degree":
            return student.get_degree() == internship.get_field()
        if criterion == "score":
            return student.get_score() >= internship.get_minscore()
        if criterion == "experience":
            return student.get_experience() == internship.get_field()
        return False