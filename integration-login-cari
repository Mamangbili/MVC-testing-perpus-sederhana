import unittest
from constant import * 
from Login import Login
from LoginException import *
from Search import Search
from Buku import Buku
from KoleksiBuku import KoleksiBuku
from User import Admin

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

class IntegrationLoginCariTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.username = 'mamat'
        self.password = 'mamat123'
        self.auth = User(self.username, self.password)

    def test_intTestLogin(self):
        self.assertEqual(self.auth, dummyUser[0])
        Login.validatePassword(self.auth, dummyUser[0])

    def test_intCariBuku(self):
        keyword = "Hobbit"
        result = []
        for i in Search(KoleksiBuku(bookTitlesData)).search(keyword):
            result.append(i.judul)
        self.assertTrue("The Hobbit" in result)

if __name__ == "__main__":
    unittest.main()
