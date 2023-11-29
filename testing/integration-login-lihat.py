from constant import User,Admin
from KoleksiBuku import KoleksiBuku
from Buku import Buku
from UIView import MenuUI
from Controller import Controller, Menu
import unittest
from Login import Login

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
    Admin("mamat","mamat123"),
]

class LoginLihatIntTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.username = 'mamat'
        self.password = 'mamat123'
        self.auth = User(self.username, self.password)
        
    def test_intTestLogin(self):
        self.assertEqual(self.auth, dummyUser[0])
        Login.validatePassword(self.auth, dummyUser[0])

    def test_intTestLihatAdmin(self):
        self.assertEqual(KoleksiBuku(bookTitlesData).getKoleksi(), bookTitlesData)
if __name__ == "__main__":
    unittest.main()