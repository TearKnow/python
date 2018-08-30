def calc(number):
	sum = 0
	for n in number:
		sum = sum + n
	return sum
r = calc([1, 2, 4])
print(r)

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

#可变参数
def calc_b(*number):
	sum = 0
	for n in number:
		sum = sum + n
	return sum
r = calc_b(1, 2, 4)
print(r)
r1 = calc_b(1, 2, 4)
print(r1)


nums = [1, 2, 4]
r3 = calc_b(*nums)
print(r3)


#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
person('jack', '28', city='shanghai', region='jinshan')
pDict = {'city':'sh', 'region':'js'}
person('alice', '28', **pDict)


#如果要限制关键字参数的名字，就可以用命名关键字参数
#限制关键字参数的名字
def person2(name, age, *, city):
	print('name:', name, 'city:', city)

person2('me', 11, city='shjs')



