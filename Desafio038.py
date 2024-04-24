# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor é maior, o segundo valor é maior, não existe valor maior os dois são iguais.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('O primeiro número é {} e o segundo número é {}'.format(n1,n2))

if n1 > n2:
    print('O primeiro número é maior que o segundo!')
elif n2 > n1:
    print('O segundo número é maior que o primeiro!')
else:
    print('Não existe valor maior, os dois são iguais!')
