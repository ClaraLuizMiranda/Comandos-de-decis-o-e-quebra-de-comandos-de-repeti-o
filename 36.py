Faça uma função que retorne o maior fator primo de um número.

def funcao(x):
    
    maiorf = 1 

    while x % 2 == 0:
        maiorf= 2 
        x //= 2         
    d = 3
    while d * d <= x:
        while x % d == 0:
            maiorf = d 
            x //= d         
        d += 2 
    if x > 1:
        maiorf= x
        
    return maiorf
