import os
os.system('cls')

vetor_nota = []
QUANTIDADE = 5
soma = 0

for i in range(QUANTIDADE):
    nota = int(input(f'Digite sua {i+1} nota: '))
    vetor_nota.append(nota)
    soma = soma + nota

print(f'\nMostrando as notas: {vetor_nota}')

media = soma / QUANTIDADE

print(f'\nMédia: {soma}')

if soma >= 7:
    print('\nTurma Aprovada')
else:
    print('\nReprovada')

acima_da_media = 0

print('\nNotas acima da média: ')
for nota in vetor_nota:
    if nota > media:
        print(nota)
        acima_da_media = acima_da_media + 1

print(f'\nQuantidade de notas acima da média: {acima_da_media}')