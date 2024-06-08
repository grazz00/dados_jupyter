#A - Faça um programa que solicite um número do usuário e imprima a tabuada (+) desse número até 10.
num = int(input("Digite um número: "))

i = 1

while i <= 10:
    soma = num + i
    print(f"{num} + {i} = {soma}")
    i = i + 1 
