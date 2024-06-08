# B - Faça um programa que solicite ao usuário que insira uma senha. O programa deve permitir que
# o usuário tente entrar com a senha até que ele acerte a senha correta.
senha = '123'
tentativa = input("Digite a senha: ")

while (senha != tentativa):
    tentativa = input("Senha errada! Tente novamente: ")

print("Senha correta!")