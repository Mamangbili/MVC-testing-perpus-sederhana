from LoginException import *

class Login:
    @staticmethod
    def login(user,dataBaseUser):
        userInDb = None
        for user_db in dataBaseUser:
            if user_db.Id == user.Id:
                userInDb = user_db
                break
        else :
            raise LoginWrongIdAndPasswordException("Id dan Password salah")
            
        if userInDb.password == user.password :
            user.loginStatus=True
        else :
            raise LoginWrongIdException("Password Salah")
            
        
        

                
        
            
    