class BukuTambahException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __repr__(self) -> str:
        return super().__repr__()
        
class BukuHapusException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
    def __repr__(self) -> str:
        return super().__repr__()