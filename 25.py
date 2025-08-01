Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.

somap= 0
contp= 0
while contp < 10:    
    n = float(input())        
    if n > 0:
        somap += n       
        contp+= 1
media = somap / contp
print(f' {media:.2f}')
