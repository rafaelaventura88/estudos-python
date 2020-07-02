#constantes são escritas com letra maiúscula
#constantes quando não queremos que o valor
#seja alterado.
X = "X"
O = "O"
VAZIO = " "

#tabuleiro = [0,1,2
 #            3,4,5
  #           6,7,8

#tabuleiro = [X, O, X,
 #             O, X, O,
  #            O, VAZIO, X]

tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
              VAZIO, VAZIO, VAZIO]
#
#tabuleiro = [X, O, X,
 #             X, X, VAZIO,
  #            O, O, O]
#
#tabuleiro  = [ X , O , X ,
 #              O , X , O ,
  #             O , X , O ]




alinhamento = False
vencedor = VAZIO  

#possibilidades de alinhamento HORIZONTAL:             
#if tabuleiro[0] == tabuleiro[1]== tabuleiro[2]:
#    print("O jogo acabou!")
#if tabuleiro[3] == tabuleiro[4]== tabuleiro[5]:
#    print("O jogo acabou!")
#if tabuleiro[6] == tabuleiro[7]== tabuleiro[8]:
#    print("O jogo acabou!")

for i in range(0,9,3):
    if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
    #print("O jogo acabou!")
        alinhamento = True
        vencedor = tabuleiro[i]

    
#possibilidades de alinhamento VERTICAL:
#if tabuleiro[0] == tabuleiro[3]== tabuleiro[6]:
#    print("O jogo acabou!")
#if tabuleiro[1] == tabuleiro[4]== tabuleiro[7]:
#    print("O jogo acabou!")
#if tabuleiro[2] == tabuleiro[5]== tabuleiro[8]:
#    print("O jogo acabou

if not alinhamento:
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
            #print("O jogo acabou!")
            alinhamento = True
            vencedor = tabuleiro[i]


    
 #possibilidade de alinhamento DIAGONAL:
#if tabuleiro[0] == tabuleiro[4]== tabuleiro[8]:
#    print("O jogo acabou!")
#if tabuleiro[2] == tabuleiro[4]== tabuleiro[6]:
#    print("O jogo acabou!")  

if not alinhamento:
    for i in range(0,3,2):
        #assim que começar i == 0 logo [0+0=0]
        #4 se mantém
        #i =0 logo [8 -0 = 8]: primeira diagonal 0,4,8!!
        #no segundo for, i começa com 2
        #logo [0 + 2= 2], 4 se mantém
        #e [8 - 2 = 6]: segunda diagonal 2,4,6!!
        if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
            #print("O jogo acabou
            alinhamento = True
            vencedor = tabuleiro[i]


if alinhamento:
    print("Vencedor: ", vencedor)
elif not VAZIO in tabuleiro:
    print("Deu velha! O jogo empatou!")
else:
    print("VAZIO: jogo não foi preenchido!")