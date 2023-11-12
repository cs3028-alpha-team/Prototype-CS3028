import uuid 

# Class to represent placements listings 
class Internship:

    def __init__(self, title, organization, field, min_score):

        self.id = str(uuid.uuid4())
        self.title = title
        self.organization = organization 
        self.field = field
        self.min_score = min_score

    def get_id(self): 
        return self.id

    def get_title(self): 
        return self.title

    def get_organization(self): 
        return self.organization

    def get_field(self): 
        return self.field

    def get_minscore(self): 
        return self.min_score
