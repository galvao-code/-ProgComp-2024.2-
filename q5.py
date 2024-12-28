import datetime

contador = 0
hoje = datetime.datetime.today()
data_zero = datetime.datetime(1968, 4, 27)


total_dias = hoje - data_zero

sabados = total_dias//7



print(f'A quantidade de dias de {data_zero} até {hoje} é:  {total_dias}')
print(f'e a quantidade de sábados é: {sabados}')
