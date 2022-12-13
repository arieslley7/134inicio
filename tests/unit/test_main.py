from main import somar, dividir


def testar_somar():
    # 1 - Configura
    num_a = 8
    num_b = 7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(num_a, num_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido

def teste_dividir_Positivo():
    # 1 - Configura
    # 1.1  - Dados de Entrada
    num_a = 36    
    num_b = 4

    # 1.2  - Dados Esperados
    resultado_esperado = 9

    # 2 - Executa
    resultado_obtido = dividir(num_a, num_b)


    # 3 - Valida
    assert resultado_obtido == resultado_esperado

def teste_dividir_negativo():
        # 1 - Configura
        # 1.1  - Dados de Entrada
        num_a = 36
        num_b = 0

        # 1.2  - Dados Esperados
        resultado_esperado = 'Não dividirás por zero'

        # 2 - Executa
        resultado_obtido = dividir(num_a, num_b)

        # 3 - Valida
        assert resultado_obtido == resultado_esperado

    # TDD = Test Driven Development - Desenvolvimento Direcionado por teste.

    # - Criar todos os testes de unidade no começo
    # -  Execultar todos os testes pelo menos uma vez por dia..

    # TDD : Teste é uma medida de progresso.
