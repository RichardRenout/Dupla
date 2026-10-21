import os
os.system('cls')

lista_A = []
lista_B_positivos = []
numero_copiado = []

for i in range(10):
    numero = int(input(f'Digite o {i+1} número: '))
    lista_A.append(numero)

    if numero > 0 and numero in lista_A:
        numero_copiado.append(numero)
        lista_B_positivos.append(numero)

print(f'Número de positivos: {lista_B_positivos}')
print(f'Foram copiados {len(numero_copiado)} números')
