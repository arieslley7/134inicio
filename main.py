import pytest

def imprimir_oi (nome):
    print(f'Olá, {nome}')

def somar(num_a, num_b):
    return num_a + num_b


def dividir(num_a, num_b):
    try:
        return num_a / num_b
    except ZeroDivisionError:
        return 'Não dividirás por zero'
if __name__ == '__main__':
    imprimir_oi ('Arieslley')

    resultado = somar(17, -6)
    print(f'A soma: {resultado}')



