O numero 3025 possui uma característica interessante, sendo a seguinte: 30 + 25 = 55 e 552 = 3025. Elaborar um algoritmo que verifique todos os números de quatro algarismos que apresentem essa propriedade. Não use operações com strings.

for i in range(1000,10000):
    num12 = i // 100
    num34 = i % 100
    
    s=num12 +num34
    r= s**2
    
    if r==i:
        print(i)
