Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

menorn = 0
maiorn = 0 

for i in range(1, 11): 
    n = float(input())  
    if i == 1:
        menorn = n
        maiorn = n
    else:       
        if n < menorn:
            menorn= n        
        if n > maiorn:
            maiorn = n
print(f"{menorn:.2f}")
print(f"{maiorn:.2f}")
