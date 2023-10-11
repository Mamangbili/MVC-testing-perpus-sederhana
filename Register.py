from RegisterException import *
from User import User

class Register: 
    def __init__(self,dummyDataUser):
        self.dummyDataUser = dummyDataUser
    
    def create(self,Id,password1,password2):
        self._validateId(Id)
        self._validatePassword(password1,password2)
        
        return User(Id, password1)
    
    def _validatePassword(self,password1,password2):
        if password1 == password2:return
        else: raise RegisterPasswordNotMatchException("Password tidak sama")
    
    def _validateId(self,Id):
        for user in self.dummyDataUser:
            if user.Id == Id:
                raise RegisterIdAlreadyExistException("Id sudah digunakan")
        return
        

    