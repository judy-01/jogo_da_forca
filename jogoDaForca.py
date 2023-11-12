import random

def jogo_da_forca():
    lista_de_palavras = ["Python", "Java", "computer", "hacker", "world"]
    numeroAleatorio = random.randint(0, 4)
    palavra = lista_de_palavras[numeroAleatorio]
    palpite_errado = 0
    fases =  ["",
             "________________",       
             "|                ",
             "|        |       ",
             "|        0       ",
             "|       /|\      ",
             "|       / \      ",
             "|                ",
              "----------------"      
              ]
    
    
    letras_restantes = list(palavra)
    quadro_de_letras = ["__"] * len(palavra)
    ganhar = False
    print('Bem-vindo(a) ao jogo da forca')
    while palpite_errado < len(fases) - 1:
        print('\n')
        adivinhar = input("Digite uma letra :")
        if adivinhar in letras_restantes:
            indice_de_caract = letras_restantes.index(adivinhar)
            quadro_de_letras[indice_de_caract] = adivinhar
            letras_restantes[indice_de_caract] = '$'
        else:
            palpite_errado += 1
        print((' '.join(quadro_de_letras)))
        print('\n'.join(fases[0: palpite_errado + 1]))
        if '__' not in quadro_de_letras:
            print('Você ganhou, a palavra é :')
            print(' '.join(quadro_de_letras))
            ganhar = True
            break
    if not ganhar:
        print('\n'.join(fases[0: palpite_errado]))
        print('Você perdeu, a palavra seria  {}'.format(palavra))

jogo_da_forca()


