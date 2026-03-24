"""
Questao 5
Dado um DataFrame de clientes, escreva o codigo necessario para excluir a
coluna ’CPF’ usando o comando del. Em seguida, exclua a coluna ’Telefone’
usando o metodo pop() e exiba o conteudo da coluna removida.
"""

import pandas as pd

dados = [
    ['Melissa', '00522802257', '62981422262'],
    ['Mateus', '36770656078', '6228367537'],
    ['Igor', '00554442086', '6225774571'],
    ['Felipe', '94336995079', '6224783171']
]

df = pd.DataFrame(
    dados,
    columns=('Clientes', 'CPF', 'Telefone')
)

print(df)

#excluindo a coluna CPF
inserir = int(input('Informe a coluna que deseja excluir da listagem: 1 - CPF | 2 - Telefone : '))
if inserir == 1:
    del df['CPF']
    print(df)
#excluindo a coluna Telefone
elif inserir == 2:
    df.pop('Telefone')
    print(df)
else:
    print("comando inválido")



