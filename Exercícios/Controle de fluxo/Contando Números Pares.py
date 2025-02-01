numeros = [1, 4, 7, 9, 20, 23, 45, 169, 200, 274]

contador = 0 

for x in numeros:
    if x % 2 == 0:
        contador += 1

print(f"A quantidade de numeros pares é: {contador}")   