from __future__ import annotations
from MenuBukuException import *
from Buku import Buku
from User import Authorize

class KoleksiBuku:
    def __init__(self,koleksiDummy) -> None:
        self.__koleksiBuku = [*koleksiDummy]
        
    def getKoleksi(self):
        return self.__koleksiBuku
        
    def tambahBuku(self,admin:Authorize,buku):
        from User import Authorize
        if not isinstance(buku, Buku):
            raise BukuTambahException("Bukan instance Buku")
        
        if isinstance(admin,Authorize):
            self.__koleksiBuku.append(buku)
        else : 
            raise BukuTambahException("Bukan User Authorize")
    
    def hapusBuku(self,admin,judul):
        from User import Authorize
        if isinstance(admin, Authorize):
            judulStringList = list(map(lambda buku : buku.judul, self.__koleksiBuku)) 
            if judul in judulStringList:
                self.__koleksiBuku.remove(Buku(judul))
            else :  
                raise BukuHapusException("Tidak ada judul buku yang akan dihapus")
        else:
            raise BukuHapusException("Bukan Admin")
    def __eq__(self,koleksiLain: KoleksiBuku):
        return self.__koleksiBuku == koleksiLain.getKoleksi()
                    
                