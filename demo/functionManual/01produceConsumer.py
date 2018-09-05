import random,time

def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		
		print('[consumer] Consuming %s...' % n)
		r = '200 OK'
		
def produce(c):
	#调用c.send(None)启动生成器
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[producer] producing %s...' % n)
		#一旦生产了东西，通过c.send(n)切换到consumer执行
		r = c.send(n)
		print('[producer] consumer return: %s' % r)
	c.close()
	
c = consumer()
produce(c)


############################## 一些预备知识 ###################$$$
b = ''
if not b:
	#if b is empty, go to here
	print('is empty')
	print('-------------------------------------')
	
def odd():
	print('step 1')
	yield 'one'#返回这个值
	print('step 2')
	yield 'two'
	
o = odd()
x1 = next(o)
print(x1)
x2 = next(o)
print(x2)







