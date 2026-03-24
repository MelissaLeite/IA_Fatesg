"""
Questao 3
Crie um DataFrame utilizando duas Series distintas. A primeira Series deve
conter os nomes de tres produtos e a segunda seus precos. Defina manualmente
os  indices das Series como ’p1’, ’p2’ e ’p3’ antes de uni-las no DataFrame.
"""

import pandas as pd

#criando dados SEM dicionario
info_produtos = [['Smartwatch Amazfit 6', 619.29], ['Geladeira Frost Free', 5299.99], ['Ar Condicionado Split LG Dual Inverter', 1890.78]]

#criando dataframe
df = pd.DataFrame(
    info_produtos,
    columns= ['Produto', 'Preço'],
    index=['p1', 'p2', 'p3']
    )

#exibindo dataframe
print(df)