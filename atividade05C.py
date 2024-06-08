#C-Peça ao usuário que diga quantas notas quer digitar e em seguida, faça a media.
notas = []
q = int(input("Quantas notas você vai digitas? "))
i = 0 
while i < q:
    notas.append(float(input("Digite uma nota")))
    i = i + 1 

print(notas)

soma = 0
for n in notas:
    soma = soma + n

print(soma/q)


