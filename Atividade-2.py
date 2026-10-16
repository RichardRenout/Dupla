import os
os.system("cls")

dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

temperaturas = []

for dia in dias:
    temp = int(input(f"Digite a temperatura do dia {dia} "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)


print("\n-----TEMPERATURA DE CADA DIA -----")
for i in range(len(dias)):
    print(f"{dias[i]}: {temperaturas[i]}°C ")



print("\n--- Resumo da Semana ---")
print(f"Média da semana: {media:.2f}°C")
print(f"Maior temperatura registrada: {maior}°C")
print(f"Menor temperatura registrada: {menor}°C")