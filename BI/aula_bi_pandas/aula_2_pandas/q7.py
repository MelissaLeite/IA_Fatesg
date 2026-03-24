"""
Questao 7
Crie um DataFrame com dados de 6 modelos de carros. Escreva o comando que
utiliza o indexador iloc para selecionar e exibir os dados apenas do quarto e
do quinto carro da lista.
"""

import pandas as pd

#criando dicionario
carro = {
    'Carro': pd.Series(['Corolla', 'Civic', 'HB20', 'Onix', 'T-Cross', 'Jeep Compass']),
    'Marca': pd.Series(['Toyota', 'Honda', 'Hyundai', 'Chevrolet', 'Volkswagen', 'Jeep'])
}

#criando dataframe
df = pd.DataFrame(carro)

#imprimindo
print("\nOs veículos cadastrados são: ")
print(df)

#localizando indices
print("\nO quarto veículo da lista é: ")
print(df.iloc[3])

print("\nO quinto veículo da lista é: ")
print(df.iloc[4])