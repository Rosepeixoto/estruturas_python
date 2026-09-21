# Recebe o nome do usuário na variaável
name = input("qual seu nome? ")

# Recebe a idade do usuario na variável
age = input("qual sua idade? ")

# Exibe uma mesage formatada
print("ola", name, "!")
print("você tem", age, "anos")

# usando string formatada (f) - melhor prática
print()
print(f"olá {name}! Você tem {age} anos.")