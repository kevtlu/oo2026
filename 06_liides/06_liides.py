from abc import ABC, abstractmethod

class Maksekanal(ABC):
    @abstractmethod
    def maksa(self, summa, saaja):
        pass

class Kaart(Maksekanal):
    def __init__(self, number):
        self.number = number
    
    def maksa(self, summa, saaja):
        print(f"Kaart lõpuga {self.number[-4:]} - {summa}€ -> {saaja}")

class PayPal(Maksekanal):
    def __init__(self, email):
        self.email = email
    
    def maksa(self, summa, saaja):
        print(f"PayPal - {summa}€ -> {saaja}")

class Rahakott:
    def __init__(self, omanik):
        self.omanik = omanik
        self.kanalid = {}
    
    def lisa(self, nimi, kanal):
        self.kanalid[nimi] = kanal
    
    def maksa(self, kanal, summa, saaja):
        if kanal in self.kanalid:
            print(f"{self.omanik} maksab:")
            self.kanalid[kanal].maksa(summa, saaja)
            print()

rahakott = Rahakott("Jaan")
rahakott.lisa("kaart", Kaart("1234567890123456"))
rahakott.lisa("paypal", PayPal("jaan@gmail.com"))

rahakott.maksa("kaart", 50, "Amazon")
rahakott.maksa("paypal", 25, "Spotify")