# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar no serviço militar, se é a hora de se alistar, se já passou do tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Digite o ano do seu nascimento '))

anoatual = date.today().year
alistamento = anoatual - ano
x = 18 - alistamento
y = alistamento - 18

if alistamento < 18:
    print('Você ainda não completou a idade miníma para se alistar')
    print('Faltam ainda {} anos para se alistar!'.format(x))
elif alistamento == 18:
    print('Chegou a hora de se alistar!')
else:
    print('Você já passou {} anos do alistamento!'.format(y))
