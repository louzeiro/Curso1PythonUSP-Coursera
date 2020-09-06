
def entrada():
	print("Bem-vindo ao jogo do NIM! Escolha:")
	print("1 - para jogar uma partida isolada")
	opcao = int(input("2 - para jogar um campeonato\n"))
	return opcao


def main():
	opcao = entrada()	
	if (opcao == 1 or opcao == 2):
		if(opcao==1):
			print("Você escolheu partida isolada")
			partida()
		else:
			print("Vocẽ escolheu um campeonato")
			campeonato()
	else:
		print("Escolha uma opcao valida")
		opcao = entrada()


def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))

	#definindo quem começa
	if (n%(m+1)==0):
		print("Você começa!")
		vez_computador = False
	else:
		print("Computador começa")
		vez_computador = True

	while(n>0): #enquanto houver peças no tabuleiro
		if (vez_computador): 
			jogada = computador_escolhe_jogada(n,m)
			print("Computador retirou ", jogada, "peças")
			vez_computador = False
		else:
			jogada = usuario_escolhe_jogada(n,m)
			print("Você retirou ", jogada, "peças")
			vez_computador = True

		n=n-jogada
		print("Restam apenas ", n, "peças no tabuleiro" )
	if(vez_computador):
		print("Você ganhou!")
		return 1
	else:
		print("O computador ganhou")
		return 0

def usuario_escolhe_jogada(n,m):
	testeEntrada = True
	while(testeEntrada): #só vale tirar menor ou igual a m
		pecas = int(input("Quantas peças você vai tirar? "))
		if (pecas>m or pecas<1):
			testeEntrada = True
		else:
			testeEntrada = False
	
	return pecas

def computador_escolhe_jogada(n,m):
	if(n<=m):
		return n
	else:
		aux = n%(m+1)
		if(aux>0): # se não for multiplo e esta sobrando mais que m, tira o resto
			return aux
	return m
			
		


def campeonato():
	pontosComputador=0
	pontosUsuario=0
	for i in range(3):
		print("**** Rodada ", i+1, " *****")
		vencedor = partida()
		if (vencedor):
			pontosUsuario+=1
		else:
			pontosComputador+=1

	print("Placar final: Voce ", pontosUsuario,"x",pontosComputador,"Computador")

