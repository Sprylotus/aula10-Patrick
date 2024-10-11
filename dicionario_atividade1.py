import os


notas = {}


for i in range(3):
    os.system('cls')
    aluno = input('digite o nome: ')
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    nota3 = float(input('digite a terceira nota: '))
    nota4 = float(input('digite a quarta nota: '))
    soma = nota1 + nota2 + nota3 + nota4  
    media = soma / 4

    notas[aluno] = {
    'Nota 1': nota1,
    'Nota 2': nota2,
    'Nota 3': nota3,
    'Nota 4': nota4,
    'Média': media
    }

print(notas)