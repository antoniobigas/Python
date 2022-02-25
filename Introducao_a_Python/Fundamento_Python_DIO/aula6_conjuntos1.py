# o que é um conjunto ?  sao conjuntos aritiméticos.

#conjunto = {1, 2, 3 ,4} #se inserir valores duplicados, o conjunto nao imprime novamente {4,4,4} so imprime uma vez o 4.
#print(type(conjunto)) #class 'set' = conjunto !
#conjunto.add(5)
#conjunto.discard(2)
#print(conjunto)

conjunto = {1, 2, 3, 4 , 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2) #comando union une os dois conjuntos. e cria uma nova variavel com os valores dos dois conjuntos e ainda exclui duplicidades.
print('Uniao: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2) #tanto faz a sequencia que declara o conjunto
print('Interseccao: {}' .format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2) # .diference para imprimir a diferenca dos conjuntos
print('Diferenca entre 1 e 2: {}'.format (conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferenca entre 2 e 1: {}'.format(conjunto_diferenca2))

#diferenca assimetrica = tudo que não tem nos dois, aquilo que so tem no a ou no b!
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferenca simetrica: {}'.format(conjunto_dif_simetrica))  # se tiver valores totalmente iguais retorna 0, se tiver somente um valor diferente retorna somente este numero, etc.

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A e subconjunto de B: {}'.format(conjunto_subset)) # ele responde com true, porque o conjunto b contem os elementos do priemruio conjunto

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B e um superconjunto de A: {} '. format(conjunto_superset))  # a é um subconjunto de B, e B e um superconjunto de B, pois B contem todos elementos de A.


lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante', 'elefante']
conjunto_animais = set(lista) #dessa forma fez conversão, tira a duplicidade e ainda traz em ordem alfabética.
print('Esta e um conjunto de animais: {}'.format(conjunto_animais))
lista_animais = list(conjunto_animais) # usar o LIST para transformar a o conjunto novamente em lista
print('Esta e uma lista de animais: {}'.format(lista_animais))