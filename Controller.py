from enum import Enum
from MenuException import MenuWrongException
from Register import Register
from UIView import MenuUI
from Login import Login
from User import *
from KoleksiBuku import KoleksiBuku
from Buku import Buku

class Menu(Enum):
    MENU_AWAL = 1
    LOGIN = 2
    HALAMAN_USER = 3
    HALAMAN_ADMIN = 4
    REGISTER = 5 
    LIHAT_BUKU = 6
    TAMBAH_BUKU = 7
    HAPUS_BUKU = 8
    EXIT = 9
    

class Controller:
    def __init__(self, view: MenuUI, koleksiBuku: KoleksiBuku,dummyDbData):
        self.koleksiBuku = koleksiBuku
        databaseUser = dummyDbData        
        self.currentPage = Menu.MENU_AWAL
        self.exit = False
        user = None
        while (not self.exit):
            match self.currentPage:
                case Menu.MENU_AWAL:
                    self.menuAwal(view)
                case Menu.LOGIN:
                    user = self.menuLogin(view,databaseUser)
                case Menu.HALAMAN_USER:
                    self.menuUser(view,user)
                case Menu.HALAMAN_ADMIN:
                    self.menuAdmin(view,user)
                case Menu.REGISTER:
                    user = self.menuRegister(view,databaseUser)
                case Menu.LIHAT_BUKU:
                    self.menuTampilkanBuku(view,user,koleksiBuku)
                case Menu.HAPUS_BUKU:
                    self.menuHapusBuku(view,koleksiBuku,user)
                case Menu.TAMBAH_BUKU:
                    self.menuTambahBuku(view,koleksiBuku,user)
                case Menu.EXIT:
                    exit()
                    
    def menuAdmin(self,view:MenuUI,admin):
        view.clearScreen()
        print(f"Nama User Anda    : {admin.Id}")
        view.tampilanAdmin()
        pilihanAdmin = view.inputAdmin()
        self.adminMenuChoice(pilihanAdmin)
        
    def adminMenuChoice(self, pilihan):
        match pilihan:
            case '1':
                self.currentPage = Menu.LIHAT_BUKU
            case '2':
                self.currentPage = Menu.TAMBAH_BUKU
            case '3':
                self.currentPage = Menu.HAPUS_BUKU
            case '4':
                self.currentPage = Menu.MENU_AWAL
            case _:
                raise MenuWrongException("Tidak ada di pilihan")
    
    def menuAwal(self,view: MenuUI):
        view.clearScreen()
        view.menuAwal()
        pilihan = view.inputMenuAwal()
        match pilihan:
            case '1':
                self.currentPage = Menu.LOGIN
            case '2': 
                self.currentPage = Menu.REGISTER
            case '3':
                self.currentPage = Menu.EXIT
            case _:
                raise MenuWrongException("Tidak ada di pilihan")
                
    def userLoginChoice(self, pilihan):
        match pilihan:
            case '1':
                self.currentPage = Menu.LIHAT_BUKU
            case '2':
                self.currentPage = Menu.MENU_AWAL
            case '3':
                self.exit = True
            case _:
                raise MenuWrongException("Tidak ada di pilihan")
                
    def menuUser(self,view: MenuUI,user):
        print(f"Nama User Anda    : {user.Id}")
        view.tampilanUser()
        pilihanMenuUser = view.inputUser()
        self.userLoginChoice(pilihanMenuUser)
        view.clearScreen()
        
    def menuLogin(self,view: MenuUI,dummyDbUser):
        IdLogin, PassLogin = view.loginScreen()
        postLoginData = User(IdLogin,PassLogin)
        loginUser = Login.login(postLoginData,dummyDbUser)
        
        if isinstance(loginUser, Admin):
            self.currentPage = Menu.HALAMAN_ADMIN
        else :
            self.currentPage = Menu.HALAMAN_USER
        view.clearScreen()
        return loginUser
        
    def menuRegister(self,view,dummyDbUser):
        Id,password1,password2 = view.registerScreen().values()
        register = Register(dummyDbUser)
        newUser = register.create(Id,password1,password2)
        dummyDbUser.append(newUser)
        self.currentPage = Menu.HALAMAN_USER
        view.clearScreen()
        return newUser
        
    def menuTampilkanBuku(self,view,user:User|None,koleksiBuku:KoleksiBuku):
        view.clearScreen()    
        view.tampilkanListBuku(koleksiBuku)
        input("Tekan Enter untuk kembali ke menu")
        if(isinstance(user,Admin)):
            self.currentPage = Menu.HALAMAN_ADMIN
        else:
            self.currentPage = Menu.HALAMAN_USER
        view.clearScreen()
        

    def menuTambahBuku(self, view:MenuUI, koleksi:KoleksiBuku, admin):
        view.clearScreen()
        view.tampilkanListBuku(koleksi)
        print("==========================================")
        judul = input("Masukan Judul Buku Baru : ")
        koleksi.tambahBuku(admin,Buku(judul))
        self.currentPage = Menu.HALAMAN_ADMIN
        view.clearScreen()
        
    
    def menuHapusBuku(self, view:MenuUI, koleksi:KoleksiBuku, admin):
        view.clearScreen()
        view.tampilkanListBuku(koleksi)
        print("==========================================")
        judul = input("Masukan Judul Buku yang akan di hapus : ")
        koleksi.hapusBuku(admin,judul)
        
        self.currentPage = Menu.HALAMAN_ADMIN
            