import uuid 

class Student:
    def __init__(self, fullname : str, degree : str, score : int, experience : str):
        self.id = str(uuid.uuid4())
        self.fullname = fullname
        self.degree = degree
        self.score = score  
        self.experience = experience

    # getter methods        
    def get_id(self): return self.id
    def get_fullname(self): return self.fullname
    def get_degree(self): return self.degree
    def get_score(self): return self.score
    def get_experience(self): return self.experience