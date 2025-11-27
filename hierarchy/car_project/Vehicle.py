from abc import ABC, abstractmethod
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._active = False
    
    @abstractmethod
    def turn_on(self):
        pass
    
    def __str__(self):
        return f"Marca: {self.brand} | Modelo: {self.model} | Ativo: {self._active}"