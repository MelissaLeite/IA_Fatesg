"""
Questao 1
Uma escola precisa organizar os dados de seus alunos. Crie um DataFrame
a partir de um dicionario contendo o nome de cinco alunos e suas respectivas
idades. O codigo deve exibir o DataFrame final utilizando o indice padrao
automatico. 
"""

import pandas as pd

#criando dicionario
dados = {'Nome': pd.Series(['Mateus', 'Igor', 'Felipe', 'Melissa', 'Adroaldo']),
         'Idade': pd.Series([25, 24, 29, 28, 26])
         }

#criando dataframe
df = pd.DataFrame(dados)

#exibindo dataframe
print("Exibindo dataframe:")
print(df)

#exibindo dataframe como excel
print("Exibindo dataframe como excel:")
print(df.T)