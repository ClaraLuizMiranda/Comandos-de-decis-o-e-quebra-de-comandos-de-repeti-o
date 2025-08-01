Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva, para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

import math
while True:
    n=float(input())
    if n<=0:
        print()
        break
    q=n**2
    c=n**3
    r=math.sqrt(n)
    if n > 0:
        print(f'{q:.2f}')
        print(f'{c:.2f}')
        print(f'{r:.2f}')
    else:
        print()
        
    
