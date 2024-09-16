import os
os.system("cls || clear")
QUANTIDADE_NUMEROS = 5 
lista_vetores = []
maior_numero = 0
menor_numero = 0
soma_pares = 0
soma_impares = 0
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
soma_geral = 0

# Variáveis para armazenar os números
for i in range(5): 
    numero = int(input(f"digite seu {i+1} numero: "))

    if numero % 2 == 0 : 
        quantidade_pares += 1
        soma_pares += numero
        media_pares = soma_pares / quantidade_pares
    else:
        quantidade_impares += 1
        soma_impares += numero
        media_impares = soma_impares / quantidade_impares
    if numero < 0:
        quantidade_negativos += 1
    else: 
        quantidade_positivos += 1 
    
    lista_vetores.append(numero)

    maior_numero = max(lista_vetores)
    menor_numero = min(lista_vetores)


if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    media_pares = 0

if quantidade_impares > 0:
    media_impares = soma_impares / quantidade_impares
else:
    media_impares = 0

    media_geral = (soma_impares + soma_pares)/QUANTIDADE_NUMEROS


 























print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")