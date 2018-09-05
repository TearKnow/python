# https://blog.csdn.net/qq_27825451/article/details/78847473
# yield from  generator 。实际上就是返回另外一个生成器
# yield from iterable本质上等于 for item in iterable: yield item的缩写版
# yield from 后面可以跟的式子有“ 生成器  元组 列表等可迭代对象以及range（）函数产生的序列
def gen2():
	yield from ['a','b','c']

for i in gen2():
	print(i)
