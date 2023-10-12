class MyException(Exception):
    def __init__(self,message, *args: object) -> None:
        super().__init__(*args)
        self.message = message