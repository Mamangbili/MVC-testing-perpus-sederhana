from MenuException import *
import time
import os  # For clearing the screen



class MenuUI:
    def __init__(self):
        self.input = None
        
    def clearScreen(self):
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def menuAwal(self): 
        print("""
        Selamat Datang di Perpus Nusantara
        ==================================
        1. login
        2. register
        3. exit
        """)
        
    def inputMenuAwal(self):
        Input = input("Silahkan masukan menu diatas : ")
        try :
            
            if 0 < int(Input) < 4:
                return Input
            else:
                raise ValueError("Tidak sesuai dengan Menu")
        except ValueError as err:
            raise MenuWrongException(err)
            
    def tampilkanListBuku(self,koleksiBuku):
        print("=================================")
        koleksiBuku = koleksiBuku.getKoleksi()
        for i,buku in enumerate(koleksiBuku,1):
            print(f"{i}. {buku.judul}")
    
    def tampilanUser(self):
        print('''
        1. lihat buku
        2. log out
        3. exit
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
        user = [userId,userPassword]
        return user
        
    def registerScreen(self):
        print("=====================")
        Id = input("Masukan Id: ")
        password1 = input("Masukan Password : ")
        password2 = input("Masukan Passowrd kembali : ")
        print("=====================")
        
        return {"Id": Id, "password1": password1, "password2":password2}