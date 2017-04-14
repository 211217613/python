"""Greatest common divisor is implemented with the following
if x % y == 0
    return y
else 
"""

def main():
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter an integer: '))

    print('The greatest common divisor is {}'.format(gcd(num1, num2)))

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)

if __name__ == '__main__':
    main()
