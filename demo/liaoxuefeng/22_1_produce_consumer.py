import random,time

def consumer():
	r = ''
	while True:
		#time.sleep(random.randint(1,2))##########################不行 不能交叉显示
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
		#time.sleep(random.randint(1,2))##########################不行 不能交叉显示
		#一旦生产了东西，通过c.send(n)切换到consumer执行
		r = c.send(n)
		print('[producer] consumer return: %s' % r)
	c.close()
	
c = consumer()
produce(c)


