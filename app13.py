# Itrando dicionário
import os
os.system('cls')

prods = {
    "cod": "123abc",
    "name": "caixa de sapato vazi",
    "fabr": "caixeiro Vijante",
    "preço": 120.99
}

print(prods)
print()

for prod in prods:
    print(prods[prod])
    print(f' • {prod} - {prods[prod]}')

    print()
print('------', prods.keys())
for prod in prods.keys():
    print(prod)

print()
print('------', prods.values())
for prod in prods.values():
    print(prod)

print()

for prod_key, prod_value in prods.items():
    print(f' • {prod_key.capitalize()} - {prod_value}')