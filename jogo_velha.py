import pygame

pygame.init()

comprimento = 600
altura = 600

tela = pygame.display.set_mode( ( comprimento, altura ) )
tabuleiro = [ ["v", "v", "v"], ["v", "v", "v"], ["v", "v", "v"] ]
simbolo = "X"
pos_x, pos_y = 0, 0

def desenhar_simbolos( tela, simbolo, x, y, tabuleiro ):
	for campo in range( len( tabuleiro ) ):
		for item in range( len( tabuleiro[0] ) ):
			if tabuleiro[campo][item] != "v":
				if tabuleiro[campo][item] == "O":
					pygame.draw.circle( tela, ( 255, 255, 255 ), ( item * 200 + 100, campo * 200 + 100 ), 50, 5 )
				elif tabuleiro[campo][item] == "X":
					pygame.draw.line( tela, ( 255, 255, 255 ), ( item * 200 + 50, campo * 200 + 50 ), ( item * 200 + 150, campo * 200 + 150 ), 5 )
					pygame.draw.line( tela, ( 255, 255, 255 ), ( item * 200 + 150, campo * 200 + 50 ), ( item * 200 + 50, campo * 200 + 150 ), 5 )

def alterar_tabuleiro( tabuleiro, x, y, simbolo ):
	#Se clicou em um espaço vazio, coloca o simbolo do jogador e alterna o simbolo
	if tabuleiro[y][x] == "v":
		tabuleiro[y][x] = simbolo
		if simbolo == "O":
			simbolo = "X"
		else:
			simbolo = "O"
	return tabuleiro, simbolo

def mostrar_tabuleiro( tabuleiro ):
	for item in tabuleiro:
		print( item )
	print()

def verificar_vitoria( tabuleiro ):
	for campo in tabuleiro:
		horizontal = campo[0]
		c = 0
		for item in campo:
			if item != "v":
				if horizontal == item:
					c += 1
		if c == 3:
			print( horizontal, "ganhou" )
			return horizontal


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			# Pega posição do mouse e armazena em mouse_pos
			mouse_pos = pygame.mouse.get_pos()

			pos_x = mouse_pos[0] // 200
			pos_y = mouse_pos[1] // 200

			tabuleiro, simbolo = alterar_tabuleiro( tabuleiro, pos_x, pos_y, simbolo )
	
	desenhar_simbolos( tela, simbolo, pos_x, pos_y, tabuleiro )
	#mostrar_tabuleiro( tabuleiro )		
	verificar_vitoria( tabuleiro )
	
	# Desenhar linha. Argumentos ( Onde você quer desenhar, cor, ponto inicial, ponto final )		
	pygame.draw.line( tela, ( 250, 250, 250 ), ( 200, 0 ), ( 200, altura ) )		
	pygame.draw.line( tela, ( 250, 250, 250 ), ( 400, 0 ), ( 400, altura ) )
	pygame.draw.line( tela, ( 250, 250, 250 ), ( 0, 200 ), ( comprimento, 200 ) )
	pygame.draw.line( tela, ( 250, 250, 250 ), ( 0, 400 ), ( comprimento, 400 ) )

	pygame.display.update()		
