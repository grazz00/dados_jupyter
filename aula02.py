##operadores lógicos 

#AND --> no operador AND precisamos que todas as condições 
#analisadas sejam TRUE para se ter um resultado TRUE, caso 
#contrário, o resultado será FALSE

# print("True and True =>", True and True)
# print("True and False =>", True and False)
# print("False and True =>", False and True)
# print("False and False =>", False and False)

#verificando se uma pessoa pode dirigir 
temCarro = True
temHabilitacao = True

#print(temCarro == True and temHabilitacao == True)


##OR --> No operador OR, se for encontrado pelo menos uma das 
#condições como TRUE, o resultado será TRUE, SÓ teremos um resultado
#false, se TODAS as condições forem falsas. 

# print("True or True =>", True or True)
# print("True or False =>", True or False)
# print("False or True =>", False or True)
# print("False or False =>", False or False)

#verificação se o usuario comprou um filme
compraFilme = True
assinante = False

# print(compraFilme == True or assinante == True)

##Condicionais (IF/ELSE/ELIF)
#verificando se uma pessoa é maior de idade
idade = 20

if(idade >= 18): #Verifico se a idade é maior ou igual a 18 e 
    print("É maior de idade") #mostro o texto "é maior de idade"
else: #senão for maior 
    print("Não é maior de idade") #mostra o texto "não é maior de idade"

##EX-A
# Crie algoritmo receba um número um numero e retorne "positivo" se o número for 
# maior que zero, "negativo" se for menor que zero.
    
##EX-B
# Crie um programa que peça ao usuário para digitar dois números e, 
# em seguida, informe qual deles é o maior.
    
#EX-C
#Peça ao usuario para digitar uma letra e determine se é uma vogal ou uma consoante
