from abc import ABC, abstractmethod

class Authorize(ABC):pass
    
class User:
    def __init__(self,id,password):
        self.Id=id
        self.password=password
        self.loginStatus = False
    
    
            
                   
class Admin(User, Authorize):
    def __init__(self,Id,Password):
        super().__init__(Id,Password)
        

        