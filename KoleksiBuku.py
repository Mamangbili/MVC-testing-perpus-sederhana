class KoleksiBuku:
    def __init__(self) -> None:
        self.__koleksiBuku = []
        
    def tampilkanBuku(self, userVisitor):
        userVisitor.lihat(self)
        
    def getKoleksi(self):
        return self.__koleksiBuku
        
    def tambahBuku(self,admin,judul):
        from User import Authorize
        if isinstance(admin,Authorize):
            self.__koleksiBuku.append(judul)
        else : 
            raise BukuTambahException("Bukan User Authorize")
    
    def hapusBuku(self,admin,judul):
        from User import Authorize
        if isinstance(admin, Authorize):
            found = None
            for buku in self.__koleksiBuku:
                if buku.judul == judul:
                    found = buku
                    break
            
            if found is not None:
                self.__koleksiBuku.remove(found)
            else :  
                raise BukuHapusException("Tidak ada judul buku yang akan dihapus")
                