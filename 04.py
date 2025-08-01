Ler três valores e determinar o maior entre eles.

  n1 = float(input())
n2 = float(input())
n3 = float(input())
x = n1

if n2 > x:
    x = n2
if n3 > x:
    x = n3

print(f"{x:.2f}")
