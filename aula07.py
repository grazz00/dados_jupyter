#criando uma função que retorna se um número é positivo ou negativo
def positivoOuNegativo(numero):
    #numero = 1
    if numero > 0:
            return f'{numero} é um valor positivo'
    elif numero < 0:
        return f'{numero} é um valor negativo'
    else:
        return f'{numero} é neutro'
         
# print(positivoOuNegativo(-5))
# print(positivoOuNegativo(50))
# print(positivoOuNegativo(0))

#variaveis globais(todas as funções tem acesso) e locais(visivel 
#somente na função na qual ela é criada) 
val1 = 0 #variavel global

def soma():
    a = 0 #variavel local
    return val1 + a

##tratamento e excessão --> páginas 40 e 41
def div(b):
    try: #o try quer dizer tentar, ou seja, ele tenta 
        #executar sempre este caso
        return val1 / b #variavel parametro--> local
    except: #o except vai tratar as excessões, os casos de erro.
         return 'Erro: Não foi possível dividir'

#print(div(0))








