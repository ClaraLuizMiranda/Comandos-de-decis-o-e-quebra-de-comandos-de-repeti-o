Faça um programa que receba um valor inteiro n ≥ 0 e imprima se esse número é primo ou não.

import math
n=int(input())
r=math.sqrt(n)
if n>1:
    for i in range(2, int(r)+1):
        if n%i==0:
            print('Nao primo')
            break
    else:
        print('Primo')
else:
    print('Nao primo')
    
    
    
     
