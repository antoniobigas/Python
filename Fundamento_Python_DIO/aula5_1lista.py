lista = [12, 10, 7, 5 ]  #se eu quisesse, poderia inserir 'gato' nesta lista de números, o python permite isso, porem nao e ideal fazer.
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
#print(lista_animal[1])   #dessa forma imprime somente a posicao selecionada


# for X in "lista"  faz o X erdar a string/valor da lista que voce selecionou...
#for x in lista_animal:   
#    print(x)


#print(sum(lista))  #faz a soma da lista...
#print(max(lista)) #traz o maior valor da lista
#print(min(lista)) #traz o menor valor 
#esses exemplos acima tbm funcionam com texto, conforme o abaixo

# print(max(lista_animal))  #letra g, maior da string


# como descobrir se ja incluiram um elemento na lista? EXEMPLO SABER SE JA TEM LOBO

#if 'lobo' in lista_animal:
#       print('existe um LOBO na lista!')
#else:
# #        print('NAO  existe um LOBO na lista')
        #incluir o lobo na lista
     #   lista_animal.append('lobo')
     #  print(lista_animal)
#para retirar o cachoro  da lista / o pop tira o ultimo elemento da pilha! ou vc insere a posição q vc quer retirar
#lista_animal.pop(0)
#print(lista_animal)
#como remover ataves do .remove, inserindo o nome

#lista_animal.remove('elefante')
#print(lista_animal)

# como alterar a lista
#multiplicar a lista 
#nova_lista = lista_animal * 3  #faz ficar com os valores multiplicados!!!
#print(nova_lista)

#como ordenar a lista

#lista.sort()
#lista_animal.sort()
#print(lista)
#print(lista_animal)

#diferenca de tupla e lista = a tupla é imutavel, a lista pode ser alterada.

#como alterar uma posição na lista
lista_animal[0] = 'macaco' #ira substituir cachorro por macaco
print(lista_animal)

# abaixo exemplo de tupla

tupla = (1, 10, 12, 14) #ao inves de colchetes usa parenteses
print(tupla[1])
#tupla[0] = 12 #retorna o seguinte erro TypeError: 'tuple' object does not support item assignment
#fazer um contador abaixo
print(len(tupla))
print(len(lista_animal))

tupla_animal = tuple(lista_animal) #convertendo a lista em tupla

print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100 #desta forma alterei o indice 0 da lista (que era uma tupla e foi transformado em lista)
print(lista_numerica)