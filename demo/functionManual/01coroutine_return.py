import time

def A():
	while True:
		print('A()')
		yield 11111111
		time.sleep(1)

def B(c):
	c.send(None)
	while True:
		print('B()')
		r = c.send('bb')
		print(r)
		time.sleep(2)


a = A() 
B(a)

# yield 的那个值就是返回的参数
# c.send()  和 c.__next()__ 有点类似
