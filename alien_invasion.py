
import sys
import pygame
from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien


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
		self.aliens = pygame.sprite.Group()
		self._create_fleet()

	def run_game(self):
		"""Запуск основного цикла игры."""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_aliens()
			self._update_screen()

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

	def _create_fleet(self):
		"""Создание флота вторжения."""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		"""Определяет количество рядов, помещающихся на экране."""
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height -
							(3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _create_alien(self, alien_number, row_number):
		# Создание пришельца и размещение его в ряду.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""Реагирует на достижение пришельцем края экрана."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Опускает флот и меняет направление флота."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_bullets(self):
		"""Обновляет позиции снарядов, и уничтожает старые снаряды."""
		# Обновление позиции снарядов.
		self.bullets.update()

		# Удаляет снаряды вышедшие за грань экрана
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		# Проверка попаданий в пришельцев.
		# При обнаружении попадания удалить снаряд и пришельца.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)


	def _update_aliens(self):
		"""
		Проверяет, достиг ли флот края экрана.
		с последующим обновлением позиций всех пришельцев флота.
		"""
		self._check_fleet_edges()
		self.aliens.update()

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		# При каждом проходе цикла перерисовывается экран.
		self.screen.blit(self.bg, (0, 0))
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
		# Отображение последнего прорисованного экрана.
		pygame.display.flip()

			
if __name__ == '__main__':
	# Создание экземпляра и запуск игры.
	ai = AlienInvasion()
	ai.run_game()
