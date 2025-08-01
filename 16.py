Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.


n=int(input())
if n<0:
    print()
else:    
    maior_n = n 
    menor_n = n
    while True:
        n=int(input())
        if n<0:
            break
        if n > maior_n:
            maior_n = n
        if n < menor_n:
            menor_n = n
    print(maior_n)
    print(menor_n)
