class Student(object):
	name = 'class attr'
	
obj = Student()
print(obj.name)
print(Student.name)
obj.name = 'obj attr'
print(obj.name)
del obj.name
print(obj.name)