class Model(dict): #change to object, can print(self)
	def func(self):
		self.name = 'this is name'
		print(self)
		
obj = Model()
obj.func()