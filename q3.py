# Código feito por Jullyana Pessoa e João Victor Gomes
x = 2
primos = 0
ult_primo = 0
numeros = []
contador = 0
numero = 50

while x <= numero:
    div = 1
    ndiv = 0
    while div <= x:
        if x % div == 0:
            ndiv += 1
        div += 1
    if ndiv == 2:
        primos += 1
        if x % 2 != 0:
            if ult_primo != 0 and x - ult_primo == 2:
                numeros.append ([ult_primo, x])
                contador+=1
            ult_primo = x
    x+=1

print(f'A quantidade de pares de números primos ímpares até {numero} são: {contador}')
print(f'Os números são: {numeros}')

    
