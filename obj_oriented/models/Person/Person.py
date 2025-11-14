class Person:
    def __init__(self, name, age, job):
        self.name = name.title()
        self.age = age
        self.job = job.title()
    
    def __str__(self):
        return f"Nome: {self.name} | Idade: {self.age} | Profissão: {self.job}"
    
    def anniversary(self):
        self.age += 1
    
    @property
    def salute(self):
        return f"Saudações caro(a) {self.job}"
    
person1 = Person("kleber", 22, "DJ")
person1.anniversary()

person2 = Person("sara", 24, "Acadêmica")
person2.anniversary()

print(person1)
print(person2)

print(person1.salute)
print(person2.salute)