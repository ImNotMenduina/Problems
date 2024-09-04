fat = [
    {"estado":"SP", "valor": "67.836,43"} ,
    {"estado":"RJ", "valor": "36.678,66"} ,
    {"estado":"MG", "valor": "29.229,88"} ,
    {"estado":"ES", "valor": "27.165,48"},
    {"estado":"Outros", "valor": "19.849,53"}
]

def faturamento_mensal(fat):
    total = 0.0
    for dado in fat:
        #formata para o padrao 10.0
        valor = dado["valor"].replace('.','')
        valor = valor.replace(',','.')
        valor = float(valor)
        total += valor
        dado["valor"] = valor
    return total

def percentual(total, amostra):
    return float(amostra)/float(total) * 100

total_mensal = faturamento_mensal(fat)

for dado in fat:
    print(dado["estado"], ":" , round(percentual(total_mensal, dado["valor"]), 2) , "%")


