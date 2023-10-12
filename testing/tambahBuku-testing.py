import __init__

from Buku  import Buku
from KoleksiBuku import KoleksiBuku
import unittest
import copy
from User import Admin
from MenuBukuException import BukuTambahException, BukuHapusException

bukuBaru = Buku('Buku Baru')
koleksiLama = [
    Buku("To Kill a Mockingbird"),
    Buku("1984"),
    Buku("The Great Gatsby"),
    Buku("Pride and Prejudice"),
    Buku("The Catcher in the Rye"),
    Buku("Harry Potter and the Sorcerer's Stone"),
    Buku("The Lord of the Rings"),
    Buku("The Hobbit"),
    Buku("Brave New World"),
    Buku("The Hunger Games"),
]


koleksiBaru = [
    *koleksiLama,
    bukuBaru
]


class TambahBuku(unittest.TestCase):
    def test_tambahBukuBiasa(self):
        koleksiLamaTest = KoleksiBuku(koleksiLama)
        koleksiBaruTest = KoleksiBuku(koleksiBaru)
        admin = Admin("Admin1234","Admin1234")

        #ditambah baru
        koleksiLamaTest.tambahBuku(admin,bukuBaru)
        self.assertEqual(koleksiLamaTest, koleksiBaruTest)
    
    def test_tambahSelainBuku(self):
        koleksi = KoleksiBuku(koleksiLama)
        admin = Admin("Admin1234","Admin1234")

        with self.assertRaises(BukuTambahException):
            koleksi.tambahBuku(admin,Admin('jamal','ludin'))

if __name__ == "__main__":
    unittest.main()
        