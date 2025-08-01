Faça um função que receba a data atual (cadeia de caracteres no formato “DD/MM/AAAA”) e retorne uma string com a data onde o mês está no formato textual por extenso. Considere que a data é válida. Exemplo: Data: 01/01/2000, retornar: 1 de janeiro de 2000.

def funcao(x):
    dd = int(x[0:2])
    mm = x[3:5]
    aaaa = x[6:10]

    mesporextenso = ""

    if mm == "01":
        mesporextenso = "janeiro"
    if mm == "02":
        mesporextenso = "fevereiro"
    if mm == "03":
        mesporextenso = "marco"
    if mm == "04":
        mesporextenso = "abril"
    if mm == "05":
        mesporextenso = "maio"
    if mm == "06":
        mesporextenso = "junho"
    if mm == "07":
        mesporextenso = "julho"
    if mm == "08":
        mesporextenso = "agosto"
    if mm == "09":
        mesporextenso = "setembro"
    if mm == "10":
        mesporextenso = "outubro"
    if mm == "11":
        mesporextenso = "novembro"
    if mm == "12":
        mesporextenso = "dezembro"
    
    return f"{dd} de {mesporextenso} de {aaaa}"
