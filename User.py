from abc import ABC, abstractmethod

class Authorize(ABC):pass
    
class User:
    def __init__(self,id,password):
        self.Id=id
        self.password=password
        self.loginStatus = False
    
    def lihat(self,koleksi):
        koleksiBuku = koleksi.getKoleksi()
        for i,buku in enumerate(buku,1):
            print(i+'.', buku)
            
                   
class Admin(User, Authorize):
    def __init__(self,Id,Password):
        super().__init__(Id,Password)
        

        