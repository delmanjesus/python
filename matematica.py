import random

def diferenca():
    x = random.randint(1,10)
    y = random.randint(1,10) * -1
    z =  random.randint(1,10)
    print(f"quanto é +{x}{y}+{z}?")
    res = x + y + z
    resposta = int(input("R:"))
    if resposta == res:
        print('correto')
    else:
        print('errado')

choice = True

while choice == True:
    diferenca()