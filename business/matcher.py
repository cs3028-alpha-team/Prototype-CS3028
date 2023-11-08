import sys
import csv
sys.path.append("../")
from objects.student import Student
from objects.internship import Internship

class Matcher:
    
    def __init__(self, score_threshold=5):
        self.score_threshold = score_threshold

    def filter_matches(self, students, internships):
        valid_matches = {}
        unmatched_students = []

        for student in students:
            student_interests = student.get_experience()  
            student_score = student.get_score()  
            
            # Filter internships based on student's interests and fields
            matching_internships = [
                internship for internship in internships 
                if internship.get_field() in student_interests
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
            else:
                unmatched_students.append(student)
        
        # Sort valid matches by the student's score in descending order
        valid_matches = {k: v for k, v in sorted(valid_matches.items(), key=lambda item: item[0].get_score(), reverse=True)}

        # write valid_matches and unmatched_students to a csv file in 'output' folder   
        try:
            matches_data_path = 'C:\\Users\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\output\\matches.csv'
            with open(matches_data_path, 'w', newline='') as f:
                writer = csv.writer(f)
                for student, internship in valid_matches.items():
                    writer.writerow([student.get_fullname(), internship.get_title(), internship.get_organization()])

                writer.writerow([])

                for student in unmatched_students:
                    writer.writerow([student.get_fullname()])

        except FileNotFoundError as error:
            raise Exception(error)

        return valid_matches, unmatched_students







