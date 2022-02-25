# aprender a utilizar e interargir modulos. entender como trabalhar com varios modulos
#aprender a acessar classes e metodos do modulo.
#Entendo como trabalhar com funções anonimas (lambda)

#cada arquivo .py são um módulo do python. e eles podem interarir entre eles, pode ser feito ate do console.
#para importar utilizar FROM NOME DO ARQUIVO IMPORT METODO ou FUNCAO.
#para importar mais de um metodo ou função exemplo na linha 12.

from doctest import testfile
from aula7_televisao import Televisao
from aula7_calculadora2 import Calculadora
from aula8_contador_letras import contador_letras, teste


if __name__ == '__main__':
    televisao = Televisao ()
    televisao.power()
    print('Televisao esta ligada:{} '.format(televisao.ligada))
    calculadora = Calculadora()
    print('A soma de 5 e 10 e: {}'.format(calculadora.soma(5, 10)))
    lista = ['cachorro', 'gato', 'elefante']
    total_letras=contador_letras(lista)
    print('Total de letras de cada palavra da lista {}'.format(total_letras))
    print(teste())



