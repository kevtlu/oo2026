class pangakonto:
    def __init__(self, omaniku_nimi, algsaldo):
        self.omanik = omaniku_nimi
        self.saldo = algsaldo

    def lisa_raha(self, summa):
        self.saldo += summa
        print(f"({self.omanik}): Kontole lisati {summa}€. Uus jääk: {self.saldo}€")

    def vota_raha(self, summa):
        if summa <= self.saldo:
            self.saldo -= summa
            print(f"({self.omanik}): Kontolt võeti välja {summa}€. Uus jääk: {self.saldo}€")
        else:
            print(f"({self.omanik}): Viga! Soovisid kontolt välja võtta {summa}€, aga arvel on vaid {self.saldo}€")

konto_malle = pangakonto("Malle", 1000)
konto_kalle = pangakonto("Kalle", 2000)

konto_malle.lisa_raha(500)
konto_kalle.vota_raha(2200)