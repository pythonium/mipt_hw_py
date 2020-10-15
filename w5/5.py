class Mother:
	def __init__(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def __str__(self):
		return "Name: {}".format(self.get_name())




class Daughter(Mother):
	def __init__(self, name, mother):
		super().__init__(name)
		self.__mother = mother

	def get_mother(self):
		return self.__mother

	def __str__(self):
		return "Name: {}, Mother: {}".format(self.get_name(), self.get_mother())

Helen = Mother("Helen")
Nancy = Daughter("Nancy", "Helen")

print(Helen)
print(Nancy)
