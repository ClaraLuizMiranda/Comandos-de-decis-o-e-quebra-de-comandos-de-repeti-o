Faça um algoritmo que leia um número inteiro e imprima seus divisores.

n=int(input())
cont=1
while cont<=n:
    if n%cont==0:
        print(cont)
    cont+=1    
