#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(num):
	n, a, b = 0, 0 , 1
	while n < num:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

b = fib(9)

for i in b:
	print(i)	

