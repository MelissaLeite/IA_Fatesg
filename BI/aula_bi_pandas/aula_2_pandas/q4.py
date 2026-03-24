"""
Questao 4
Uma empresa de vendas possui um DataFrame com as colunas ’Sede A’ e
’Sede B’. Escreva um codigo que:
1. Crie uma nova coluna chamada ’Total Vendas’ com a soma das duas sedes.
2. Adicione uma coluna chamada ’Imposto’ calculada como 10% do valor da
’Sede A’.
"""

import pandas as pd
import math

v1 = 50589.98
v2 = 78654.33

dados = [[
    v1,
    v2,
    v1+v2,
    v1*0.10
]]

#criando dataframe
df = pd.DataFrame(
    dados,
    columns=['Sede A', 'Sede B', 'Total Vendas', 'Imposto'],
)

#printando
print(df)