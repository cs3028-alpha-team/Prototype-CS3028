import uuid 

# Class to represent users with admin priviliges
class Admin:

    def __init__(self, fullname, email, password):
        self.id = str(uuid.uuid4())
        self.fullname = fullname
        self.email = email
        self.password = password

    def get_fullname(self): 
        return self.fullname

    def get_email(self) : 
        return self.email

    def get_password(self) : 
            return self.password