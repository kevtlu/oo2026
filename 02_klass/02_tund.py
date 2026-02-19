class isikukood:
    def __init__(self, isikukood):
        if len(isikukood) != 11:
            raise Exception("Vigane pikkus!")

        self.kood = isikukood

    def kuupaev(self):
        return self.kood[5:7]
    
    def kuu(self):
        kuu = self.kood[3:5]
        if kuu == "01":
            kuu = "jaanuar"
        elif kuu == "02":
            kuu = "veebruar"
        elif kuu == "03":
            kuu = "märts"
        elif kuu == "04":
            kuu = "aprill"
        elif kuu == "05":
            kuu = "mai"
        elif kuu == "06":
            kuu = "juuni"
        elif kuu == "07":
            kuu = "juuli"
        elif kuu == "08":
            kuu = "august"
        elif kuu == "09":
            kuu = "september"
        elif kuu == "10":
            kuu = "oktoober"
        elif kuu == "11":
            kuu = "november"
        elif kuu == "12":
            kuu = "detsember"
        return kuu
    
    def aasta(self):
        aasta2 = self.kood[1:3]
        aasta1 = self.kood[0:1]

        if aasta1 in ["1", "2"]:
            synniaasta = "18"
        elif aasta1 in ["3", "4"]:
            synniaasta = "19"
        elif aasta1 in ["5", "6"]:
            synniaasta = "20"

        return synniaasta + aasta2
    
    def kontroll(self):
        summa = 0
        korrutis = 1
        for i in range(len(isikukood)):
            summa = korrutis * isikukood[i]
            korrutis += 1
            isikukood[i + 1]

        jaak = summa // 11

        return

ik1 = isikukood("50508270861")
isikukoodid = [ik1]
print([ik.kuupaev() + ". " + ik.kuu() + " " + str(ik.aasta()) for ik in isikukoodid])