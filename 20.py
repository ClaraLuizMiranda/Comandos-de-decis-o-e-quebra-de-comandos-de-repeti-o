Faça uma função para verificar se um número é um quadrado perfeito. Ex: 1, 4, 9...

import math
def funcao(n):
    
    r=math.sqrt(n)
    
    if r**2==n:
        return 'True'
    else:
        return 'False'
