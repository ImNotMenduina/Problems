import json
import math

def abrir_arquivo() :
    f = open('dados.json')
    data = json.load(f)
    f.close()
    return data

def media_mensal(data) :
    soma = 0.0
    total_registros = 0
    for d in data :
        valor = float(d["valor"])
        soma += valor
        if valor != 0.0:
            total_registros += 1
    return soma/total_registros

def maior_menor_faturamento(media) :
    menor = math.inf
    maior = -math.inf
    dias_media_mensal = 0
    for d in data : 
        num = float(d["valor"])
        if num > media:
            dias_media_mensal += 1
        if menor > num and num != 0.0:
            menor = num
        if maior < num:
            maior = num
    return (maior, menor, dias_media_mensal)

data = abrir_arquivo()
media = media_mensal(data)
maior, menor, dias_media_mensal = maior_menor_faturamento(media)

print("Menor Faturamento : ", menor)
print("Maior Faturamento : ", maior)
print(dias_media_mensal, "dias superiores à média mensal de ", media)



