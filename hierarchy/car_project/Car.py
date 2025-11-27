from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color
    
    def turn_on(self):
        self._active = True
        
    def __str__(self):
        return super().__str__() + f" | Cor: {self.color}"