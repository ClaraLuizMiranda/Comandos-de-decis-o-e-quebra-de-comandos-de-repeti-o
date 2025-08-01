Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
◦ adição (opção 1)
◦ subtração (opção 2)
◦ multiplicação (opção 3)
◦ divisão (opção 4)
◦ saída (opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5).

print("1 - Adicao")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")
print("5 - Saida")

while True:
    x=int(input())
    if x==5:
        break
            
        
    n1=float(input())
    n2=float(input())
        
    if x==1:
        print(f'{n1+n2:.2f}')
    if x==2:
        print(f'{n1-n2:.2f}')
    if x==3:
        print(f'{n1*n2:.2f}')        
    if x==4:
        print(f'{n1/n2:.2f}')
    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Saida")    
