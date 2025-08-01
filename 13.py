Calcule as raízes da equação do 2o grau. Lembrando que: x = (−b± √∆)/(2a), onde ∆ = b2 − 4ac, e  ax2 + bx + c = 0 representa uma equação do 2o grau. A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Nao eh equacao do 2o grau".
◦ Se ∆ < 0 , não existe raiz real. Imprima a mensagem “Nao existe raiz real”.
◦ Se ∆ = 0 , existe uma raiz real. Imprima a raiz e a mensagem "Raiz unica".
◦ Se ∆ > 0 , Imprima as duas raízes reais.

import math
a=float(input())
b=float(input())
c=float(input())

if a==0:
    print("Nao eh equacao do 2o grau")
   
else:
    d=(b**2) - (4*a*c)
    if d == 0:
        x1 = (f'{(-b + (math.sqrt(d)))/(2*a):.2f}')
        x2 = (f'{(-b - (math.sqrt(d)))/(2*a):.2f}')
        print(x1)
        print("Raiz unica")
    elif d < 0:
        print("Nao existe raiz real")
    elif d > 0:
        x1 = (f'{(-b + (math.sqrt(d)))/(2*a):.2f}')
        x2 = (f'{(-b - (math.sqrt(d)))/(2*a):.2f}')
        print(x1)
        print(x2)
