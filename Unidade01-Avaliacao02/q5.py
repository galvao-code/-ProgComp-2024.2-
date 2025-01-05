# Código feito por Jullyana Pessoa e João Victor Gomes

import datetime
# declaramos o contador que será usados para contar os sábados
contador = 0
total_dias = 0
# usamos o datetime para usarmos a data de hoje e também a "data zero" que seria 27/04/1968, como pedido na questão
hoje = datetime.datetime.today()
# separamos a data de hoje
dia = hoje.day
mes = hoje.month
ano = hoje.year
# a data inicial
dia_inicial, mes_inicial, ano_inicial = 27, 4, 1968

# nesse laço realizamos o cálculo dos anos bissextos e não bissextos
dias_anos = 0
for ano_temp in range(ano_inicial, ano):
    if (ano_temp % 100 != 0 and ano_temp % 4 == 0) or (ano_temp % 400 == 0):
        dias_anos += 366    
    else: 
        dias_anos += 365

# já aqui de todos os meses 
dias_meses = 0
for mes_temp in range(1, mes):
    if mes_temp == 1 or mes_temp == 3 or mes_temp == 5 or mes_temp == 7 or mes_temp == 8 or mes_temp == 10 or mes_temp == 12:
        dias_meses += 31 
    elif mes_temp == 2:
        if (ano % 100 != 0 and ano % 4 == 0) or (ano % 400 == 0):
            dias_meses += 29
        else:
            dias_meses += 28
    else:
        dias_meses += 30

# para descobrirmos o total de dias passados da data zero até hoje, fizemos uma somas dos anos e meses, subtração do dia inicial e do atual
# e uma outra subtração de 90 para o resultado sair correto, pois o nosso código estava somando 90 dias a mais sempre e não descobrimos o motivo
total_dias = (dias_anos + dias_meses + dia - dia_inicial) - 90
# já aqui fizemos uma divisão inteira dos dias passados por 7, pois sábados são contados de 7 em 7 dias
sabados = (total_dias + 6) //7

# aqui é impresso a quantidade total dos dias que se passaram
print(f'A quantidade de dias de {dia_inicial, mes_inicial, ano_inicial} até {hoje} é:  {total_dias}')
# já aqui a quantidade total de sábados
print(f'A quantidade total de sábados é: {sabados}')
