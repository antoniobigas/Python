#como usar lambda, contador de letras é o nome da funcao, lambda parametro que sera usado e define como lista

from operator import mul


contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

##lambda usar para simplificar funçoes em uma unica linha.
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print('A soma de 5 e 10 e: {}'.format(soma(5, 10)))
print('A subtracao de 10 e 5 e: {}'.format(soma(10, 5)))

calculadora = {
    'soma': lambda a, b: a + b, 
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora)) #classe dicionario, porque estamos usando a lambda e dentro dela há toda a calculadora. funcao anonima

soma = calculadora ['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']

print('A soma de 10 e 5 e: {}'.format(soma(10, 5)))
print('A multiplicacao de 10 e 2 e: {}'.format(multiplicacao(10, 2)))

