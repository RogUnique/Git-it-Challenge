import random

separadores = ['+', '.','>', '<', '§','\n','\t']


def cria_txt():
    with open("numeros.txt","w")  as txt:
       i = 0
       while i < 20:
           indice = random.randint(0,len(separadores ) - 1)
           num_atual = random.randint(0,9999)
           txt.writelines(str(num_atual) + get_separador(indice))
           i += 1
    txt.close()

def get_separador(posicao):
    return separadores[posicao]

cria_txt()

