Faça um programa que leia 3 notas, verifique se as notas são válidas e exiba na tela a média destas notas com duas casas decimais. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.00 e 10.00, onde caso a nota não possua valor válido, este fato deve ser informado ao usuário e o programa termina.

soma=0
cont=0

for i in range(3):
    n=float(input())
    if n>= 0:
        if n <= 10:
            soma+=n
            cont+=1
        else:
            print('Nota invalida')
            break
    else:
        print('Nota invalida')
        break
if cont==3:
    print(f'{soma/3:.2f}')
