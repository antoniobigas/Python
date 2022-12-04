x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
fim = len(x) -1 #fim recebe x -1, recebendo o valor final. 14
## O for percore toda lista e divide em 2, sem sobrar nada.
##
for i in range(len(x)//2):
        aux = x[i]  #aux recebe x na posicao i
        x[i] = x[fim] # x na posicao i, recebe fim
        x[fim] = aux #fim recebe aux
        fim -= 1

print(x)
