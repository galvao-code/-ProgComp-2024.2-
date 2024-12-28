import datetime

contador = 0
data_zero = datetime.datetime(1968, 4, 27)
hoje = datetime.datetime.today()

total_dias = hoje - data_zero

data_atual = data_zero
#while data_atual <= hoje:
    #if data_atual.weekday() == 5:  # 5 representa sábado
        #contador += 1
    #data_atual+= 1  # Incrementa um dia




print (f'A quantidade de dias de {data_zero.date()} até {hoje.date()} é: {total_dias.days}')