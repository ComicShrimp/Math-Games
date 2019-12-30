import random
import time

total_de_campos = 9
campo_central = 4
numero_de_bolas = 500
numero_de_etapas = 15

campo_inicial = campo_central

def bolinha(campo, etapa):
    etapa += 1
    escolha = random.randint(0, 1)
    
    if escolha == 1 and campo < total_de_campos - 1:
        campo += 1
    elif escolha == 0 and campo > 0:
        campo -= 1
    
    if etapa == numero_de_etapas:
        return campo
        
    return bolinha(campo, etapa)

vetor_resultado = [0] * total_de_campos
for i in range(0, total_de_campos):
    vetor_resultado[i] = 0

for i in range(1, numero_de_bolas + 1):
    vetor_resultado[bolinha(campo_inicial, 1)] += 1

print(vetor_resultado)