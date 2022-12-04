x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y = []

for i in range(len(x)-1, -1, -1):
    y.append(x[i])

print(y)

# o problema de usar este metodo, é que criamos uma nova variavel para armazenar a lista.