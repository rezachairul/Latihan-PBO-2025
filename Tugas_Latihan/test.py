class Vehicle:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class GasCar(Vehicle):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.c = c
        self.d = d
  
    def __str__(self):
        return f"{self.a} {self.b} {self.c} {self.d}"

agya = GasCar("Toyoya", "Agya", 10, 20)
print(agya)