from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar'))

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

