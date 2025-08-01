Escreva um programa que leia a idade e o primeiro nome de várias pessoas. Seu programa deve terminar quando uma idade negativa for digitada. Ao terminar, seu programa deve escrever o nome e a idade das pessoas mais jovens e mais velhas.

  cont=0

while True:
    nome=str(input())
    idade=int(input())
    
    if idade < 0:
        break
    if cont==0:
        idade_menor=idade
        idade_maior=idade
        nome_jovem=nome
        nome_velho=nome
    else:
        if idade_menor> idade:
            idade_menor=idade
            nome_jovem=nome
        if idade_maior< idade:
            idade_maior=idade
            nome_velho=nome
            
    cont+=1
print(nome_jovem)
print(idade_menor)
print(nome_velho)
print(idade_maior)
    
    
