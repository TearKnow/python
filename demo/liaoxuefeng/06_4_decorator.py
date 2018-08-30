
def log(func):
	def wrapper(*args, **kw):
		print('class function')
		return func(*args, **kw)
	return wrapper


@log
def now():
	print('2018-08-22')

now()
