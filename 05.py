Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

  import math
n=float(input())
if n > 0:
    print(f'{math.sqrt(n):.2f}')
else:
    print("Numero invalido")
    

