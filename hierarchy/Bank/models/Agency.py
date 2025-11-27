from models.Bank import Bank

class Agency(Bank):
    def __init__(self, name, address, number):
        super().__init__(name, address)
        self.number = number
        
    def __str__(self):
        return f"Nome: {self.name} | Address: {self.address} | Number: {self.number}"