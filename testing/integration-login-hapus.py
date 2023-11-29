from constant import User,Admin, dummyUser
import unittest
from KoleksiBuku import KoleksiBuku
from Buku import Buku
from User import User, Admin
from Login import Login
from MenuException import MenuWrongException
from MenuBukuException import BukuHapusException

class TestLoginDeleteBook(unittest.TestCase):
    def setUp(self):
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

        self.koleksi_buku = KoleksiBuku(bookTitlesData)

    def test_adminDeleteBook(self):
        # Simulate admin login
        admin_user = Admin("mamat", "Mamat1234")

        # Mengambil data buku yang akan dihapus
        book_to_delete = self.koleksi_buku.getKoleksi()[0]

        # Memastikan apakah buku tersebut ada pada koleksi buku
        self.assertIn(book_to_delete, self.koleksi_buku.getKoleksi())

        # User adalah Admin dan mencoba menghapus buku
        try:
            Login.validatePassword(admin_user, admin_user)  
            self.koleksi_buku.hapusBuku(admin_user, book_to_delete.judul)
            
        except BukuHapusException as err:
            self.fail(f"Failed to delete book: {err}")

        # Cek apakah buku yang sudah di hapus ada pada koleksi buku 
        self.assertNotIn(book_to_delete, self.koleksi_buku.getKoleksi())
        print("Buku berhasil dihapus")

    def test_nonAdminDeleteBook(self):
        # Simulate non-admin user login
        non_admin_user = User("asep", "Asep1234")

        # Mengambil data buku yang akan dihapus
        book_to_delete = self.koleksi_buku.getKoleksi()[0]

        # Memastikan apakah buku tersebut ada pada koleksi buku
        self.assertIn(book_to_delete, self.koleksi_buku.getKoleksi())

        # User bukanlah Admin dan mencoba menghapus buku
        try:
            Login.validatePassword(non_admin_user, non_admin_user) 
            with self.assertRaises(BukuHapusException):
                self.koleksi_buku.hapusBuku(non_admin_user, book_to_delete.judul)
        except MenuWrongException as err:
            self.fail(f"Unexpected exception: {err}")

        # Cek apakah buku masih ada pada koleksi buku 
        self.assertIn(book_to_delete, self.koleksi_buku.getKoleksi())

if __name__ == '__main__':
    unittest.main()
