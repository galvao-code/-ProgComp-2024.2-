# Código feito por Jullyana Pessoa e João Victor Gomes
x = 2
primos = 0
contador = 0
numeros = []
while x <= 50:
    div = 1
    ndiv = 0
    while div <= x:
        if x % div == 0:
            ndiv += 1
        div += 1
    if ndiv == 2:
        primos += 1
        if x % 2 != 0:
            #numeros.append(x)
            contador += 1
    x+=1

print(f'A quantidade de número primos ímpares é: {contador}')
#print(numeros)

    