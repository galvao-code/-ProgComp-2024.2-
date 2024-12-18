# Código feito por Jullyana Pessoa e João Victor Gomes

# declaramos as variáveis do menore maior número estabelecido na questão
numero = 10
num_final = 987631
# o contador com o valor de 0 para ir aumentando a quantidade de números decrescentes quando forem encontrados
contador = 0

# utilizamos o for para criar o laço pois temos uma sequência certa, adicionamos +1 por que se não ficaria até 987360
for numero in range (numero, num_final + 1):
  # declaramos o descrescente true para usarmos mais a frente
  decrescente = True
# criamos o while para procurarmos os números decrescentes e ficar repetindo o loop até o número máximo
  while numero >= 10:
    # aqui extraimos o último dígito do número, por causa do resto da divisão
    a = numero % 10
    # aqui realiza uma divisão inteira e atribui o resultado de volta à variável
    numero //= 10
    # novamente pegamos o último digito e extraímos, só que o outro dígito após o da variável 'a'
    b = numero % 10
    # durante o processo, se b for menor que a, não o torna decrescente, logo decrescente é falso
    if b < a:
      decrescente = False
# se o número for decrescente, irá aumentar 1 no contador
if decrescente:
    contador += 1
    
# e no final, mostramos a quantidade de números entre 10 e 987361
print(f"o total de números decrescentes de 10 a 987631 é: {contador}")
