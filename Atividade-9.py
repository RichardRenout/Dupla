import os
os.system('cls' if os.name == 'nt' else 'clear')

vetor_original = []
vetor_transformado = []
QUANTIDADE = 6

for i in range(QUANTIDADE):
    numero = int(input(f'Digite o {i+1}º número inteiro: '))
    vetor_original.append(numero)

for numero in vetor_original:
    if numero % 2 == 0:
        vetor_transformado.append(0)
    else:
        vetor_transformado.append(1)

print(f'\nVetor antes: {vetor_original}')
print(f'Vetor depois: {vetor_transformado}')
