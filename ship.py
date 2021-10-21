
import pygame


class Ship:
	"""Класс управления кораблем."""

	def __init__(self, ab_game):
		"""Инициализирует корабль и задаёт его начальную позицию"""
		self.screen = ab_game.screen.get_rect()
		# Загружает изображение корабля и получает прямоугольник
		self.image = pygame.image.load(images/ship.bmp)
		self.rect = self.image.get_rect()
		# Каждый новый корабль появляется у нижнего края экрана.
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""Рисует корабль в текущей позиции."""
		self.screenblit(self.image, self.rect)
