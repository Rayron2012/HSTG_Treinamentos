''''''

'''Em algumas ocasio~es é necessario codificar para padões brasileiros para entender o ~ ou Ç'''
'''Formatos brasileitos de codificação: ("ISO-8859-1", "latin1", "utf-8", "cp1252)"'''


import pandas as pd

vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

# print(vendas_df)
# print(produto_df)
# print(loja_df)
# print(clientes_df)


# Para apagar subistitiur a antiga variavel, passar coluna com axis = 1 eixo de colunas
'''clientes_df = clientes_df.drop(["Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10"], axis=1)
print(clientes_df)'''

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

# print(clientes_df)
# print(produto_df)
# print(loja_df)



'''Em casos de mesclar Dataframes (Tabelas), usar o merge novo_datafreme = dataframe1.merge(dataframe2, on="coluna")'''

# Se a coluna tiver nomes diferentes, sera necessario renomealas
# dataframe.rename({'coluna1': 'coluna nova'})

vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})

print(vendas_df)