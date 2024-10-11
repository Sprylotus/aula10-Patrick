import pandas as pd


dados = {
    'cargos':['assistente','auxiliar','gerente'],
    'salários':[2500, 1000, 750]
}

dados_bi = pd.DataFrame(dados)
print(dados_bi)

dados_cargos = pd.Series(dados['cargos'])
print(type(dados_cargos.values))

df_linha = (dados_bi.iloc[1]['cargos'])
print(df_linha)