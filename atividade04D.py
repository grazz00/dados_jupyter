valor = int(input("Digite um número: "))
acerto = 40

while valor != acerto:
    if(valor>acerto):
        print("Você errou, valor muito alto!")
    else:
        print("Você errou, valor muito baixo!")
    valor = int(input("Digite um outro número: "))
print("Você acertou o número!")

            
