# Quantos anos voce tem?
# Idade:
# Se idade < 16:
#- Voce nao pode votar!

idade = int(input("Quantos anos você tem?\n"))
if idade < 16:
	print("Você não pode votar!")

elif idade < 18:	
	print("Voto facultativo!")

elif idade < 66:
	print("Você é obrigado a votar!")

else:
	print("Voto facultativo!")

print("FIM")
