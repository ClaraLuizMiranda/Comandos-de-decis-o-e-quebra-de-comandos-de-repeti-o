Escreva um programa que substitui as ocorrências de um caractere 0 em uma string pelo caractere 1. Não use nenhuma funcionalidade do python que já faça isso.

p = input()
p1= ''

for i in p:
    if i=='0':
        p1+='1'
    else:
        p1+=i

print(p1)
