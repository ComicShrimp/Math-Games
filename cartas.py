import random

jogador1 = input('Coloque a sua sequencia: ')
jogador2 = input('Coloque a sua sequencia: ')

def ganhador(vetor):
    tamanho = len(vetor)
    if int(jogador1[2]) == vetor[tamanho - 1] and int(jogador1[1]) == vetor[tamanho - 2] and int(jogador1[0]) == vetor[tamanho - 3]:
        return 1
    elif int(jogador2[2]) == vetor[tamanho - 1] and int(jogador2[1]) == vetor[tamanho - 2] and int(jogador2[0]) == vetor[tamanho - 3]:
        return 2
    else:
        return -1

print('1° jogador: {}\n2° jogador: {}\n\n'.format(jogador1, jogador2))

vetor_saiu = []
while True:
    saiu = random.randint(0, 1)
    print(saiu, end='')
    vetor_saiu.append(saiu)
    
    if len(vetor_saiu) > 3:
        vetor_saiu.pop(0)
        if ganhador(vetor_saiu) == 1:
            print('\n\nJogador 1 ganhou')
            break
        elif ganhador(vetor_saiu) == 2:
            print('\n\nJogador 2 ganhou')
            break
