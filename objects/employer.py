import uuid 

# NOTE : fields classes will need to be validated 

class Employer:
    def __init__(self, company_name : str, email : str, password : str):
        self.id = str(uuid.uuid4())
        self.company_name = self.set_company_name(company_name)
        self.email = self.set_email(email)
        self.password = self.set_password(password)

    # getter methods 
    def get_company_name(self): return self.company_name

    def get_id(self) : return self.id
    
    def get_email(self) : return self.email

    def get_password(self) : return self.password # will need to be protected when we get to auth
    
    # setter methods    
    def set_company_name(self, company_name : str): self.company_name = company_name

    def set_email(self, email): self.email = email 

    def set_email(self, email) : self.email = email

    def set_password(self, password) : self.password = password