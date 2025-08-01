aça um algoritmo que, dados dois números inteiros, seja capaz de obter o quociente inteiro da divisão entre o maior e o menor deles. Não use a operação de divisão (/), nem a operação de divisão inteira (//) e nem a operação de resto da divisão inteira (%).


n1 = int(input())
n2 = int(input())

maiorn = 0
menorn = 0

if n1 > n2:
    maiorn = n1
    menorn= n2
else:
    maiorn = n2
    menorn = n1

r = 0

if menorn == 0:
    
    print(0) 
else:
    n_temp = maiorn
    while n_temp >= menorn:
        n_temp -= menorn 
        r += 1 
    print(r)
    
