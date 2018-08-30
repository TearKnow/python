#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
	return x * x

f = map(f, [1, 2, 4, 5, 6])
for i in f:
	print(i)




#reduce
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def jiechen(a, b):
	return a * b

result = reduce(jiechen, [1, 2, 3, 4, 5, 6])
print(result)

