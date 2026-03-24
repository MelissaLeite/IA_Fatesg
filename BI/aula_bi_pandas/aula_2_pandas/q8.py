"""
Questao 8
A partir de um DataFrame com 20 linhas de dados historicos, utilize o operador
de Slicing (dois pontos) para extrair e exibir um novo DataFrame contendo
apenas da 5a ate a 12a linha do conjunto original.
"""

import pandas as pd

# Gerando dados fictícios
dados = {
    'Nome': [f'Pessoa {i}' for i in range(1, 21)],
    'Idade': [20 + i for i in range(20)],
    'Cidade': ['Goiânia'] * 20
}

df = pd.DataFrame(dados)

print("DataFrame original:\n")
print(df)

# 🔹 Aplicando o slicing (5ª até a 12ª linha)
novo_df = df.iloc[4:12]

print("\nDataFrame fatiado (5ª até a 12ª linha):\n")
print(novo_df)