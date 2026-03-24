"""
Questao 2
Um analista de RH recebeu uma lista de dicionarios contendo informacoes de
funcionarios: [’Nome’: ’Ana’, ’Cargo’: ’Analista’, ’Nome’: ’Bruno’,
’Cargo’: ’Gerente’, ’Bonus’: 500]. Escreva o codigo para transformar
essa lista em um DataFrame e explique (via comentario no codigo) o que acon-
tece com a coluna ’Bonus’ para a funcionaria Ana.
"""

import pandas as pd

#criando dicionario
info_funcionarios = {
    'Nome': pd.Series(['Ana', 'Bruno']),
    'Cargo': pd.Series(['Analista', 'Gerente']), 
    'Bonus': pd.Series([500]) #só possui 1 informacao, logo, entende-se que é referente ao primeiro registro da lista e por isso, o Bruno ficará como NaN.
}

#criando dataframe
df = pd.DataFrame(info_funcionarios)

#exibindo dataframe
print(df)