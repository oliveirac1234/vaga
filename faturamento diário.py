import json

# Exemplo de dados em JSON
dados = '''
{
    "faturamento": [1000, 2000, 1500, 0, 0, 3000, 2500, 0, 4000, 5000, 0, 0, 3500, 4500, 0, 0, 6000, 5500, 0, 0, 7000, 6500, 0, 0, 8000, 7500, 0, 0, 9000, 8500]
}
'''

# Carregando os dados
faturamento = json.loads(dados)['faturamento']

# Filtrando dias sem faturamento
faturamento_filtrado = [valor for valor in faturamento if valor != 0]

# Calculando menor e maior valor
menor_valor = min(faturamento_filtrado)
maior_valor = max(faturamento_filtrado)

# Calculando a média
media = sum(faturamento_filtrado) / len(faturamento_filtrado)

# Contando dias acima da média
dias_acima_media = sum(1 for valor in faturamento_filtrado if valor > media)

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")