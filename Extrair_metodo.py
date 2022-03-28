from Classes_Funcoes import *
from constantes import *

def aparece(msg, tamanho):
    i = 0
    l = []
    while i < len(msg):
        m = mensagem(msg[i], tamanho[i], cor_b)
        l.append(m)
        i += 1
    return l