import os
os.system("cls")



vetor_numeros = []

for i in range(8):
    numero = int(input(f"Digite o seu {i+1} numero: "))
    vetor_numeros.append(numero)


n1 = int(input("\n Digite o numero para pesquisa: "))

encontrado = False

for posicao, valor in enumerate(vetor_numeros):
    if valor == n1:
        print(f"Numero Encontrado na posição: {posicao} ")
        encontrado = True
        break
    else:
        print("Numero Não Encontrado")
