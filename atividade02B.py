##EX-B
# Crie um programa que peça ao usuário para digitar dois números e, 
# em seguida, informe qual deles é o maior.
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if(a > b):
    print(a, "é maior")
elif(a < b):
    print(b, "é maior")
else:
    print(a, "e", b, "são iguais")