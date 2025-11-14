class Client:
    clients = []
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.active = False
        Client.clients.append(self)
    
    def __str__(self):
        return f"Nome: {self.name}, idade: {self.age}, gênero: {self.gender}, ativo: {self.active}"
    
    def list_clients():
        for client in Client.clients:
            print(f"Nome: {client.name}, idade: {client.age}, gênero: {client.gender}, ativo: {client.active}")

client1 = Client("João", "27", "Masculino")
client2 = Client("Maria", "32", "Feminino")
client3 = Client("Sofia", "25", "Mulher transgênero")

Client.list_clients()