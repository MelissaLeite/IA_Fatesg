"""
Questao 6
Utilizando um DataFrame que contem informacoes de paises e tem como indice
o nome do pais (ex: ’Brasil’, ’Argentina’, ’Chile’), utilize o metodo loc para
recuperar e imprimir apenas os dados referentes ao ’Brasil’.
"""

import pandas as pd

dados = [['Brasil'], ['Argentina'], ['Chile']]

#criando dataframe
df = pd.DataFrame (
    dados,
    columns=['Países'],
    index=['Brasil', 'Argentina', 'Chile']
)

#exibindo dataframe
print(df)

#localizando info
print("O país Brasil está no índice: ")
print(df.iloc[0])