from abc import ABC, abstractmethod

class Ehitis(ABC):
    def __init__(self, nimi, pindala):
        self.nimi = nimi
        self.pindala = pindala
    
    @abstractmethod
    def kirjeldus(self):
        pass

class Elamupind(Ehitis):
    def __init__(self, nimi, pindala, korruseid):
        super().__init__(nimi, pindala)
        self.korruseid = korruseid
    
    @abstractmethod
    def iseloom(self):
        pass

class Kortermaja(Elamupind):
    def __init__(self, nimi, pindala, korruseid, korterid):
        super().__init__(nimi, pindala, korruseid)
        self.korterid = korterid
    
    def kirjeldus(self):
        print(f"{self.nimi}: {self.korterid} korterit, {self.korruseid} korrust, {self.pindala}m²")
    
    def iseloom(self):
        return "kortermaja"

class Eramaja(Elamupind):
    def __init__(self, nimi, pindala, korruseid):
        super().__init__(nimi, pindala, korruseid)
    
    def kirjeldus(self):
        print(f"{self.nimi}: eramaja, {self.korruseid} korrust, {self.pindala}m²")
    
    def iseloom(self):
        return "eramaja"

class Arihoone(Ehitis):
    def __init__(self, nimi, pindala, tyyp):
        super().__init__(nimi, pindala)
        self.tyyp = tyyp
    
    def kirjeldus(self):
        print(f"{self.nimi}: {self.tyyp}, {self.pindala}m²")

def main():
    hooned = [
        Kortermaja("Kortermaja", 5000, 9, 120),
        Eramaja("Maja Nõmmel", 200, 2),
        Arihoone("Kaubanduskeskus", 15000, "kaubandus"),
        Arihoone("Kontoribüroo", 3000, "kontorid")
    ]
    
    print("Ehitised:")
    for hoone in hooned:
        hoone.kirjeldus()

main()