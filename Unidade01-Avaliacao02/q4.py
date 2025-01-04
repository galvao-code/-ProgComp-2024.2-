import random
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

palavra1 = random.choice(palavras)
palavra2 = random.choice(palavras)
while palavra2 == palavra1:
    palavra2 = random.choice(palavras)

chutes = 6
print(palavra1)
print(palavra2)
acertou_p1 = False
acertou_p2 = False
tentativa_p1 = "_" * len(palavra1)
tentativa_p2 = "_" * len(palavra2)  

while chutes >= 0:
        print("\033[1;3m Digite todas as suas tentativas em caixa alta! Exemplo: PORTA \033[m")
        tentativa = input("Revele o mistério, qual é a palavra? ")

        if tentativa == palavra1:
            acertou_p1 = True

        elif tentativa == palavra2:
            acertou_p2 = True

        if acertou_p1 and acertou_p2:
            if chutes == 5 and acertou_p1 == True and acertou_p2 == True:
                print("Impossível, você conseguiu de primeira!")
            elif chutes == 4 and acertou_p1 == True and acertou_p2 == True:
                print("Você é um ninja!")
            elif chutes == 3 and acertou_p1 == True and acertou_p2 == True:
                print("Impressionante!")
            elif chutes == 2 and acertou_p1 == True and acertou_p2 == True:
                print("Interessante!")
            elif chutes == 1 and acertou_p1 == True and acertou_p2 == True:
                print("Pode melhorar...")

            print(f"\033[1;30;42m{palavra1}, {palavra2}\033[m")
            break
        else:
            nova_tentativap1 = ""
            nova_tentativap2 = ""   

            for i in range(len(palavra1)):
                if tentativa[i] == palavra1[i]:
                    nova_tentativap1 += f"\033[1;30;42m{palavra1[i]}\033[m"
                elif tentativa[i] in palavra1:
                    nova_tentativap1 += f"\033[1;30;43m{palavra1[i]}\033[m"
                else:
                    nova_tentativap1 += f"\033[1;30;47m{tentativa_p1[i]}\033[m"
                    
            for i in range(len(palavra2)): 
                if tentativa[i] == palavra2[i]:
                    nova_tentativap2 += f"\033[1;30;42m{palavra2[i]}\033[m"
                elif tentativa[i] in palavra2:
                    nova_tentativap2 += f"\033[1;30;43m{palavra2[i]}\033[m"
                else:
                    nova_tentativap2 += f"\033[1;30;47m{tentativa_p2[i]}\033[m"

            tentativa_p1 = nova_tentativap1 
            tentativa_p2 = nova_tentativap2

        print(f"Progresso na palavra 1: {tentativa_p1}")
        print(f"Progresso na palavra 2: {tentativa_p2}")

        chutes -= 1

        if chutes > 0:
            print(f"Você tem mais {chutes} tentativas.")

        if chutes == 0:
            print(f"as palavras corretas eram: {palavra1} e {palavra2}")
            print("Suas tentativas acabaram. Foi por pouco!")
        
