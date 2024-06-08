print("Escolha: \nTriangulo \nQuadrado \nCirculo")
fig = input("Digite a opção que deseja:")

if(fig == 'triangulo'):
    b = float(input("Qual a base?\n"))
    h = float(input("Qual a altura?\n"))
    resultadoT = (b*h)/2
    print(resultadoT)
elif(fig == 'quadrado'):
    b = float(input("Qual a base?\n"))
    resultadoQ = b**2
    print(resultadoQ)
elif(fig == 'circulo'):
    r = float(input("Qual o raio?\n"))
    resultadoC = 3.14*(r**2)
    print(resultadoC)