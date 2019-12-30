import math

numero_de_pessoas = int(input('Digite o numero de pessoas: '))

resultado = math.log(numero_de_pessoas) / math.log(2)

if resultado == math.floor(resultado):
    print('Você deve ficar na posição 1')
else:
    resto = numero_de_pessoas - (2 ** math.floor(resultado))
    resultado = 3
    for i in range(1, resto):
        resultado += 2

    print('Você deve ficar na posição {}'.format(resultado))