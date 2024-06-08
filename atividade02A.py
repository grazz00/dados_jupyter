##EX-A
# Crie algoritmo receba um número e retorne "positivo" se o número for 
# maior que zero, "negativo" se for menor que zero.

valor = float(input("Digite um número"))

if(valor > 0):
    print(valor, "é positivo")
elif(valor == 0):
    print(valor, "é neutro")
else:
    print(valor, "é negativo")