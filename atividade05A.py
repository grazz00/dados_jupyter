#A-Faça um programa que leia 5 notas e armazene em uma lista.
notas = []
i = 0 
while i < 5:
    notas.append(float(input("Digite uma nota")))
    i = i + 1 

print(notas)