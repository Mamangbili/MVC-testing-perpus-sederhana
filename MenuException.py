from MyException import MyException

class MenuWrongException(MyException):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
    



        