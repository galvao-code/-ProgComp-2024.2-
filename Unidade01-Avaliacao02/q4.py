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
chutes = 5

while chutes >= 0:
        print("\033[1;3m Digite todas as suas tentativas em caixa alta! Exemplo: PORTA")
        tentativa = input("\033[m Revele o mistério, qual é a palavra? ")
        if tentativa == palavra1 or tentativa == palavra2:
            print("Impossível! Você é um gênio.")
            break
        else:
            tentativa_p1 = ""
            tentativa_p2 = ""   

            for i in range(len(palavra1)):
                if tentativa[i] == palavra1[i]:
                    tentativa_p1 += palavra1[i]
                else:
                    tentativa_p1 += "_"
            for i in range(len(palavra2)):
                if tentativa[i] == palavra2[i]:
                    tentativa_p2 += palavra2[i]
                else:
                    tentativa_p2 += "_"
        print(f"Progresso na palavra 1: {tentativa_p1}")
        print(f"Progresso na palavra 2: {tentativa_p2}")
    chutes -= 1
            if chutes > 0:
                print(f"Não foi dessa vez! Você tem mais {chutes} tentativas.")
            else:
                print("Suas tentativas acabaram. Foi por pouco!")
if chutes == 0:
    print("as palavras corretas eram: ", palavra1, " e ", palavra2)
