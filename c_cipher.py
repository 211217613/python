message = "This is my secret messagd."
print message

key = input('Input the key: ')
mode = 'encrypt'
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipherText = ''
message = message.upper()
counter = 0

#run encryption decreyption on code on each symbol
for symbol in message:
	if symbol in LETTERS:
		counter = counter + 1
		num = LETTERS.find(symbol) #
		# print "num: " , num
		if mode == 'encrypt':
			num = num + key
		if mode == 'decrypt':
			num = num - key
		if num >= len(LETTERS):
			num = num - len(LETTERS)
		elif num < 0 :
			num = num + len(LETTERS)
		cipherText = cipherText + LETTERS[num]

	else:
		cipherText = cipherText + symbol
print cipherText