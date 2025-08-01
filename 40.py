Faça um programa que conte o número de 1’s que aparecem em uma string. Exemplo: 0011001 -> 3. Não use nenhuma funcionalidade do python que já faça isso.

  cont= 0
p = input()

for i in p:    
    if i == '1':
        cont += 1 

print(cont)
