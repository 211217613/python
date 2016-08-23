def gcdd(a, b):
	if a > b:
		print("a must be less than b")
	for x in range(b + 1):
		if x % a == 0:
			print(x)

if __name__ == '__main__':
	gcdd(10 , 25)