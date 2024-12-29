# Código feito por Jullyana Pessoa e João Victor Gomes

import datetime
# declaramos o contador que será usados para contar os sábados
contador = 0
total_dias = 0
# usamos o datetime para usarmos a data de hoje e também a "data zero" que seria 27/04/1968, como pedido na questão
hoje = datetime.datetime.today()

dia = hoje.day
mes = hoje.month
ano = hoje.year

dia_inicial, mes_inicial, ano_inicial = 27, 4, 1968

dias_anos = 0
for ano in range(ano_inicial, hoje.year):
    if (ano % 100 != 0 and ano % 4 == 0) or (ano % 400 == 0):
        bissexto = 1
        dias_anos += 366    
    else: 
        dias_anos += 365

dias_meses = 0
for mes in range(mes_inicial, hoje.month):
    if mes in (1 , 3, 5 , 7, 8, 10, 12):
        dias_meses += 31 
    elif mes == 2:
        dias_meses += 28 + bissexto
    else:
        dias_meses += 30

# para descobrirmos o total de dias passados da data zero até hoje, fizemos uma subtração 
total_dias = dias_anos + dias_meses + (hoje.day - dia_inicial)
# já aqui fizemos uma divisão inteira dos dias passados por 7, pois sábados são contados de 7 em 7 dias
sabados = total_dias//7

# aqui é impresso a quantidade total dos dias que se passaram
print(f'A quantidade de dias de {dia_inicial, mes_inicial, ano_inicial} até {hoje} é:  {total_dias}')
# já aqui a quantidade total de sábados
print(f'A quantidade total de sábados é: {sabados}')
