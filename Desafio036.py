# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comptador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
fina = int(input('Quantos anos de financiamento? '))
prestacao = casa / (fina * 12)
minimo = sal * (30 / 100)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f} reais'.format(casa,fina,prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
