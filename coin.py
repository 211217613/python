import random

# The coin class simulates  a coin toss
#

class Coin():
	def __init__(self):
		self.__sideup = 'Heads'
		self.upside = 'Heads'

	# Toss method generates a pseudo random number

	def toss(self):
		if random.randint(0,1) == 0:
			self.__sideup = 'Heads'
		else:
			self.__sideup = 'Tails'
	@property
	def get_sideup(self):
		return self.__sideup
