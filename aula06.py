#Funções
#para criar uma função, usamos a palavra reservada 'def', seguido
#do nome da função e parenteses '()', toda função pode ter ou não 
# ter parametros. Parametros são uma especie de "variavel" conhecida 
# apenas dentro daquela função a paravra return indica o que a função
# precisa devolver ao final da execução 
# def quadrado(x):
#     return x * x

# print(quadrado(8))
# print(quadrado(2))


def sub(c, d): 
    sub = c - d
    return sub

def result(x, y):
   return soma(x, x) - sub(y, x)

# print(result(1, 2))

def soma(a, b):
    soma = a + b
    return soma

def exibeResultado(nome, x, y):
     #interpolação é o conceito de usar string e variaveis dentro 
     #do mesmo elemento ==> f''
    s = soma(x, y)
    print(f'Olá {nome}, sua soma é {s}')
            # 'Olá', nome, 'sua soma é', soma


#crie um código que pergunte a uma pessoa se ela tem habilitação 
#e se o documento do veiculo esta em dia, caso contrario 
#o programa deve exibir veículo apreendido 


# Crie uma calculadora simples que permita ao usuário realizar 
# operações básicas de adição, subtração, multiplicação e divisão.
























