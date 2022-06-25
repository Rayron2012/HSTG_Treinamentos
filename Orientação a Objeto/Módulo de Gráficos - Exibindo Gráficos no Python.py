'''
Importância

Para exploração e visualização de dados, nada melhor do que usar gráficos para isso. Apesar do Python ser programação, gráficos facilitam d+ em qualquer projeto que trabalhe com dados.
Estrutura
Usaremos o módulo Matplotlib.pyplot, que é o módulo mais usado no Python. Existem outros, como o Seaborn e o Plotly, caso queira ver/usar'''

vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

import matplotlib.pyplot as plt
plt.plot(meses, vendas_meses)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 12, 0, max(vendas_meses)])
plt.show()
