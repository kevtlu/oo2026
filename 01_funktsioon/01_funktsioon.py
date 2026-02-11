def reisikalkulaator(vahemaa, kytusekulu, liitri_hind):
    kulutatud_kytus = (vahemaa / 100) * kytusekulu
    kytuse_hind = kulutatud_kytus * liitri_hind

    return round(kytuse_hind, 2)

distants = int(input("Sisesta reisi distants: "))
kytusekulu_sajale = 9
bensiini_hind = 1.4

reisi_hind = reisikalkulaator(distants, kytusekulu_sajale, bensiini_hind)

print("Sõit pikkusega", distants, "km maksab kütuse osas", reisi_hind, "€.")