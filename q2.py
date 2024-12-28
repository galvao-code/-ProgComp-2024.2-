# Código feito por Jullyana Pessoa e João Victor Gomes

# declaramos as variáveis do menore maior número estabelecido na questão
numero = 10
num_final = 10000
# o contador com o valor de 0 para ir aumentando a quantidade de números palíndromos quando forem encontrados
contador = 0

# utilizamos o for para criar o laço pois temos uma sequência certa, adicionamos +1 por que se não ficaria até 99999
for numero in range (numero, num_final + 1):
  # variável que será usada para construir o número invertido
  num_invertido = 0
  numero_orig = numero
# criamos o while para fazer a inversão dos números
  while numero > 0:
    # extraimos o último dígito do número, por causa do resto da divisão
    ult_digt = numero % 10
    # adiciona o último dígito ao número invertido
    num_invertido = num_invertido * 10 + ult_digt
    # remove o último digito do número original e o loop continua acontecendo até o valor ficar em 0
    numero //= 10
   # verifica se o número é um políndromo, se for acrescenta ao contador
    if numero_orig == num_invertido:
        contador += 1
    

print(f"o total de números palíndromos de 10 a 100000 é: {contador}")
