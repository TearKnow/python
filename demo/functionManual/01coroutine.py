import time

def A():
	while True:
		print('a')
		yield
		print('sleep 1')
		time.sleep(1)

def B(c):
	while True:
		print('b')
		c.__next__()
		print('sleep 2')
		time.sleep(2)

if __name__ == '__main__':
	a = A() 
	B(a)

#https://www.youtube.com/watch?v=fVtw3isaAus
# b a 2 b 1 a 2 b 1 a
#因为是死循环，所以2之后肯定是b，1之后是a，连起来就是 2 b 1 a
