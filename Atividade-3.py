import os
os.system('cls')

vetor_quantidade = []
vetor_numeros = []
QUANTIDADE = 10
soma = 0

print('\nSolicitando Dados')

for i in range(QUANTIDADE):
    numero = int(input('\nDigite um numero: '))

    soma = soma + numero
    if numero > 10:
        vetor_quantidade.append(numero)
        print('Esse número é maior que 10')
    else:
        continue

print(f'Mostrando os numeros maiores que 10: {len(vetor_quantidade)}')
print(f'\nSoma dos números: {soma}')
