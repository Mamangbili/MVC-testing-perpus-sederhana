from MenuException import *
from User import User
from Login import Login

class MenuUI:
    def __init__(self):
        self.input = None
        
    
    def menuAwal(self): 
        print("""
        Selamat Datang di Perpus 1
        ==========================
        1. login
        2. register
        """)
        
    def inputMenu(self):
        Input = input("Silahkan masukan menu diatas")
        try :
            Input = int(Input)
            if 0 < Input < 3:
                return Input
            else:
                raise ValueError("Tidak sesuai dengan Menu")
        except ValueError as err:
            raise MenuWrongException(err)
            
    def tampilanListBuku(self,koleksiBuku):
        koleksiBuku = koleksiBuku.getKoleksi()
        for i,buku in enumerate(koleksiBuku,1):
            print(f"{i}. {buku}")
    
    def tampilanUser(self):
        print('''
        1. lihat buku
        2. log out
        =================
        ''')
    
    def inputUser(self):
        userInput = input("masukan pilihan menu : ")
        try :
            Input = int(userInput)
            if 0 < Input < 3:
                return userInput
            else:
                raise ValueError("Tidak sesuai dengan Menu")
        except ValueError as err:
            raise MenuWrongException(err)
    
    
    def tampilanAdmin(self):
        print('''
        1. lihat buku
        2. tambah buku
        3. hapus buku
        4. log out
        ===============
        ''')
    
    def inputAdmin(self):
        adminInput = input("masukan pilihan menu : ")
        try :
            Input = int(adminInput)
            if 0 < Input < 5:
                return adminInput
            else:
                raise ValueError("Tidak sesuai dengan Menu")
        except ValueError as err:
            raise MenuWrongException(err)
            
    def loginScreen(self):
        userId = input('Enter Id : ')
        userPassword = input ('Enter password : ')
        user = User(userId, userPassword)
        return user