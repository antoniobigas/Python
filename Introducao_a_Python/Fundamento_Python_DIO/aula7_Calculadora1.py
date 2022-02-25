# Metodos e funções, como declarar, vantagens, como implementar classes, e vantagens de como utilizar classes

# diferenca de metodo e funçao. no python metodo chama-se definicao.

# def define a função, e impoe um retorno com o return.
from re import A


class Calculadora:
    def __init__(self, num1, num2):   
        self.valor_a = num1
        self.valor_b = num2   

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


#estanciar uma classe
calculadora = Calculadora(10, 2) #estanciar uma classe.
print('a soma entre 10 e 2 e {}'.format(calculadora.soma()) )
print('A subtracao de 10 e 2 e: {}'.format(calculadora.subtracao()))
print('A multiplicacao de 10 e 2 e: {}'.format(calculadora.multiplicacao()))
print('A divisao de 10 e 2 e: {}'.format(calculadora.divisao()))
