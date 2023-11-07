import uuid 

class Internship:
    def __init__(self, title, organization, field, min_score):
        self.id = str(uuid.uuid4())
        self.title = title
        self.organization = organization # will be changed to an Organization class instance later on
        self.field = field
        self.min_score = min_score

        # self.description = description
        # self.outcomes = outcomes
        # self.location = location
        # self.recruiter = recruiter # instance of Recruiter class
        # self.skills_required = skills_required

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

    # def get_location(self):
    #     return self.location

    # def get_description(self):
    #     return self.description

    # def get_outcomes(self):
    #     return self.outcomes

    # def get_skills_required(self):
    #     return self.skills_required

    # def get_recruiter(self):
    #     return self.recruiter