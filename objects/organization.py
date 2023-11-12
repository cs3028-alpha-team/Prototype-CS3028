import uuid

# Class to represent the organization advertising a placement
class Organization:

    def __init__(self, name, website, remit, placements):
        self.id = str(uuid.uuid4())
        self.name = name
        self.website = website  
        self.remit = remit
        self.placements = placements

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_website(self):
        return self.website

    def get_remit(self):
        return self.remit

    def get_placements(self):
        return self.placements

