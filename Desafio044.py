# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: a vista dinheiro/cheque: 10% de desconto, a vista no cartão 5% de desconto, em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros.

produto = float(input('Digite o preço do produto a ser comprado: '))
print('''Escolha uma das condições a seguir:
      [ 1 ] À Vista Dinheiro/Cheque
      [ 2 ] À Vista no Cartão
      [ 3 ] Até 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
condicao = int(input('Digite o número: '))

desconto10 = produto * (10 / 100)
pfinal10 = produto - desconto10

desconto5 = produto * (5 / 100)
pfinal5 = produto - desconto5

aumento30 = produto * (30 / 100)
pfinalm30 = produto + aumento30

if condicao == 1:
    print('O preço normal é de {} e recebe um desconto de 10% e fica no valor de {} reais!'.format(produto,pfinal10))
elif condicao == 2:
    print('O preço normal é de {} e recebe um desconto de 5% e fica no valor de {} reais!'.format(produto,pfinal5))
elif condicao == 3:
    print('Você irá pagar o valor normal de {} reais!'.format(produto))
elif condicao == 4:
    print('O preço normal é de {} e recebe um aumento de 30% e fica no valor de {} reais!'.format(produto,pfinalm30))
else:
    print('Condição de pagamento errada, tente novamente!')
