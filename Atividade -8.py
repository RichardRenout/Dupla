import os
os.system("cls")

nomes = []
salarios = []

for i in range(5):
    nome = input(f"Digite o Nome do  {i+1} funcionario: ")
    salario = float(input(f"Digite o salario de {nome}: "))
    nomes.append(nome)
    salarios.append(salario)


maior_salario = salarios[0]
nome_maior = nomes[0]
qtd_acima_2000 = 0

for i in range(5):
    if salarios[i] > maior_salario:
        maior_salario = salarios[i]
        nome_maior = nomes[i]

    if salarios[i] > 2000.00:
        qtd_acima_2000 += 1


print("\n--- Resultados ---")
print(f"Funcionário com maior salário: {nome_maior} (R$ {maior_salario:.2f})")
print(f"Quantidade de funcionários que ganham acima de R$ 2.000,00: {qtd_acima_2000}")