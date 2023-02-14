class Helicopter:
	def __init__(self, name:str, max_speed: float):
		"""
		Создание и подготовка к работе объекта "Вертолёт"
		"""
		self.name = name
		self.max_speed = max_speed
		self._crew = 0 #число членов команды ставим ноль и применяем инкапсуляцию, чтобы пользователь не мог напрямую поменять значение, а воспользовался специальной функцией

	def __str__(self) -> str:
		"""
		Магический метод, отображающий наименование класса и название объекта, наследуется
		"""
		return f"{self.__class__.__name__} {self.name!r}"

	def __repr__(self) -> str:
		"""
		Магический метод, выводящий всю информацию об объекте, перегружается
		"""
		return f"{self.__class__.__name__} (name = {self.name!r}, max_speed = {self.max_speed!r})"

	def set_crew(self, crew: int):
		"""
		Метод, позволяющий загрузий в вертолёт команду(спасатели, десант), наследуется
		"""
		if not isinstance(crew, int):
			raise ValueError("Ошибка, значение не int")
		if crew < 0:
			raise ValueError("Ошибка, значение не может быть отрицательно")
		self._crew = crew

	def show_crew(self):
		"""
		Метод, показывающий, сколько членов команды в вертолёте, наследуется
		"""
		return self._crew

	def if_can_land_crew(self) -> bool:
		"""
		Метод, проверяющий, может ли вертолёт высадить указанное число членов команды в СТАНДАРТНЫХ условиях, перегружается
		:param self._crew: число членов команды
		:return: Может ли высадить команду
		"""

class Military_Helicopter(Helicopter):
	def __init__(self, guns: str):
		"""
		Создание и подготовка к работе объекта "Многоцелевой военный вертолёт"
		"""
		super().__init__(name, max_speed) #наследование конструктора базового класса
		self.guns = guns #задаём вооружение вертолёта

	def __repr__(self) -> str:
		"""
		Перегрузка метода __repr__
		"""
		return f"{self.__class__.__name__} (name = {self.name!r}, max_speed = {self.max_speed!r}, guns = {self.guns!r})"
	def if_can_land_crew(self) -> bool:
		"""
		Метод, проверяющий, может ли вертолёт высадить указанное число членов команды в БОЕВЫХ условиях, перегружается
		:param self._crew: число членов команды
		:return: Может ли высадить команду
		"""
	
