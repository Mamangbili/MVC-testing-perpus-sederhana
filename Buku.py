from __future__ import annotations
class Buku: 
    def __init__(self,judul):
        self.judul = judul
    
    def __eq__(self, bukuLain: Buku):
        return self.judul == bukuLain.judul