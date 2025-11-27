from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type
    
    def turn_on(self):
        self._active = True
        
    def __str__(self):
        return super().__str__() + f" | Tipo: {self.type}"