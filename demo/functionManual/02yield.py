def gen():
	for i in range(5):
		yield i

a = gen();
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
