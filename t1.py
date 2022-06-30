class Car:
	def __init__(self, name, manufacturer, year):
		self.name = name
		self.manufacturer = manufacturer
		self.year = year


	def __repr__(self):
		return f"repr: {self.name}->{self.manufacturer}->{self.year}"

	def __str__(self):
		return f"str: {self.name}->{self.manufacturer}->{self.year}"


if __name__ == '__main__':
	car1 = Car("Camry", "Toyota", "2022")
	print(car1)
