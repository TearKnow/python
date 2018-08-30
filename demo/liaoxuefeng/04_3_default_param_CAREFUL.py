def add_end(L=[]):
	L.append('END');
	return L

a = add_end([1, 3, 4])
print(a)
b = add_end([1, 3, 4])
print(b)


c = add_end()
print(c)
d = add_end()
print(d)
dd = add_end([55])
#print(dd)
e = add_end()
print(e)
# 定义默认参数要牢记一点：默认参数必须指向不变对象！,[]是一个变量
