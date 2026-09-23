# Recebe a variável name
name = input("qual seu nome? ")
age = input("qual sua idade ")

age = int(age)

#criar uma função
def biscoito ():
    x = "esta com fome!"
    print ("Rose", x)

biscoito ()

print(type(name))
print(type(age))

age = int(age)

older = age + 10

print(f" {name} terá {older} daqui a 10 anos")