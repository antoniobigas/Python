# forcar um erro
# dividir algo por zero, gera erro.

from dis import findlinestarts


lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 5
    numero = lista[1]  # nao temos indice 3 na lista!!!!
except ZeroDivisionError:
    print('Nao e possivel realizar uma divisao por 0 zero')
except ArithmeticError:
    print('houve um erro ao realizar uma operacao aritimetica')
except IndexError:  # erro que gera, quando nao temos nada na lista.
    print('Erro ao Acesar um indice invalido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro{}'.format(ex))
else:
    print('Executa quando nao ocorre excecao')
finally:
    print('Sempre Executa')
    print('Fechando Arquivo')
    arquivo.close()    
