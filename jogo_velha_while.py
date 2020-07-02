X = "X"
O = "O"
VAZIO = " "

tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
              VAZIO, VAZIO, VAZIO]

jogada = 0

#tabuleiro = [0,1,2
 #            3,4,5
  #           6,7,8
			  
jogo_valido = True
vencedor = False

jogador1 = VAZIO
jogador2 = VAZIO

jogador1 = input("Escolha X ou O: ")

if jogador1 == X:
    jogador2 = O
else:
    jogador2 = X
    
for i in range(0,9,3):
        print(i,"|",i+1,"|",i+2,"----",tabuleiro[i],"|",tabuleiro[i+1],"|",tabuleiro[i+2])  
    
while jogo_valido:
    jogada = jogada + 1    
    casa = int(input("Escolha onde jogar: "))
    
    #nas jogadas de n° ímpar o jogador1 um faz a anotação (X ou O)
    if jogada % 2 == 1:
        tabuleiro[casa] = jogador1
    #nas jogadas de n°par o jogador2 um faz a anotação (X ou O)
    else:
        tabuleiro[casa] = jogador2
    
    for i in range(0,9,3):
        print(i,"|",i+1,"|",i+2,"----",tabuleiro[i],"|",tabuleiro[i+1],"|",tabuleiro[i+2])    

# TODO: verificar se jogo acabou 
#possibilidades de alinhamento HORIZONTAL:             
#if tabuleiro[0] == tabuleiro[1]== tabuleiro[2]:
#    print("O jogo acabou!")
#if tabuleiro[3] == tabuleiro[4]== tabuleiro[5]:
#    print("O jogo acabou!")
#if tabuleiro[6] == tabuleiro[7]== tabuleiro[8]:
#    print("O jogo acabou!")

    for i in range(0,9,3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
            vencedor = tabuleiro[i]

    
#possibilidades de alinhamento VERTICAL:
#if tabuleiro[0] == tabuleiro[3]== tabuleiro[6]:
#    print("O jogo acabou!")
#if tabuleiro[1] == tabuleiro[4]== tabuleiro[7]:
#    print("O jogo acabou!")
#if tabuleiro[2] == tabuleiro[5]== tabuleiro[8]:
#    print("O jogo acabou

    if not vencedor:
        for i in range(3):
            if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
                vencedor = tabuleiro[i]


    
 #possibilidade de alinhamento DIAGONAL:
#if tabuleiro[0] == tabuleiro[4]== tabuleiro[8]:
#    print("O jogo acabou!")
#if tabuleiro[2] == tabuleiro[4]== tabuleiro[6]:
#    print("O jogo acabou!")  

    if not vencedor:
        for i in range(0,3,2):
            if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
                vencedor = tabuleiro[i]


    if vencedor:
        jogo_valido = False
        print("Vencedor: ", vencedor)
    elif not VAZIO in tabuleiro:
            jogo_valido = False
            print("Deu velha! O jogo empatou!")
   
