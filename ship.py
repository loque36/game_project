
import pygame


class Ship:
	"""Класс управления кораблем."""

	def __init__(self, ab_game):
		"""Инициализирует корабль и задаёт его начальную позицию"""
		self.screen = ab_game.screen
		self.settings = ab_game.settings
		self.screen_rect = ab_game.screen.get_rect()
		# Загружает изображение корабля и получает прямоугольник
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		# Каждый новый корабль появляется у нижнего края экрана.
		self.rect.midbottom = self.screen_rect.midbottom
		#Сохранение вещественно координаты центра корабля
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		#Флаги перемещения
		self.moving_right = False
		self.moving_left = False
		self.moving_forward = False
		self.moving_backward = False

	def update(self):
		#Обновляет позицию корабля с учетом флагов
		#Обновялется атрибут x, не rect
		if self.moving_right:
			self.x += self.settings.ship_speed
		if self.moving_left:
			self.x -= self.settings.ship_speed
		if self.moving_forward:
			self.y -= self.settings.ship_speed
		if self.moving_backward:
			self.y += self.settings.ship_speed

		# Обновление атрибута rect на основании self.x
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Рисует корабль в текущей позиции."""
		self.screen.blit(self.image, self.rect)
