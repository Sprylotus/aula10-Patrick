import os

os.system('cls')


import pandas as pd 

try:

    df_base_de_dados = pd.read_csv('ClassicDisco.csv', sep=',', encoding='utf-8')



    # imprimindo a base de dados completa
    print(df_base_de_dados.info())

except Exception as e:
    print(f'Erro {e}')