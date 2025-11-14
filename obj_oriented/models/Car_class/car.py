class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
    
    def __str__(self):
        return f"Modelo: {self.model} | cor: {self.color} | year:{self.year}"

Car1 = Car("Golf", "Vermelho", "1992")

print(Car1)