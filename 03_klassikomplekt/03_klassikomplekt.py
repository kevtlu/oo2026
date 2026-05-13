import random

class Toode:
    def __init__(self, nimi, hind, kogus):
        self.nimi = nimi
        self.hind = hind
        self.kogus = kogus
    
    def __str__(self):
        return f"{self.nimi} ({self.hind}€, laos: {self.kogus}tk)"

class Klient:
    def __init__(self, nimi, budget):
        self.nimi = nimi
        self.budget = budget
        self.algne_budget = budget
        self.ostetud = []
    
    def ostad_toodet(self, toode):
        if self.budget >= toode.hind and toode.kogus > 0:
            self.budget -= toode.hind
            toode.kogus -= 1
            self.ostetud.append(toode.nimi)
            print(f"{self.nimi} ostis {toode.nimi} ({toode.hind}€)")
            return True
        elif toode.kogus == 0:
            print(f"{self.nimi} ei saanud osta {toode.nimi} (otsas)")
        else:
            print(f"{self.nimi} ei saanud osta {toode.nimi} (raha pole piisavalt)")
        return False
    
    def __str__(self):
        kulutus = self.algne_budget - self.budget
        return f"{self.nimi}: kulutas {round(kulutus, 2)}€, jäänud {round(self.budget, 2)}€"

class Pood:
    def __init__(self, nimi):
        self.nimi = nimi
        self.tooted = []
        self.kliendid = []
    
    def lisa_toode(self, toode):
        self.tooted.append(toode)
    
    def lisa_klient(self, klient):
        self.kliendid.append(klient)
    
    def simuleeri_ostlemist(self, voorud=5):
        
        for voor in range(voorud):
            print(f"Voor {voor + 1}:")
            klient = random.choice(self.kliendid)
            toode = random.choice(self.tooted)
            klient.ostad_toodet(toode)
            print()
        
        print("Lõpptulemused:")
        for klient in self.kliendid:
            print(klient)
        
        print("\nKaubad:")
        for toode in self.tooted:
            print(toode)

pood = Pood("Kõik Kaupade Kauplus")

pood.lisa_toode(Toode("Leib", 2.5, 8))
pood.lisa_toode(Toode("Piim", 1.8, 10))
pood.lisa_toode(Toode("Juust", 4.2, 5))
pood.lisa_toode(Toode("Munad", 3.0, 6))

pood.lisa_klient(Klient("Anna", 20))
pood.lisa_klient(Klient("Jaan", 15))
pood.lisa_klient(Klient("Liis", 25))

pood.simuleeri_ostlemist(8)