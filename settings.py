
class Setting:
	"""Класс для хранения всех настроек игры."""

	def __init__(self):
		"""Инициализирует настройки игры."""
		# Параметры экрана
		self.screen_width = 1280
		self.screen_height = 720
		self.bg_color = (80, 230, 200)

		# Настройки корбаля
		self.ship_speed = 20

		# Параметры снаряда
		self.bullet_speed = 50
		self.bullet_width = 4
		self.bullet_height = 25
		self.bullet_color = (80, 190, 230)
		self.bullet_allowed = 3

		# Настройки пришельцев
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# fleet_direction = 1 обозначает движение вправо, а -1 - влево.
		self.fleet_direction = 1