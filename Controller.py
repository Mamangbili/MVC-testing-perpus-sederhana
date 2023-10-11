from enum import Enum
from MenuException import MenuWrongException
from Register import Register
from UIView import MenuUI
from Login import Login
from User import *
from KoleksiBuku import KoleksiBuku
from typing import Optional, Union

class Menu(Enum):
    MENU_AWAL = 1
    LOGIN = 2
    HALAMAN_USER = 3
    HALAMAN_ADMIN = 4
    REGISTER = 5 
    LIHAT_BUKU = 6
    TAMBAH_BUKU = 7
    HAPUS_BUKU = 8
    

class Controller:
    def __init__(self, view: MenuUI, koleksiBuku: KoleksiBuku):
        self.koleksiBuku = koleksiBuku
        dummyDbUser = [
            User("asep", "asep123"),
            User("rudi","rudi123"),
            Admin("mamat","mamat123"),
            User("cepi","cepi123")
        ]        
                
        while self.currentPage:
            try :
                view.menuAwal()
                pilihanMenuUser = view.inputMenuAwal()
                # self.currentPage = self.menuAwal(pilihanMenuUser)
            except MenuWrongException as err:
                self.currentPage = Menu.MENU_AWAL
        
        
        self.currentPage = Menu.MENU_AWAL
        user = None
        while True:
            match self.currentPage:
                case Menu.MENU_AWAL:
                    self.menuAwal(view)
                case Menu.LOGIN:
                    user = self.menuLogin(view,dummyDbUser)
                case Menu.HALAMAN_USER:
                    self.menuUser(view)
                case Menu.HALAMAN_ADMIN:
                    self.menuAdmin(view)
                case Menu.REGISTER:
                    user = self.menuRegister(view,dummyDbUser)
                case Menu.LIHAT_BUKU:
                    self.menuTampilkanBuku(view,user)
                case Menu.HAPUS_BUKU:
                    self.menuHapusBuku(view,koleksiBuku,user)
                case Menu.TAMBAH_BUKU:
                    self.menuTambahBuku(view,koleksiBuku,user)
                    
    def menuAdmin(self,view:MenuUI):
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
                self.currentPage = Menu.HALAMAN_ADMIN
            case _:
                raise MenuWrongException("Tidak ada di pilihan")
    
    def menuAwal(self,view: MenuUI):
        view.menuAwal()
        pilihan = view.inputMenuAwal()
        match pilihan:
            case '1':
                self.currentPage = Menu.LOGIN
            case '2': 
                self.currentPage = Menu.REGISTER
            case _:
                raise MenuWrongException("Tidak ada di pilihan")
                
    def userLoginChoice(self, pilihan):
        match pilihan:
            case '1':
                self.currentPage = Menu.LIHAT_BUKU
            case '2':
                self.currentPage = Menu.MENU_AWAL
            case _:
                raise MenuWrongException("Tidak ada di pilihan")
                
    def menuUser(self,view: MenuUI):
        view.tampilanUser()
        pilihanMenuUser = view.inputUser()
        self.userLoginChoice(pilihanMenuUser)
        view.clearScreen()
        
    def menuLogin(self,view: MenuUI,dummyDbUser):
        guest = view.loginScreen()
        loginUser = Login.login(guest,dummyDbUser)
        
        if isinstance(loginUser, Admin):
            self.currentPage = Menu.HALAMAN_ADMIN
        else :
            self.currentPage = Menu.HALAMAN_USER
        view.clearScreen()
        return loginUser
        
    def menuRegister(self,view,dummyDbUser):
        Id,password1,password2 = view.registerScreen(view).values()
        register = Register(dummyDbUser)
        newUser = register.create(Id,password1,password2)
        dummyDbUser.append(newUser)
        self.currentPage = Menu.HALAMAN_USER
        view.clearScreen()
        return newUser
        
    def menuTampilkanBuku(self,view,user:User|None):
        view.tampilkanListBuku()
        input("Tekan Enter untuk kembali ke menu")
        if(isinstance(user,Admin)):
            self.currentPage = Menu.HALAMAN_ADMIN
        else:
            self.currentPage = Menu.HALAMAN_USER
        view.clearScreen()    

    def menuTambahBuku(self, view:MenuUI, koleksi:KoleksiBuku, admin):
        view.tampilkanListBuku(koleksi)
        print("==========================================")
        judul = input("Masukan Judul Buku Baru : ")
        koleksi.tambahBuku(admin,judul)
        self.currentPage = Menu.HALAMAN_ADMIN
        view.clearScreen()
    
    def menuHapusBuku(self, view:MenuUI, koleksi:KoleksiBuku, admin):
        view.tampilkanListBuku(koleksi)
        print("==========================================")
        judul = input("Masukan Judul Buku yang akan di hapus : ")
        koleksi.hapusBuku(admin,judul)
        
        self.currentPage = Menu.HALAMAN_ADMIN
        view.clearScreen()
            
        