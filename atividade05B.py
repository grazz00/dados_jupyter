#B-Com o programa anterior, calcule a média das notas digitas.
notas = []
i = 0 
while i < 5:
    notas.append(float(input("Digite uma nota")))
    i = i + 1 

print(notas)

soma = 0
for n in notas:
    soma = soma + n

print(soma/5)
