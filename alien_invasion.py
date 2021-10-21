
import sys

import pygame

from settings import Setting

class AquaBlow:
	"""Класс для управления ресурсами и поведением игры."""

	def __init__(self):
		"""Инициализирует игру и создает игровые ресурсы."""
		pygame.init()

		self.settings = Setting()
		self.bg = pygame.image.load('images/bgr.bmp')

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("AquaBlow")

	def run_game(self):
		"""Запуск основного цикла игры."""
		while True:
			#Отслеживание событий клавиатуры и мыши.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			# При каждом проходе цикла перерисовывается экран.
			self.screen.fill(self.settings.bg_color)
			self.screen.blit(self.bg, (0, 0))
			# Отображение последнего прорисованного экрана.
			pygame.display.flip()
			
if __name__ == '__main__':
	# Создание экземпляра и запуск игры.
	ai = AquaBlow()
	ai.run_game()