Faça um programa que simule uma calculadora com as 4 operações básicas. O usuário digita o primeiro número, escolhe a operação e em seguida digita o segundo número, exatamente nessa ordem. O programa deve mostrar o resultado da operação.

n1=float(input())
s=str(input(''))
n3=float(input())
if s=='+':
    print(n1+n3)
if s=='-':
    print(f'{n1-n3:.2f}')
if s=='*':
    print(f'{n1*n3:.2f}')
if s=='/':
    print(f'{n1/n3:.2f}')
