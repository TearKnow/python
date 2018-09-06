#装饰器
#求质数

import time

def display_time(func):
	def wrap():
		t1 = time.time()
		func()
		t2 = time.time()
		print("Total times: %.4fs" % (t2 - t1))#old
		print("Total times: {:.4}s" . format(t2 - t1))#new
	return wrap

def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	else:
		for i in range(2, n):
			if n % i == 0:
				return False
		return True

@display_time
def prime_nums():
	for i in range(2, 500):
		if is_prime(i):
			print(i)


prime_nums()


print('-----------------formmat usage -----------------')
name = 'jack'
age = 18
print("My name is {}, I am {} years old".format(name, age))
