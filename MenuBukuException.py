from MyException import MyException

class BukuTambahException(MyException):
      def __init__(self, message,*args: object) -> None:
        super().__init__(message, *args)
        
        
class BukuHapusException(MyException):
      def __init__(self, *args: object) -> None:
        super().__init__(*args)
      