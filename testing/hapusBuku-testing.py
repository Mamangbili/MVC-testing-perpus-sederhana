import __init__
import copy
from KoleksiBuku import KoleksiBuku
from Buku import Buku
import unittest
from User import Admin,User
from MenuBukuException import *
koleksiTanpa1984 = [
    Buku("To Kill a Mockingbird"),
    
    Buku("The Great Gatsby"),
    Buku("Pride and Prejudice"),
    Buku("The Catcher in the Rye"),
    Buku("Harry Potter and the Sorcerer's Stone"),
    Buku("The Lord of the Rings"),
    Buku("The Hobbit"),
    Buku("Brave New World"),
    Buku("The Hunger Games"),
]

koleksiBaru = [*koleksiTanpa1984,Buku("1984")]

class HapusBuku(unittest.TestCase):
    
    def test_hapusBiasa(self):
        koleksi = KoleksiBuku(koleksiBaru)
        koleksiBaruTest = KoleksiBuku(koleksiTanpa1984)
        admin = Admin("Admin", 'Admin123')
        
        koleksi.hapusBuku(admin,'1984')
        
        self.assertEqual(koleksi, koleksiBaruTest)
        
    def test_hapusYangTidakAdaDiList(self):
        koleksi = KoleksiBuku(koleksiBaru)
        koleksiBaruTest = KoleksiBuku(koleksiTanpa1984)
        admin = Admin("Admin", 'Admin123')
        
        with self.assertRaises(BukuHapusException):
            koleksi.hapusBuku(admin,'buku tidak ada di list')
            
    def test_hapusSelainAdmin(self):
        koleksi = KoleksiBuku(koleksiBaru)
        koleksiBaruTest = KoleksiBuku(koleksiTanpa1984)
        user = User("Admin", 'Admin123')
        
        
        with self.assertRaises(BukuHapusException):
            koleksi.hapusBuku(user,'1984')
        

        
if __name__ == "__main__":
    unittest.main()