from random import randint
class Die():
	def __init__(self, sides):
		self.sides = sides
		
	def roll_die(self):
		value = randint(1, self.sides)
		print(value)
		
die1 = Die(6)
die2 = Die(sides = 10)

die1.roll_die()
die2.roll_die()
