# Latihan 2: Mobil Listrik VS Mobil Bensin

#Kelas Utama
class Vehilce:
    def __init__(self, manufactur, model):
        self.manufactur = manufactur
        self.model = model
    
    def display_specs(self):
        print ("Manufactur", self.manufactur)
        print ("Model", self.model)

    def calculate_range(self):
        pass

#Sub Kelas Mobil Bensin
class GasCar(Vehilce):
    def _init_(self, manufactur, model, fuel_capacity, fuel_level, fuel_efficiency):
        super().__init__(manufactur, model)
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.fuel_efficiency = fuel_efficiency
    
    def refuel (self, amount=None):
        if amount is None:
            self.fuel_level = self.fuel_capacity
        else:
            self.fuel_level = min(self.fuel_capacity, self.fuel_level + amount)
    
    def calculate_range(self):
        return self.fuel_level * self.fuel_efficiency


#Sub Kelas Mobil Listrik
class Electric(Vehilce):
    def _init_(self, manufactur, model, battery_capacity, battery_level, energy_efficiency):
        super().__init__(manufactur, model)
        self.battery_capacity = battery_capacity
        self.battery_level = battery_level
        self.energy_efficiency = energy_efficiency
    
    def charge (self, amount=None):
        if amount is None:
            self.battery_level = self.battery_capacity
        else:
            self.battery_level = min(self.battery_capacity, self.battery_level + amount)
    
    def calculate_range(self):
        return self.battery_level * self.energy_efficiency
    
def print_range(vehicle):
    print (vehicle.manufactur, vehicle.model, "dapat menempuh jarak", vehicle.calculate_range(), "Km")

# Main program
gas_car = GasCar("Daihatsu", "Rocky", 50, 20, 10)
electric_car = Electric("Tesla", "Model S", 100, 80, 20)


# jarak tempuh mobil bensin
print_range(gas_car)
# jarak tempuh mobil listrik
print_range(electric_car)