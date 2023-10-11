class LoginWrongPasswordException(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message = message
        
    def __repr__(self) -> str:
        return super().__repr__()

    
class LoginWrongIdException(Exception):
    def __init__(self,message):
        super().__init__(message)
        
    def __repr__(self) -> str:  
        return super().__repr__()
        

