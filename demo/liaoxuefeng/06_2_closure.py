#闭包
def createCounter():
	i = 0
	def counter():
		nonlocal i
		i = i + 1
		return i
	return counter

b = createCounter()
print(b(), b(), b(), b())


bb = createCounter()
print(bb(), bb(), bb(), bb(), bb())

