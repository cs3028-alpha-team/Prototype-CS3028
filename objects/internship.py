import uuid 

# NOTE : fields classes will need to be validated 

class Internship:
    def __init__(self, title : str, company : str, field : str, min_score : int):
        self.id = str(uuid.uuid4())
        self.title = title
        self.company = company
        self.field = field
        self.min_score = min_score

    # getter methods 
    def get_id(self): return self.id
    def get_title(self): return self.title
    def get_company(self): return self.company
    def get_field(self): return self.field
    def get_minscore(self): return self.min_score