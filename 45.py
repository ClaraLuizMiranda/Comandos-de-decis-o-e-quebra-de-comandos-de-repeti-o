O código de César é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, ‘A’ seria substituído por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente uma função que faça uso desse Código de César, entre com uma string e a quantidade de posições e retorne a string codificada. Exemplo:
String: A LIGEIRA RAPOSA MARROM SALTOU SOBRE O CACHORRO CANSADO
Nova string com 3 posições: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
Observação: caso a letra codificada passe da letra Z, ela deve voltar para o início do alfabeto.

#-*- coding: utf-8 -*-

def funcao(txt, d):
    res = ""
    for c in txt:
        if 'A' <= c <= 'Z':
            i_a = ord('A')
            c_cod = ((ord(c) - i_a + d) % 26) + i_a
            res += chr(c_cod)
        elif 'a' <= c <= 'z':
            i_a = ord('a')
            c_cod = ((ord(c) - i_a + d) % 26) + i_a
            res += chr(c_cod)
        else:
            res += c
    return res
