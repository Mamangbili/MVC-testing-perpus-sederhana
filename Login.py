from typing import List, Optional, Union
from LoginException import *
from User import *
class Login:
    @staticmethod
    def login(user:User,dataBaseUsers : List[Union[Admin,User]]):
        userFound : Optional[User] = None
        for userInDb in dataBaseUsers:
            if userInDb.Id == user.Id:
                userFound = userInDb
                break
        else :
            raise LoginIdNotExistException("Id Tidak Terdaftar")
            
        userValidated = Login.validatePassword(userFound, user)
        if userValidated : return userInDb
            
    @staticmethod
    def validatePassword(userInDb:User, user):
        if userInDb.password == user.password :
            return True
        else :
            raise LoginWrongPasswordException("Password Salah")
            
        
        

                
        
            
    