class Client:
    def __init__(self, owner, age, job, value):
        self.owner = owner.title()
        self.age = age
        self.job = job
        self.value = value
        self.isActive = False
        
    def changeClientStatus(self):
        self.isActive = not self.isActive
    
    def __str__(self):
        return f"Titular: {self.owner} | Idade: {self.age} | Profissão: {self.job} | Saldo: {self.value} | Client ativo: {self.isActive}"
        
client1 = Client("gabriel", 37, "programador", 110.000)
client1.changeClientStatus()
client2 = Client("daniel", 29, "gerente", 220.000)

print(client1)
print(client2)