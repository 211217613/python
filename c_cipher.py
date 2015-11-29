message = "This is my secret messagd."
print message

key = input('Input the key: ')
mode = 'encrypt'
LETTERS = "0123456789BCDEFGHIJKLMNOPQRSTUVWXYZ"
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
		# if mode == 'decrypt':
		else:
			num = num - key

		#Handles overflow/underflow	
		if num >= len(LETTERS):
			num = num - len(LETTERS)
		else:
			if num < 0 :
				num = num + len(LETTERS)
		cipherText = cipherText + LETTERS[num]

	else:
		cipherText = cipherText + symbol
print cipherText