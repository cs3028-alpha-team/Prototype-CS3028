import uuid 

# Class to represent placements listings 
class Internship:

    def __init__(self, title, organization, field, min_score, candidates_wanted):

        self.id = str(uuid.uuid4())
        self.title = title
        self.organization = organization 
        self.field = field
        self.min_score = min_score
        self.candidates_wanted = candidates_wanted

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

    def get_candidates_wanted(self):
        return self.candidates_wanted