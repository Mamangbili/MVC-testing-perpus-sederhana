from abc import ABC

class Authorize(ABC):pass
    
class User:
    def __init__(self,id,password):
        self.Id=id
        self.password=password
        self.loginStatus = False         
                   
    def __eq__(self, other):
        if isinstance(other, User):
            return (self.Id, self.password) == (other.Id, other.password)
        return False

class Admin(User, Authorize):
    def __init__(self,Id,Password):
        super().__init__(Id,Password)
        

        