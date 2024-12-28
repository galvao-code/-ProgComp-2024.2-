
# Código feito por Jullyana Pessoa e João Victor Gomes Galvão

#Aqui declaramos as variáveis que vamos utilizar. 

#A variável x é o ponto de partida pro while. 
#primos é quantidade de primos. 
#ult_primo é o último valor primo encontrado
#contador será a quantidade de pares consecutivos encontrados
#numero é o valor máximo de comparação

x = 2
primos = 0
ult_primo = 0
numeros = []
contador = 0
numero = 50

#usamos esse laço para realizar operações enquanto o x for menor igual ao valor máximo
while x <= numero:
    div = 1
    ndiv = 0
    #aqui verificamos se o número é primo 
    while div <= x:
        if x % div == 0:
            ndiv += 1
        div += 1
    #depois do while, se o número de divisões for igual a 2, o número é primo
    if ndiv == 2:
        primos += 1
        #aqui verificamos se o número é ímpar
        if x % 2 != 0:
            #verificamos se os últimos dois primos ímpares encontrados são consecutivos
            if ult_primo != 0 and x - ult_primo == 2:
                #numeros.append ([ult_primo, x]) 
                #se forem consecutivos, ele incrementa o contador que será usado para mostrar a quantidade de pares
                #são consecutivos quando a diferença entre os dois primos do par é 2
                contador+=1
            ult_primo = x
    #por último incrementamos o x para testar com o próximo número 
    x+=1

print(f'A quantidade de pares de números primos ímpares até {numero} são: {contador}')
#print(f'Os números são: {numeros}')

    
    