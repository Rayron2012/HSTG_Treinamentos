''''''

'''
Módulo os e pathlib
Os módulos os e pathlib são uns dos melhores módulos/bibliotecas para controlar as pastas e arquivos do seu computador. 
Existem alguns outros módulos que podem auxiliar dependendo do que você está querendo fazer, mas em essência conseguiremos usar esses módulos para resolver nossos desafios.

Usaremos aqui o pathlib por ele funcionar bem independente do sistema operacional que você está usando.

Atenção Especial
Normalmente os caminhos em computadores Windows, Mac ou Linux são diferentes, mas isso é algo que o pathlib vai resolver para a gente

Módulo shutil
Para as ações de copiar e colar arquivo, até conseguimos fazer com os módulos os e pathlib, mas é mais difícil e com maior margem de erro. MAS, existe o módulo shutil para ajudar nisso

Importando os Módulos
Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo
Descobrindo onde está o nosso arquivo
Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo
Navegando até uma pasta específica
Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo
Listando todos os arquivos da Pasta Atual
Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo
Criando uma pasta
Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo
Verificando se um Arquivo Existe
Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo
Copiando um Arquivo
Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo
Movendo um Arquivo
Tipo de célula incompatível Clique duas vezes para inspecionar/editar o conteúdo

'''

import shutil
from pathlib import Path

# print(Path.cwd())
caminho = Path('C:/Users/rayro/OneDrive/GITHUB/HSTG_Treinamentes/Análise da Dados com o Pandas + Integração Python e Excel/Z_Arquivos_Lojas')
'''Sempre colocar barra normal no lugar da barra invertida'''


# print(caminho)
arquivos = caminho.iterdir()

for arquivo in arquivos:
    # print(arquivo)
    if (caminho / Path('202004_Morumbi_SP.csv')).exists():
        print("Existe")



# Criar novas pastas, passar o caminho / o nome da pasta
# Path(caminho/'Nova Pasta').mkdir()

copiar_aqui = Path('C:/Users/rayro/OneDrive/GITHUB/HSTG_Treinamentes/Análise da Dados com o Pandas + Integração Python e Excel/Z_Arquivos_Lojas/202004_Shopping Tijuca_RJ.csv')
colar_aqui = Path('C:/Users/rayro/OneDrive/GITHUB/HSTG_Treinamentes/Análise da Dados com o Pandas + Integração Python e Excel/Z_Arquivos_Lojas/Nova Pasta/202004_Shopping Tijuca_RJ_V2.csv')
shutil.copy2(copiar_aqui, colar_aqui)




