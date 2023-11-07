import uuid 

class Recruiter:
    def __init__(self, name, job_title, email, contact_number, organization):
        self.id = str(uuid.uuid4())
        self.name = name   
        self.job_title = job_title
        self.email = email
        self.contact_number = contact_number
        self.organization = organization # instance of Organization class

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_job_title(self):
        return self.job_title

    def get_email(self):
        return self.email

    def get_contact_number(self):
        return self.contact_number

    def get_organization(self):
        return self.organization