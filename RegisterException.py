from MyException import MyException

class RegisterIdAlreadyExistException(MyException):
      def __init__(self, message,*args: object) -> None:
        super().__init__(message,*args)

class RegisterPasswordNotMatchException(MyException):
      def __init__(self, message,*args: object) -> None:
        super().__init__(message,*args)



