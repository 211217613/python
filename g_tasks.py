import re
from oauth2client.contrib import gce


# class Point(object):
# 	def __init__(self, x = 0, y = 0):
# 		self.x = x
# 		self.y = y

# 	def __add__(self, other):
# 		return Point(self.x + other.x, self.y + other.y) 

# 	def __str__(self):
# 		return "Point {0}, {1}".format(self.x, self.y)

# 	def rotate_90_CC(self):
# 		self.x, self.y  = -self.y, self.x



def main():
	# pt1 = Point(3,4)
	# pt2 = Point()
	# pt1.rotate_90_CC()
	# print(pt1)
	# print(pt2)
	string = "My 2 favorite numbers are 21 and 12"
	x = re.findall('[0-9].', string)
	for _ in x:
		x = _.rstrip()
	y = "".join(x)
	print(x)
	print(y)

main()