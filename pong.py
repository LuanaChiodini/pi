import pygame
import numpy as np

pygame.init()
pygame.font.init()

tamanho = comprimento_tela, altura_tela = 1000, 600
tela = pygame.display.set_mode(tamanho)
fonte = pygame.font.SysFont("ubuntu", 72)

comprimento = 100
largura = 20

class Jogador():
	def __init__(self, jogador_num, comeco_x, comeco_y):
		self.num = jogador_num
		self.x = comeco_x
		self.y = comeco_y
		self.velocidade = 2
		self.pontos = 0
		self.pontos_texto = fonte.render(str(self.pontos), False, (255, 255, 255))

	def mover(self, direcao, y_tela):
		if direcao == "pra_cima":
			if self.y - self.velocidade >= 0:
				self.y -= self.velocidade
		else:
			if self.y + comprimento + self.velocidade <= y_tela:
				self.y += self.velocidade

	def marcar_ponto(self):
		self.pontos += 1
		self.pontos_texto = fonte.render(str(self.pontos), False, (255, 255, 255))

class Bola():
	def __init__(self, comeco_x, comeco_y):
		self.x = comeco_x
		self.y = comeco_y
		self.tamanho = 10
		self.velocidade_x = -2
		self.velocidade_y = -2

	def mover(self, x_tela, y_tela):
		if self.x + self.velocidade_x + self.tamanho > x_tela:
			jogador1.marcar_ponto()
			self.reiniciar_posicao("esquerda")

		elif self.x < 0:
			jogador2.marcar_ponto()
			self.reiniciar_posicao("direita")

		if self.checar_colisao_y(y_tela):
			self.velocidade_y *= -1

		self.x += self.velocidade_x
		self.y -= self.velocidade_y

	def checar_colisao_x(self, x_tela):
		if self.x + self.velocidade_x + self.tamanho >= x_tela or self.x <= 0:
			return True
		return False

	def checar_colisao_y(self, y_tela):
		if self.y + self.tamanho >= y_tela or self.y <= 0:
			return True
		return False

	def checar_colisao_barra(self, jogador):
		if jogador.num == 1:
			if self.x == jogador.x + largura and self.y in np.arange(jogador.y, jogador.y + comprimento + 1):
				self.velocidade_x *= -1

		elif jogador.num == 2:
			if self.x in np.arange(jogador.x, jogador.x + self.velocidade_x + 1) and self.y in np.arange(jogador.y, jogador.y + comprimento + 1):
				self.velocidade_x *= -1

	def reiniciar_posicao(self, direcao):
		if direcao == "direita":
			self.velocidade_x = 2
			self.velocidade_y = 2
		else:
			self.velocidade_x = -2
			self.velocidade_y = -2
		self.x = comprimento_tela / 2
		self.y = altura_tela / 2

jogador1 = Jogador(1, 10, altura_tela / 2 - comprimento / 2)
jogador2 = Jogador(2, comprimento_tela - 10 - largura, altura_tela / 2 - comprimento / 2)

bola = Bola(comprimento_tela / 2, altura_tela / 2)

while True:
	tela.fill((0, 0, 0))

	teclas = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	if teclas[pygame.K_w]:
		jogador1.mover("pra_cima", altura_tela)
	if teclas[pygame.K_s]:
		jogador1.mover("pra_baixo", altura_tela)

	if teclas[pygame.K_UP]:
		jogador2.mover("pra_cima", altura_tela)
	if teclas[pygame.K_DOWN]:
		jogador2.mover("pra_baixo", altura_tela)

	pygame.draw.rect(tela, (255, 255, 255), (jogador1.x, jogador1.y, largura, comprimento))
	pygame.draw.rect(tela, (255, 255, 255), (jogador2.x, jogador2.y, largura, comprimento))

	bola.mover(comprimento_tela, altura_tela)

	bola.checar_colisao_barra(jogador1)
	bola.checar_colisao_barra(jogador2)

	pygame.draw.rect(tela, (255, 255, 255), (bola.x, bola.y, bola.tamanho, bola.tamanho))

	tela.blit(jogador1.pontos_texto, (comprimento_tela / 2 - 100, 50))
	tela.blit(jogador2.pontos_texto, (comprimento_tela / 2 + 100, 50))

	pygame.display.flip()