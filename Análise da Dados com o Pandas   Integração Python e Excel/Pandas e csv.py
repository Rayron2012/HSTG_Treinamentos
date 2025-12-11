import pandas as pd

vendas_df = pd.read_csv(r'C:\Users\rayro\Downloads\Contoso - Cadastro Produtos - Contoso - Cadastro Produtos.csv', sep=';')


vendas_df.info

print(vendas_df.head())

print(vendas_df.head(10))