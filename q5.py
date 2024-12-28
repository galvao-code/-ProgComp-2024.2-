# Código feito por Jullyana Pessoa e João Victor Gomes

import datetime
# declaramos o contador que será usados para contar os sábados
contador = 0
# usamos o datetime para usarmos a data de hoje e também a "data zero" que seria 27/04/1968, como pedido na questão
hoje = datetime.datetime.today()
data_zero = datetime.datetime(1968, 4, 27)

# para descobrirmos o total de dias passados da data zero até hoje, fizemos uma subtração 
total_dias = hoje - data_zero
# já aqui fizemos uma divisão inteira dos dias passados por 7, pois sábados são contados de 7 em 7 dias
sabados = total_dias//7

# aqui é impresso a quantidade total dos dias que se passaram
print(f'A quantidade de dias de {data_zero} até {hoje} é:  {total_dias}')
# já aqui a quantidade total de sábados
print(f'A quantidade total de sábados é: {sabados}')
