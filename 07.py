Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário então imprima: "Emprestimo nao concedido", caso contrário imprima: "Emprestimo concedido".

s=float(input())
p=float(input())

porcetagem = (s/10)*2

if p<=porcetagem:
    print('Emprestimo concedido')
    
else:
    print('Emprestimo nao concedido')
