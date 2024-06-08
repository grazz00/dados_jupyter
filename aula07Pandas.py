#importando a biblioteca pandas
import pandas as pd

# Importe a biblioteca pandas
import pandas as pd

#Crie uma série contendo os números de 1 a 5 e calcule a soma de todos os elementos.
s1 = pd.Series([1, 2, 3, 4, 5])
print("Exercício 1:")
print("Soma dos elementos:", s1.sum())

# Crie uma série contendo os dias da semana (segunda a sexta-feira) e imprima o último elemento
dias_semana = pd.Series(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'])
print("\nExercício 2:")
print("Último dia da semana:", dias_semana.iloc[-1])

# Crie uma série contendo os nomes de três cores de sua escolha e ordene-os em ordem alfabética.
cores = pd.Series(['Azul', 'Verde', 'Vermelho'])
print("\nExercício 3:")
print("Cores em ordem alfabética:", cores.sort_values())

# Crie uma série contendo as idades de três pessoas em sua família e calcule a média das idades.
idades = pd.Series([30, 25, 40])
print("\nExercício 4:")
print("Média das idades:", idades.mean())

#Crie uma série contendo três valores booleanos (True ou False) que representem respostas a perguntas 
#simples e conte quantas respostas são True.
respostas = pd.Series([True, False, True])
print("\nExercício 5:")
print("Número de respostas verdadeiras:", respostas.sum())