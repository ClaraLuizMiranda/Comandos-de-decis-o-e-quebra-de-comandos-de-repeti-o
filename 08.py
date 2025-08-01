Faça um programa que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário:
◦ 1: Média entre os números digitados
◦ 2: Diferença do maior pelo menor
◦ 3: Produto entre os números digitados
◦ 4: Divisão do primeiro pelo segundo
Se a opção digitada for inválida, mostrar uma mensagem de erro e terminar a execução do programa. Dica do Brother: Na operação 4 o segundo número deve ser diferente de 0.

n1=float(input())
n2=float(input())
x=int(input())

if x == 1:
    print(f'{(n1+n2)/2:.2f}')
if x == 2:
    if n1>n2:
        print(n1-n2)
    else:
        print(n2-n1)
if x == 3:
    print(f'{n1*n2:.2f}')
if x == 4:
    if n2 != 0:
        print(f'{n1/n2:.2f}')
    else:
        print('Erro')
if x<1:
    print('Erro')
if x>4:
    print('Erro')    
        
