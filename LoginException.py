from MyException import MyException

class LoginWrongPasswordException(MyException):
      def __init__(self, message,*args: object) -> None:
        super().__init__(message,*args)

    
class LoginIdNotExistException(MyException):
      def __init__(self, message,*args: object) -> None:
        super().__init__(message, *args)
        

