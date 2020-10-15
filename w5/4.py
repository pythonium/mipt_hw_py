class Shape():
	def __init__(self, height, length):
		self.height = height
		self.length = length

	def get_area(self):
		raise NotImplementedError()

class Triangle(Shape):

	def get_area(self):
		area = (self.height * self.length)/2
		return area

class Rectangle(Shape):

	def get_area(self):
		area = self.height * self.length
		return area


t = Triangle(3, 4)
print(t.get_area())

r = Rectangle(3, 4)
print(r.get_area())
