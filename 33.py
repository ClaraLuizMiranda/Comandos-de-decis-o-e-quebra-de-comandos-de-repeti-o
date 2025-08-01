Dado um número n inteiro e positivo, dizemos que n é perfeito se n for igual à soma de seus divisores positivos diferentes de n. Construa um programa que verifica se um dado número é perfeito. Ex: 6 é perfeito, pois 1 + 2 + 3 = 6.

n = int(input())

soma = 0
cont = 1

while cont < n:   
    if n % cont == 0:       
        soma += cont       
    cont += 1

if soma == n:
    print("Perfeito")
else:
    print("Nao perfeito")
