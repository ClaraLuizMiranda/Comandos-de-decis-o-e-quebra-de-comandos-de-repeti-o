Faça um programa que receba uma frase e imprima-a de maneira invertida, trocando as letras A (maiúsculas ou minúsculas) por *. Não use nenhuma funcionalidade do python que já faça isso.

def funcao(frase):
    invercao = ''
    t = 0
    for _ in frase:
        t += 1

    x = t - 1
    while x >= 0:
        letra = frase[x]
        comparacao = letra

        if letra == 'A':
            comparacao= '*'
        if letra == 'a':
            comparacao = '*'
        
        if comparacao != '*':
            invercao += letra
        else:
            invercao += '*'
        
        x -= 1
            
    return invercao

print(funcao(input()))

