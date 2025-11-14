class Restaurant:
    def __init__(self, name, category, active, address, rent):
        self.name = name
        self.category = category
        self.active = False
        self.address = address
        self.rent = rent
    
    def __str__(self):
        return f"Nome: {self.name} | Categoria: {self.category} | Ativo: {self.active} | Endereço: {self.address} | Aluguel: {self.rent}"
    
restaurant = Restaurant("Pizza's loko", "Pizzaria", None, "Rua do bobos, 0", "12.000")

print(restaurant)