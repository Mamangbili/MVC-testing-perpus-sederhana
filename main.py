from Controller import Controller
from UIView import MenuUI
from KoleksiBuku import KoleksiBuku
from Buku import Buku
from User import User, Admin

bookTitlesData = [
    Buku("To Kill a Mockingbird"),
    Buku("1984"),
    Buku("The Great Gatsby"),
    Buku("Pride and Prejudice"),
    Buku("The Catcher in the Rye"),
    Buku("Harry Potter and the Sorcerer's Stone"),
    Buku("The Lord of the Rings"),
    Buku("The Hobbit"),
    Buku("Brave New World"),
    Buku("The Hunger Games")
]

dummyUser = [
            User("asep", "Asep1234"),
            User("rudi","Rudi1234"),
            Admin("mamat","Mamat1234"),
            User("cepi","Cepi1234")
        ]

if __name__ == '__main__':
    koleksiBuku = KoleksiBuku(bookTitlesData)
    view = MenuUI()
    controller = Controller(view,koleksiBuku, dummyUser)