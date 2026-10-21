import os
os.system("cls")


A = []
B = []
C = []

print("Digite 5 Numeros Inteiros para o Vetor A: ")
for i in range(5):
    numero = int(input(f"A[{i}]: "))
    A.append(numero)

print("Digite 5 Numeros Inteiros para o Vetor B: ")
for i in range(5):
    numero = int(input(f"B[{i}]: "))
    B.append(numero)

for i in range(5):
    soma = A[i] + B[i]
    C.append(soma)

print(f"\n--- Resultado ---")
print("vetor A:", A)
print("vetor B:", B)
print("Vetor C (A + B):", C)