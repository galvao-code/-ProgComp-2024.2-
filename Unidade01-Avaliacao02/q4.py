# Código feito por Jullyana Pessoa e João Victor Gomes

import random

# Configuração de cores
reset_cor = '\033[0;0m'  # Retoma a cor padrão
letra_inexiste = '\033[40m'     # Fundo preto
letra_pos_errado = '\033[43m'   # Fundo amarelo
letra_pos_correta = '\033[42m'  # Fundo verde

#CONJUNTO DE PALAVRAS
palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)

#SORTEIO DE PALAVRAS E IMPEDIMENTO DE PALAVRAS REPETIDAS
palavra1 = random.choice(palavras)
palavra2 = random.choice(palavras)
while palavra2 == palavra1:
    palavra2 = random.choice(palavras)

#DECLARAÇÃO DAS VARIÁVEIS PRINCIPAIS
chutes = 5
print(palavra1)
print(palavra2)
acertou_p1 = False
acertou_p2 = False
tentativa_p1 = "_" * len(palavra1)
tentativa_p2 = "_" * len(palavra2)

#COMEÇO DA ITERAÇÃO
while chutes >= 0:
    print("\033[1;3m Digite todas as suas tentativas em caixa alta! Exemplo: PORTA \033[m")
    tentativa = input("Revele o mistério, qual é a palavra? ")
    #CASO A PALAVRA INSERIDA NÃO ESTIVER NO CONJUNTO(SEJA POR ESCRITA ERRADA, CARACTERES PROIBIDOS OU NÚMEROS)
    #OS LAÇOS SUBSEQUENTES NÃO SERÃO EXECUTADOS E A TENTATIVA NÃO SERÁ GASTA
    
    #USAMOS O CONTINUE PARA PULAR O RESTANTE DO LAÇO CASO O IF SEJA TRUE
    if tentativa not in palavras:
        print("Palavra inválida. Digite novamente")
        continue

    if tentativa == palavra1:
        acertou_p1 = True

    elif tentativa == palavra2:
        acertou_p2 = True
    
    #MENSAGEM DE RETORNO BASEADO EM QUANTOS CHUTES O USUÁRIO ACERTOU
    if acertou_p1 and acertou_p2:
        if chutes == 5:
            print("Impossível, você conseguiu de primeira!")
        elif chutes == 4:
            print("Você é um ninja!")
        elif chutes == 3:
            print("Impressionante!")
        elif chutes == 2:
            print("Interessante!")
        elif chutes == 1:
            print("Pode melhorar...")

        print(letra_pos_correta + palavra1, palavra2 + reset_cor)
        break
    else:
        nova_tentativap1 = ""
        nova_tentativap2 = ""

        #VERIFICAÇÃO DA PALAVRA 1
        if acertou_p1:
            nova_tentativap1 = letra_pos_correta + palavra1 + reset_cor
        else:
            #A PARTIR DAQUI INICIAREMOS OS LAÇOS FOR
            i = 1
            for c in tentativa:
                #AQUI VAMOS PERCORRER CADA LETRA DA PALAVRA INSERIDA E COMPARAR COM A PALAVRA SORTEADA
                if c in palavra1:
                    #NO CASO DA LETRA E A POSIÇÃO CONDIZEREM IRÁ COLORIR DE VERDE
                    if c == palavra1[i]:
                        nova_tentativap1 += (letra_pos_correta + c + reset_cor)
                    #DO CONTRÁRIO, IRÁ COLORIR DE AMARELO CASO A LETRA ESTEJA NA POSIÇÃO ERRADA
                    else:
                        nova_tentativap1 += (letra_pos_errado + c + reset_cor)
                #E NO CASO DE NÃO PERTENCER PALAVRA, SERÁ REESCRITA SEM COR
                else:
                    nova_tentativap1 += (letra_inexiste + c + reset_cor)
                i += 1

        # VERIFICAÇÃO DA PALAVRA 2
        if acertou_p2:
            tela_2 = letra_pos_correta + palavra2 + reset_cor
        else:
            i = 0
            for c in tentativa:
                #AQUI VAMOS PERCORRER CADA LETRA DA PALAVRA INSERIDA E COMPARAR COM A PALAVRA SORTEADA
                if c in palavra2:
                    #NO CASO DA LETRA E A POSIÇÃO CONDIZEREM IRÁ COLORIR DE VERDE
                    if c == palavra2[i]:
                        nova_tentativap2 += (letra_pos_correta + c + reset_cor)
                    #DO CONTRÁRIO, IRÁ COLORIR DE AMARELO CASO A LETRA ESTEJA NA POSIÇÃO ERRADA
                    else:
                        nova_tentativap2 += (letra_pos_errado + c + reset_cor)
                 #E NO CASO DE NÃO PERTENCER PALAVRA, SERÁ REESCRITA SEM COR
                else:
                    nova_tentativap2 += (letra_inexiste + c + reset_cor)
                i += 1

        #ARMAZENAMOS A O VALOR COM A CORES RESPECTIVAS NAS VARIAVEIS DE TENTATIVA PARA MOSTRAR AO USUÁRIO O PROGRESSO
        tentativa_p1 = nova_tentativap1
        tentativa_p2 = nova_tentativap2

    #PRINT DO PROGRESSO
    print(f"Progresso na palavra 1: {tentativa_p1}")
    print(f"Progresso na palavra 2: {tentativa_p2}")

    #DECREMENTAMOS O CHUTE A CADA LOOP
    chutes -= 1
    if chutes > 0:
        print(f"Você tem mais {chutes} tentativas.")

    #REVELAMOS AS PALAVRAS CORRETAS CASO O USUÁRIO NÃO ACERTE ATÉ CHEGAREM EM 0
    if chutes == 0:
        print(f"As palavras corretas eram: {palavra1} e {palavra2}")
        print("Suas tentativas acabaram. Foi por pouco!")
