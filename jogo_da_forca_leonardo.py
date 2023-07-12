import random

# Lista de palavras para o jogo
palavras = ['html', 'algoritmo','backbone','cookies','firewall','intranet','arduino','dashboards','ethernet','gateway']

# Escolhe aleatoriamente uma palavra da lista de palavras
palavra = random.choice(palavras)

# Transforma a palavra escolhida em uma lista de caracteres
lista_caracter_palavra = list(palavra)

# Lista que armazena as letras que foram digitadas pelo usuário
lista_jogada_usuario = []


# Varriáveis para contabilizar as vidas do usuário
vidas = 0
vida_restante = 6

# Regras do Jogo para informar o usuário
print("#### Jogo da Forca ####")
print('Regras:')
print('- Digite uma letra de cada vez')
print('- Não é permitido repetir letras')
print('- Se você acertar a letra, ela é revelada')
print('- Se errar, perde uma vida')
print('- Você tem 6 vidas')
print('Boa sorte!')

# Lista com o desenho da forca
forca = [
    ' +----+ \n |   | \n |     \n |      \n |      \n |       \n=========',
    ' +----+ \n |   | \n |     \n |   0  \n |      \n |       \n=========',
    ' +----+ \n |   | \n |     \n |   0  \n |   |  \n |       \n=========',
    ' +----+ \n |   | \n |     \n |   0  \n |  /|  \n |       \n=========',
    ' +----+ \n |   | \n |     \n |   0  \n |  /|\ \n |       \n=========',
    ' +----+ \n |   | \n |     \n |   0  \n |  /|\\\n |  /    \n=========',
    ' +----+ \n |   | \n |     \n |   0  \n |  /|\\\n |  / \  \n========='
]

# Loop principal do jogo
while vidas < 6:
    print()
    print()

    # Exibe a palavra com tracinhos - e caso uma letra ja foi digitada pelo usuário exibe a letra
    for jogada in palavra:
        if jogada in lista_jogada_usuario:
            print(jogada, end=' ')
        else:
            print('-', end=' ')
    print()

    # Solicita ao usuário que digite uma letra
    jogada = input("Digite uma letra: ")

    # Verifica se a jogada do usuário é uma letra
    if jogada.isalpha() == True:

        # Verifica se a letra já foi digitada anteriormente
        if jogada in lista_jogada_usuario:
            print('Você já digitou essa letra, digite novamente!')

        # Verifica se a jogada do usuário está na palavra, caso sim informo que ele acertou
        elif jogada in lista_caracter_palavra:
            lista_jogada_usuario.append(jogada)
            print('Acertou!!!')

            # Verifica se o usuário acertou todas as letras da palavra
            if len(lista_jogada_usuario) == len(set(lista_caracter_palavra)):
                print()
                print("### Voc^e ganhou :) ###")
                break

        # Caso a jogada do usuário nao esteja na palvra, informa que ele errou e a quantidade de vidas que ele ainda tem
        else:
            vidas += 1
            vida_restante -= 1
            print(forca[vidas])
            if vida_restante < 3:
                print(f'Uhhh! Vidas Restantes: {vida_restante}')

            else:
                print(f'ERRO! Vidas Restantes: {vida_restante}')
        # Verifica se o usuário perdeu todas as vidas
        if vidas == 6:
            print('Você perdeu!')
            break

    # Imprime a forca
    print(forca[vidas])
