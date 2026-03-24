"""
Questao 10
Crie um DataFrame com nomes de funcionarios e seus salarios. Em seguida, utilize atributos do Pandas para imprimir:
1. A transposta do DataFrame.
2. Os tipos de dados (dtypes) de cada coluna.
3. A quantidade total de elementos presentes no objeto (size).
4. Apenas as duas ultimas linhas do DataFrame (tail).
"""

import pandas as pd

#criando dicionario
info_funcionarios = {
    'Nome': pd.Series(['Karem', 'Melissa', 'Vitoria', 'Gustavo', 'Adriano']),
    'Salário': pd.Series([8790.98, 5556.66, 2500.76, 432.55, 10879.00]), 
}

#criando dataframe
df = pd.DataFrame(info_funcionarios)

#exibindo dataframe
print("Exibindo dataframe: ")
print(df)

#exibindo dataframe transposto
print("\nExibindo dataframe transposto: ")
print(df.T)

#exibindo os tipos de dados
print("\nExibindo os tipos de dados: ")
print(df.dtypes)

#exibindo o total de elementos
print("\nExibindo o total de elementos: ")
print(df.size)

#exibindo as ultimas linhas
print("\n Exibindo as últimas linhas: ")
print(df.tail(2))