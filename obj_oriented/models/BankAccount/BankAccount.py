class BankAccount:
    def __init__(self, owner, value):
        self.owner = owner
        self.value = value
        self.isActive = False

    def __str__(self):
        return f"Titular: {self.owner} | Saldo: {self.value} | Ativo: {self.isActive}"
    
    def activeAccount(self):
        self.isActive = True
        
    @property
    def accountValue(self):
        return f"Saldo da conta: {self.value}R$"

conta1 = BankAccount("Sofia", 13.000)
conta2 = BankAccount("Helena", 45.000)

conta1.activeAccount()

print(conta1)
print(conta2)

print(conta1.accountValue)
print(conta2.accountValue)

print(conta1.owner)
print(conta2.owner)