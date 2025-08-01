Faça uma função chamada de simplificada que receba como parâmetro o numerador e o denominador de uma fração. Esta função deve simplificar a fração recebida dividindo o numerador e denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplificada para 3/5 dividindo o numerador e denominador por 12.

  def simplificar(n, d):        
    a = n
    b = d
    
    while b != 0:        
        x = b
        b = a % b
        a = x
        
    mdc = a
    
    n1 = n // mdc
    d1 = d // mdc
    
    return n1, d1

