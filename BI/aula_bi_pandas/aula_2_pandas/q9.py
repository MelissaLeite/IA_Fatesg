"""
Questao 9
Voce tem dois DataFrames: df loja1 e df loja2, ambos com as colunas ’Produto’ e ’Estoque’. Escreva o codigo para concatenar 
(anexar) os dados da loja2 ao final da loja1 e exiba o resultado.
"""

import pandas as pd

#inserindo dados
loja1 = [['Produto A', 239.87], ['Produto B', 298.09]]
loja2 = [['Produto C', 226.78], ['Produto D', 999.99]]

#criando dataframes
loja1 = pd.DataFrame(
    loja1,
    columns=['Produto', 'Estoque']
)

loja2 = pd.DataFrame(
    loja2,
    columns=['Produto', 'Estoque']
)

#imprimindo dataframes
print("Produtos da Loja 1: ")
print(loja1)

print("\nProdutos da Loja 2: ")
print(loja2)

#juntando os dataframes
print("\n Juntando os dados: \n")
df = pd.concat([loja1, loja2], ignore_index=True)
print(df)