from audioop import mul
# usar hashtag para fazer comentários em python

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado =  (' Soma: {soma}.'
'\n Subtracao: {subtracao} .'
'\n multiplicacao: {multiplicacao}.'
'\n divisao: {divisao}.'
'\n resto: {resto}.'.format(soma=soma,
                            subtracao=subtracao,
                            multiplicacao=multiplicacao,
                            divisao=divisao,
                            resto=resto) )
print(resultado)

# o format concatena dentro da string
# print('Soma:'+str(soma))
#print('Subtracao: '+ str(subtracao))
# print(multiplicacao)
# print(int(divisao))  #int transforma para numero inteiro. float = quebrado.
# print(resto)
#x = '1'
#soma2 = int(x) + 1
# print(soma2)
