Escreva um programa que leia duas palavras e diga qual delas vem primeiro na ordem alfabética. Não use nenhuma funcionalidade do python que já faça isso. Dica: ‘a’ é menor do que ‘b’.

p1 = str(input())
p2 = str(input())

prim_l= ''

taman_p1 = 0
for char in p1: 
    taman_p1 += 1
taman_p2 = 0
for char in p2: 
    taman_p2 += 1
minimo = 0
if taman_p1 < taman_p2:
    minimo = taman_p1
else:
    minimo = taman_p2

diferenca = 0

for i in range(minimo):
    
    valor_char1 = ord(p1[i])
    valor_char2 = ord(p2[i])
    
    if valor_char1 < valor_char2:
        prim_l = p1
        diferenca = 1 
        break 
    elif valor_char2 < valor_char1:
        prim_l = p2
        diferenca = 1 
        break 
if diferenca == 0: 
    if taman_p1 < taman_p2:
        prim_l= p1
    elif taman_p2 < taman_p1:
        prim_l = p2
    else:
        
        prim_l= p2

print(prim_l)
