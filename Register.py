from RegisterException import *
from User import User

class Register: 
    def __init__(self,dummyDataUser):
        self.dummyDataUser = dummyDataUser
    
    def create(self,Id,password1,password2):
        self._validateId(Id)
        self._validateSamePassword(password1,password2)
        self._validate8Digit(password1)
        self._validateMustContain(password1)
        
        return User(Id, password1)
    
    
    def _validateSamePassword(self,password1,password2):
        if password1 == password2:return
        else: raise RegisterPasswordNotMatchException("Password tidak sama")
    
    def _validateId(self,Id):
        for user in self.dummyDataUser:
            if user.Id == Id:
                raise RegisterIdAlreadyExistException("Id sudah digunakan")
        return
    
    def _validate8Digit(self,password):
        if len(password) >= 8: return
        raise RegisterPasswordRulesException("Password harus 8 digit atau lebih")
        
    def _validateMustContain(self,password):
        import re
        regex = r'^(?=.*[A-Z])(?=.*\d).*$'
        if bool(re.match(regex,password)): return
        raise RegisterPasswordRulesException("Password harus memiliki minimal 1 Angka dan huruf besar")
        

    