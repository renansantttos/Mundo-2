# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: média abaixo de 5 reprovado, media entre 5 e 6.9 recuperação. média 7 ou superior aprovado.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >=7:
    print('Aluno Aprovado com a média {}!'.format(media))
elif media >=5 and media <=6.9:
    print('Aluno está de recuperação com média {}. Estude mais!'.format(media))
else:
    print('Aluno reprovado com a média {}'.format(media))
