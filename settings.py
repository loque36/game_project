
class Setting():
	"""Класс для хранения всех настроек игры"""

	def __init__(self):
		"""Инициализирует настройки игрыю"""
		# Параметры экрана
		self.screen_width = 1280
		self.screen_height = 720
		self.bg_color = (80,230,200)

		#Настройки корбаля
		self.ship_speed = 1.5