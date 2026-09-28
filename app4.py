import os

# Define o valor da variável
has_invitation = is_vip = False
invited = age = vip = str()

# Limpa a tela do terminal CMD
os.system("cls")

# Recebe dados d usuário
age = int(input('Digite a idade: '))
vip = input('É vip [sim/não]? ')

# Testa a entrada do usuário
if vip.lower() == 'sim':
    is_vip = True
else:
    invited = input('Tem convite [sim/não]? ')

# Testa a entrada do usuário
if invited.lower() == 'sim':
    # Neste caso, altera o valor da variável
    has_invitation = True

# Depuração de variáveis
print(type(age), age)
print(type(has_invitation), has_invitation)
print(type(is_vip), is_vip)

'''''
if is_vip:
    print("que bom ver você novamente")
    
elif age >= 18 and has_invitation: 

    print("Entrada permitida") 

else: 
    print("Entrada não permitida") 

'''

print('acabou')