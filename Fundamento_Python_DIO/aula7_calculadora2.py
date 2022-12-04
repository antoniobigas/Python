#calculadora, sem os números pre instanciados, vc instancia o valor na hora que for fazer a chamada


class Calculadora:
   # def __init__(self):   
    #    pass #nao faz nada, deixa vazio. prof mandou apagar 
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

if __name__ == '__main__':
    calculadora = Calculadora()
    print('a soma entre 10 e 2 e: {}'.format(calculadora.soma(10, 2)) )
    print('A subtracao de 10 e 2 e: {}'.format(calculadora.subtracao(10, 2)))
    print('A multiplicacao de 10 e 2 e: {}'.format(calculadora.multiplicacao(10, 2)))
    print('A divisao de 10 e 2 e: {}'.format(calculadora.divisao(10, 2)))