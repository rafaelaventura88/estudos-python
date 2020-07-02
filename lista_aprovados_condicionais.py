[1,2,3,True,"Texto"]
vazia = []
aprovados =  ["Graziela Barroso", "Juliano Moreira", "André Rebouças",
    "César Lattes", "Enedina Alves", "Machado de Assis",
    "Ayrton Senna", "Luiz Gama", "Ruth de Souza",
    "Nise da Silveira", "Johanna Döbereiner", "Carolina de Jesus",
    "Leopoldo Nachbin", "Antonieta de Barros", "Lima Barreto"
]
aprovados[0]
print("Lista de aprovados : ", aprovados)
print("Primeira(o) colocada(o): ",aprovados[0],".")

# 1. Quantidade total de aprovados
# len retorna um inteiro com o tamanho da lista
print("Total de aprovados: ", len(aprovados))

# 2. Primeira pessoa na condição de reserva
# Considerando que há 5 vagas
print("Primeiro candidato reserva:", aprovados[5])

# 3. Verificar se alguém está na lista
if "Oswaldo Cruz" in aprovados:
    print("Parabéns, Oswaldo Cruz!")
else:
    print("Uma pena, não foi dessa vez Oswaldo Cruz.")
    
# 4. Lista de classificados
#Considerando que há 5 vagas
classificados = aprovados[0:5]
print("Lista de classificados: ", classificados)
print("Último classificado: ", classificados[-1])

#tentar com o len

# 5. Lista de reservas
reservas = aprovados[5:len(aprovados)]
print("Lista de reservas: ", reservas)
print("Último reserva: ", reservas[-1])

# 6 Modificar o elemento em uma determinada posiçao
aprovados[5] = "Oswaldo Cruz"
if "Oswaldo Cruz" in aprovados:
    print("Parabéns, Oswaldo Cruz!")
else:
    print("Uma pena, não foi dessa vez Oswaldo Cruz.")
    

# 7 adicionar um elemento ao final da lista
aprovados.append("Rafaela Ventura")

# 8 Remover um elemento da 
aprovados.remove("Oswaldo Cruz")
print("Nova lista de aprovados: ", aprovados)
