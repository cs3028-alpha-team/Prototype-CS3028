import uuid 

class Student:
    def __init__(self, fullname, degree, score, experience, study_mode, study_pattern):
        self.id = str(uuid.uuid4())
        self.fullname = fullname
        self.degree = degree
        self.score = score  
        self.study_mode = study_mode
        self.study_pattern = study_pattern
        self.experience = experience
     
    def get_id(self): 
        return self.id

    def get_fullname(self): 
        return self.fullname

    def get_degree(self):
         return self.degree

    def get_score(self): 
        return self.score

    def get_experience(self): 
        return self.experience

    def get_study_pattern(self) : 
        return self.study_pattern

    def get_study_mode(self) : 
        return self.study_mode