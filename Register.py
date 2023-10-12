from RegisterException import *
from User import User

class Register: 
    def __init__(self,dummyDataUser):
        self.dummyDataUser = dummyDataUser
    
    def create(self,Id,password1,password2):
        self.validateId(Id)
        self.validateSamePassword(password1,password2)
        self.validate8Digit(password1)
        self.validateMustContainDigitAndUpperCase(password1)
        
        return User(Id, password1)
    
    
    def validateSamePassword(self,password1,password2):
        if password1 == password2:return
        else: raise RegisterPasswordNotMatchException("Password tidak sama")
    
    def validateId(self,Id):
        for user in self.dummyDataUser:
            if user.Id == Id:
                raise RegisterIdAlreadyExistException("Id sudah digunakan")
        return
    
    def validate8Digit(self,password):
        if len(password) >= 8: return
        raise RegisterPasswordRulesException("Password harus 8 digit atau lebih")
        
    def validateMustContainDigitAndUpperCase(self,password):
        import re
        pattern = r'^(?=.*[A-Z])(?=.*\d).*$'
        if bool(re.match(pattern,password)): return
        raise RegisterPasswordRulesException("Password harus memiliki minimal 1 Angka dan huruf besar")
        

    