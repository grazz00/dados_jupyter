#EX-C
#Peça ao usuario para digitar uma letra e determine se é uma vogal ou uma consoante

letra = input("Digite uma letra: ")

letra = letra.lower()

if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print(letra, "é uma vogal")
else: 
    print(letra, "é uma consoante")