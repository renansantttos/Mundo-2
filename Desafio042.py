# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    #print('Os segumentos acima PODEM FORMAR um triângulo!')
    if a == b == c:
        print('Os segumentos acima PODEM FORMAR um triângulo EQUILÁTERO!!')
    elif a != b != c != a:
        print('Os segumentos acima PODEM FORMAR um triângulo ESCALENO!')
    else:
       print('Os segumentos acima PODEM FORMAR um triângulo ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')
