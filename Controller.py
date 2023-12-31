from enum import Enum
from MenuException import MenuWrongException
from Register import Register
from Search import Search
from UIView import MenuUI
from Login import Login
from User import *
from KoleksiBuku import KoleksiBuku
from Buku import Buku
from typing import List
from MyException import MyException


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
    CARI = 10


class Controller:
    def __init__(self, view: MenuUI, koleksiBuku: KoleksiBuku, dummyDbData):
        self.koleksiBuku = koleksiBuku
        databaseUser = dummyDbData
        self.currentPage = Menu.MENU_AWAL
        self.exit = False
        currentUser = None
        while not self.exit:
            match self.currentPage:
                case Menu.MENU_AWAL:
                    self.loopPage(self.menuAwal, view)
                case Menu.LOGIN:
                    currentUser = self.loopPage(self.menuLogin, view, databaseUser)
                case Menu.HALAMAN_USER:
                    self.loopPage(self.menuUser, view, currentUser)
                case Menu.HALAMAN_ADMIN:
                    self.loopPage(self.menuAdmin, view, currentUser)
                case Menu.REGISTER:
                    currentUser = self.loopPage(self.menuRegister, view, databaseUser)
                case Menu.LIHAT_BUKU:
                    self.loopPage(
                        self.menuTampilkanBuku, view, currentUser, koleksiBuku
                    )
                case Menu.HAPUS_BUKU:
                    self.loopPage(self.menuHapusBuku, view, koleksiBuku, currentUser)
                case Menu.TAMBAH_BUKU:
                    self.loopPage(self.menuTambahBuku, view, koleksiBuku, currentUser)
                case Menu.EXIT:
                    exit()
                case Menu.CARI:
                    self.loopPage(self.menuCari, view, currentUser)

    def menuAdmin(self, view: MenuUI, admin):
        view.clearScreen()
        view.tampilanAdmin(admin)
        pilihanAdmin = view.inputAdmin()

        self.adminMenuChoice(pilihanAdmin)

    def adminMenuChoice(self, pilihan):
        match pilihan:
            case "1":
                self.currentPage = Menu.LIHAT_BUKU
            case "2":
                self.currentPage = Menu.TAMBAH_BUKU
            case "3":
                self.currentPage = Menu.HAPUS_BUKU
            case "4":
                self.currentPage = Menu.MENU_AWAL
            case "5":
                self.currentPage = Menu.CARI
            case _:
                raise MenuWrongException("Tidak ada di pilihan")

    def menuCari(self, view: MenuUI, user):
        view.clearScreen()
        keyword = view.inputCari()
        cari = Search(self.koleksiBuku)
        result = cari.search(keyword)
        view.menuCari(result)
        
        print()
        print("Tekan Enter untuk kembali ke menu")
        input()

        if isinstance(user, Authorize):
            self.currentPage = Menu.HALAMAN_ADMIN
        else:
            self.currentPage = Menu.HALAMAN_USER
        view.clearScreen()

    def menuAwal(self, view: MenuUI):
        view.clearScreen()
        view.menuAwal()
        pilihan = view.inputMenuAwal()
        match pilihan:
            case "1":
                self.currentPage = Menu.LOGIN
            case "2":
                self.currentPage = Menu.REGISTER
            case "3":
                self.currentPage = Menu.EXIT
            case _:
                raise MenuWrongException("Tidak ada di pilihan")

    def userLoginChoice(self, pilihan):
        match pilihan:
            case "1":
                self.currentPage = Menu.LIHAT_BUKU
            case "2":
                self.currentPage = Menu.MENU_AWAL
            case "3":
                self.currentPage = Menu.CARI
            case _:
                raise MenuWrongException("Tidak ada di pilihan")

    def menuUser(self, view: MenuUI, user):
        view.clearScreen()
        view.tampilanUser(user)
        pilihanMenuUser = view.inputUser()
        self.userLoginChoice(pilihanMenuUser)

    def menuLogin(self, view: MenuUI, dummyDbUser):
        view.clearScreen()
        IdLogin, PassLogin = view.loginScreen()
        postLoginData = User(IdLogin, PassLogin)
        loginUser = Login.login(postLoginData, dummyDbUser)

        if isinstance(loginUser, Authorize):
            self.currentPage = Menu.HALAMAN_ADMIN
        else:
            self.currentPage = Menu.HALAMAN_USER
        return loginUser

    def menuRegister(self, view, dummyDbUser):
        view.clearScreen()
        Id, password1, password2 = view.registerScreen().values()
        register = Register(dummyDbUser)
        newUser = register.create(Id, password1, password2)
        dummyDbUser.append(newUser)
        self.currentPage = Menu.HALAMAN_USER
        return newUser

    def menuTampilkanBuku(self, view, user: User, koleksiBuku: KoleksiBuku):
        view.clearScreen()
        view.tampilkanListBuku(koleksiBuku)
        print()
        print("Tekan Enter untuk kembali ke menu")
        input()
        if isinstance(user, Authorize):
            self.currentPage = Menu.HALAMAN_ADMIN
        else:
            self.currentPage = Menu.HALAMAN_USER
        view.clearScreen()

    def menuTambahBuku(self, view: MenuUI, koleksi: KoleksiBuku, admin):
        view.clearScreen()
        view.tampilkanListBuku(koleksi)
        print("==========================================")
        judul = input("Masukan Judul Buku Baru : ")
        koleksi.tambahBuku(admin, Buku(judul.rstrip()))
        self.currentPage = Menu.HALAMAN_ADMIN
        view.clearScreen()

    def menuHapusBuku(self, view: MenuUI, koleksi: KoleksiBuku, admin):
        view.clearScreen()
        view.tampilkanListBuku(koleksi)
        print("==========================================")
        judul = input("Masukan Judul Buku yang akan di hapus : ")
        koleksi.hapusBuku(admin, judul)

        self.currentPage = Menu.HALAMAN_ADMIN

    def loopPage(self, menuFn, *menuArgs):
        loop = True
        while loop:
            try:
                loop = False
                return menuFn(*menuArgs)
            except MyException as err:
                loop = True
                print(err.message)
