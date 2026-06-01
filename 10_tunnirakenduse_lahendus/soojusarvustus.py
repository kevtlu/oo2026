class materialAmount:
    def __init__(self, mass, heat_capacity, temperature):
        self.mass = mass
        self.heat_capacity = heat_capacity
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def get_joules_per_kelvin(self):
        return self.mass * self.heat_capacity 

class airAmount(materialAmount):
    air_density = 1.23
    air_heat_capacity = 1012

    def __init__(self, length, width, height, temperature):
        mass = length * width * height * self.air_density
        super().__init__(mass, self.air_heat_capacity, temperature)

def get_equal_temperature(materials):
    joule_kelvin_sum = 0
    joule_sum = 0
    
    for material in materials:
        joule_kelvin_sum += material.get_joules_per_kelvin()
        joule_sum += material.get_joules_per_kelvin() * material.get_temperature()
    return joule_sum / joule_kelvin_sum

if __name__ == "__main__":
    water1 = materialAmount(0.2, 4200, 40)
    water2 = materialAmount(0.02, 4200, 95)
    water3 = materialAmount(3, 4200, 21)
    iron = materialAmount(10, 412, 55)
    air = airAmount(3, 2, 2.5, 20)
    
    print("Kaks veekogust (200 grammi 40-kraadise vee sisse valatakse 20 grammi 95-kraadist vett):", get_equal_temperature([water1, water2]), "°C")
    print("Vesi ja raud:", round(get_equal_temperature([water3, iron]), 2), "°C")
    print("Vesi ja õhk:", round(get_equal_temperature([water3, air]), 2), "°C")
    print("Vesi, raud ja õhk:", round(get_equal_temperature([water3, iron, air]), 2), "°C")