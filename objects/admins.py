import uuid 

# NOTE : fields classes will need to be validated 

class Admin:
    def __init__(self, name : str, surname : str, email : str, password : str):
        self.id = str(uuid.uuid4())
        self.fullname = self.set_name(name, surname)
        self.email = self.set_email(email)
        self.password = self.set_password(password)

    # getter methods 
    def get_fullname(self): return f"{self.name} {self.surname}"

    def get_email(self) : return self.email

    def get_password(self) : return self.password # will need to be protected when we get to auth
    
    # setter methods    
    def set_name(self, name : str, surname : str):
        self.name = name    
        self.surname = surname

    def set_email(self, email): self.email = email 

    def set_email(self, email) : self.email = email

    def set_password(self, password) : self.password = password