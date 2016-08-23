import re

var1 = "Similiarly"

def encrypt_caesar(plaintext):
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = dict(zip(s, s[3 :] + s[:3]))

    print(d.values())
    # return ''.join( map(lambda l: d.get(l,l ) ,plaintext.lower() ) )
    return d



if __name__ == '__main__':
    encrypt_caesar('AAAAAAAA BBBBBBBB' )