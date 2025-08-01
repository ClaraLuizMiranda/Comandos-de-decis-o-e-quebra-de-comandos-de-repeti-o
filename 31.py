Faça um programa que receba dois números. Calcule e mostre:
◦ A soma dos números pares desse intervalo de números (intervalo incluindo os números dados);
◦ A multiplicação dos números ímpares desse intervalo (intervalo incluindo os números dados)

n1 = int(input())
n2 = int(input())

if n1 < n2:
    x = n1
    y = n2
else:
    x = n2
    y = n1

s = 0
m = 1 
for i in range(x, y + 1):
    
    if i % 2 == 0: 
        s += i 
    else: 
        m *= i

print(s)
print(m)
