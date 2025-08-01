Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.

n = int(input())

m_n= 0  
cont= 0
n2 = 1    

for i in range(n):
    n1 = int(input())
    
    if n2 == 1:
        m_n = n1
        cont = 1
        n2 = 0  
    else:
        if n1 > m_n:
            m_n = n1
            cont = 1 
        elif n1 == m_n:
            cont += 1 

if n > 0:
    print(m_n)
    print(cont)
else:
    
    print(0)
    print(0)
