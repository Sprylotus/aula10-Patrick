import os

os.system('cls')


dic = {
    'nome':'Patrick',
    'idade':18,
    'celular':'96981-8293',
    'CPF':'123.456.789-10'
}

dic1 = {
    'nome':'Maria'
}

# ACESSAR OS VALORES DO DICIONÁRIO
print(dic['nome'])
print(dic['idade'])
print(dic['celular'])
print(dic['CPF'])


# ALTERAR OS VALORES DO DICIONÁRIO
dic['nome'] = 'Paula'
print(dic)

# DICIONÁRIO 1 - CRIANDO NOVAS CHAVES E VALORES PARA O DICIONÁRIO
dic1['email'] = 'maria@gmail.com'
dic1['idade'] = 25
print(dic1)

# REMOVER CHAVES DO DICIONÁRIO - del
del dic1['email']

# DICIONÁRIO - REMOVER CHAVES DO DICIONÁRIO - pop retorna o valor da chave apagada
print(dic.pop('idade', 'não encontrado'))
print(dic)