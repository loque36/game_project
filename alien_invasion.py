
import sys
import pygame
from settings import Setting
from ship import Ship
from bullet import Bullet


class AlienInvasion:
	"""Класс для управления ресурсами и поведением игры."""

	def __init__(self):
		"""Инициализирует игру и создает игровые ресурсы."""
		pygame.init()

		self.settings = Setting()
		self.bg = pygame.image.load('images/bgr.png')

		# self.screen = pygame.display.set_mode(
		# 	(self.settings.screen_width, self.settings.screen_height))
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""Запуск основного цикла игры."""
		while True:
			self._check_events()
			self.ship.update()
			self.bullets.update()
			self._update_screen()

			# Удаляет снаряды вышедшие за грань экрана
			for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)

	def _check_events(self):
		"""Реагирует на нажатия клавиатуры и мыши."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		# Отслеживание нажатий клавиатуры и мыши.
		if event.key == pygame.K_RIGHT:
			# Переместить корабль вправо
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# Переместить корабль влево
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			# Переместить корабль вверх
			self.ship.moving_forward = True
		elif event.key == pygame.K_DOWN:
			# Переместить корабль вниз
			self.ship.moving_backward = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		# Отслеживание отпускания клавиатуры и мыши.
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_forward = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_backward = False

	def _fire_bullet(self):
		"""Создание нового снаряда и включение его в группу bullets."""
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		# При каждом проходе цикла перерисовывается экран.
		self.screen.blit(self.bg, (0, 0))
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# Отображение последнего прорисованного экрана.
		pygame.display.flip()

			
if __name__ == '__main__':
	# Создание экземпляра и запуск игры.
	ai = AlienInvasion()
	ai.run_game()
