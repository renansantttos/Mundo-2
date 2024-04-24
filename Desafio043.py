# Calcule o IMC e mostre 18.5 abaixo do peso, entre 18.5 e 25 peso ideal, 25 até 30 sobrepeso, 30 até 40 obesidade e acima de 40 obesidade morbida.

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC está em {:.1f} e você está ABAIXO DO PESO'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC está em {:.1f} e você está no PESO IDEAL'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC está em {:.1f} e você está SOBREPESO'.format(imc))
elif imc >=30 and imc < 40:
    print('Seu IMC está em {:.1f} e você está em OBESIDADE'.format(imc))
else:
    print('Seu IMC está em {:.1f} e você está em OBESIDADE MÓRBIDA'.format(imc))
