Escreva um algoritmo que leia um conjunto de n números e mostre qual foi o menor e o maior valor fornecido.

menorn = 0
maiorn = 0 
n=int(input())
for i in range(1,n+1): 
    n1 = float(input())  
    if i == 1:
        menorn = n1
        maiorn = n1
    else:       
        if n1 < menorn:
            menorn= n1        
        if n1 > maiorn:
            maiorn = n1
print(f"{menorn:.2f}")
print(f"{maiorn:.2f}")
    
