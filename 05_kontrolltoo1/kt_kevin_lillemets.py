import math

def ruutjuur(a, b):
    ruutjuur.a = a
    ruutjuur.b = b
    return math.sqrt(a * b)

tulemus = ruutjuur(7, 5)
print("1. Ülesanne: Arvude", ruutjuur.a, "ja", ruutjuur.b, "korrutise ruutjuur on", round(tulemus, 2))

def juur(arvud):
    korrutis = 1

    for kordaja in arvud:
        korrutis = korrutis * kordaja

    return round(korrutis ** (1 / len(arvud)), 2)

list1 = [2, 5, 7, 4, 9, 11, 15]
tulemus2 = juur(list1)

print("2. Ülesanne:", tulemus2)

class Palk:
    def __init__(self, algpalk):
        self.algpalk = algpalk
        self.koefitsendid = []

    def lisa_koefitsent(self, koef):
        self.koefitsendid.append(koef)

    def palgad_igal_aastal(self):
        palgad = [self.algpalk]
        hetkepalk = self.algpalk

        for koef in self.koefitsendid:
            hetkepalk = round(hetkepalk * koef, 2)
            palgad.append(hetkepalk)

        return palgad
    
    def palgad_keskmine(self):
        palgad = [self.algpalk]
        hetkepalk = self.algpalk
        korrutis = 1

        for koef in self.koefitsendid:
            korrutis = korrutis * koef
            
        keskmine_koef = korrutis ** (1 / len(self.koefitsendid))
        
        for i in range(len(self.koefitsendid)):
            hetkepalk = round(hetkepalk * keskmine_koef)
            palgad.append(hetkepalk)
            
        return palgad
 
palk = Palk(1300)

palk.lisa_koefitsent(1.1)
palk.lisa_koefitsent(0.9)
palk.lisa_koefitsent(1.15)

print("3. Ülesanne: Tegelikud palgad:", palk.palgad_igal_aastal())
print("3. Ülesanne: Keskmised palgad:", palk.palgad_keskmine())