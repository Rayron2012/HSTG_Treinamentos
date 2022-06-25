

import  matplotlib.pyplot as plt
import numpy as np

vendas = np.random.randint(500, 2799, 11)
churn = np.random.randint(300, 1500, 11)
cancelamento = np.random.randint(20, 799,11)
# meses = np.arange(1, 13)
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jun", "Ago", "Out", "Nov", "Dez"]

# plt.plot(meses, vendas, "r--", color='purple')
# plt.axis([0, 50, 0, max(vendas)+100])
# plt.ylabel("Vendas")
# plt.xlabel('Meses')
# plt.show()

# plt.scatter(meses,vendas)
# plt.bar(meses,vendas)


plt.figure(1, figsize=(15, 5))


plt.subplot(1, 3, 1)
plt.bar(meses, vendas, color='grey')
plt.plot(meses, churn, color='purple')
plt.title('Vendas x Churn')
plt.axis([0, max(meses), 0, max(vendas)+500])
plt.axis("auto")
plt.ylabel("Vendas")
plt.xlabel('Meses')
plt.legend(['vendas', 'churn'], fontsize = 8, loc= 'upper left' )


plt.subplot(132)
plt.scatter(meses, churn, color='red')
plt.plot(meses, churn, color="purple")
plt.ylabel("Leads")
plt.xlabel('Meses')
plt.legend(['churn'], fontsize = 8, loc= 'upper left' )
plt.title('Churn')


plt.subplot(133)
plt.plot(meses, cancelamento, color='Purple')
plt.bar(meses, churn, color= 'blue')
plt.scatter(meses, cancelamento, color='red')
plt.ylabel("Cancelamento")
plt.xlabel('Meses')
plt.legend(['Cancelamento', 'Churn'], fontsize = 8, loc= 'upper left' )
plt.title('Leads perdidos x Churn')
plt.show()

