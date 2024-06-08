# C - Agora adicione ao programa anterior uma tentativa máxima de 4 vezes para errar a senha.

senha = '123'
tentativa = input("Digite a senha: ")
quantTentativa = 4

while (senha != tentativa) and (quantTentativa>1):
    quantTentativa = quantTentativa - 1
    if quantTentativa == 1: 
        tentativa = input(f"Senha errada, você só pode errar mais {quantTentativa} vez!\nTente novamente: ")
    else: 
        tentativa = input(f"Senha errada, você só pode errar mais {quantTentativa} vezes!\nTente novamente: ")

if senha == tentativa:
    print("Senha correta!")
else:
    print("Senha bloqueada por excesso de tentativas.")