# lacos de repeticao
# for + range percore, pode ser usado (1, 101)  neste caso percore do primeiro ao 101, se nao declarar de onde começa ele inicia do ZERO.;

#a = int(input('Entre com o número: '))
a = int(input('Entre com um valor: '))

for num in range(a+1):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        #print(x, resto)
        if resto == 0:
            div += 1

    if div == 2:
        print(num)
