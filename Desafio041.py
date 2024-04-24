# A Confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos mirim, até 15 infantil, até 19 junior até 20 anos senior, acima master

from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))

anoatual = date.today().year
idadeatleta = anoatual - ano

if idadeatleta <= 9:
    print('O atleta com idade de {} anos e está escrito na categoria MIRIM!'.format(idadeatleta))
elif idadeatleta >= 10 and idadeatleta <=14:
    print('O atleta com idade de {} anos e está escrito na categoria INFANTIL!'.format(idadeatleta))
elif idadeatleta >=15 and idadeatleta <=19:
    print('O atleta com idade de {} anos e está escrito na categoria JUNIOR!'.format(idadeatleta))
elif idadeatleta == 20:
    print('O atleta com idade de {} anos e está escrito na categoria SÊNIOR!'.format(idadeatleta))
else:
    print('O atleta com idade de {} anos e está escrito na categoria MASTER!'.format(idadeatleta))
