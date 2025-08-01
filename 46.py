Faça um programa que, dada uma string, diga se ela é um palíndromo ou não. Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita. Exemplos:
           ovo
           arara
           Socorram-me, subi no onibus em Marrocos.
           Anotaram a data da maratona

def funcao(t):
    t1 = ''
    for i in t:
        if 'a' <= i <= 'z':
            t1 += i
        elif 'A' <= i <= 'Z':
            t1 += chr(ord(i) + 32)
            
    invercao = ''
    tamanho = 0
    for _ in t1:
        tamanho += 1
    
    i = tamanho - 1
    while i >= 0:
        invercao += t1[i]
        i -= 1 
        
    if t1 == invercao:
        return True
    else:
        return False
        
print(funcao(input()))
        

