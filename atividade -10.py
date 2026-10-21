import os
os.system("cls")

idades = []

for i in range(5):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa (0 a 120): "))
    
    while idade < 0 or idade > 120:
        print("Valor inválido! A idade deve estar entre 0 e 120.")
        idade = int(input(f"Digite novamente a idade da {i+1}ª pessoa (0 a 120): "))
    
    idades.append(idade)


maior_idade = idades[0]
menor_idade = idades[0]
maiores_de_idade = 0

for i in range(5):
    if idades[i] > maior_idade:
        maior_idade = idades[i]
        
    if idades[i] < menor_idade:
        menor_idade = idades[i]
        
    if idades[i] >= 18:
        maiores_de_idade += 1


print("\n--- Resultados ---")
print(f"Maior idade: {maior_idade}")
print(f"Menor idade: {menor_idade}")
print(f"Quantidade de maiores de idade (≥ 18): {maiores_de_idade}")