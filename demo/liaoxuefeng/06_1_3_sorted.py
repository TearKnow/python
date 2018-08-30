#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
l = sorted([36, 5, -12, 9, -21], key=abs)
print(l)


def by_name(t):
	return t[0]
def by_value(t):
	return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
sortByKey = sorted(L, key=by_name)
print(sortByKey)


sortByValue = sorted(L, key=by_value)
print(sortByValue)
