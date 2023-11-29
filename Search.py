from fuzzywuzzy import fuzz 
class Search:
    def __init__(self,koleksiBuku):
        self.koleksiBuku = koleksiBuku
    
    def search(self,keyword):
        choosenRatio = 70
        result = []
        for book in self.koleksiBuku.getKoleksi():
            ratio = fuzz.ratio(keyword,book.judul) 
            if ratio > choosenRatio:
                result.append(book)
        return result