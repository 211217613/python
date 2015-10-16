key = 25
MAX = 26 # wrap around 

string = 'cryptoisfun'
c_text = []
cipher = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4}

for x in string:
    temp = key + ord(x)
    if temp > 26:
        temp = 1 + ord(x) 
    c_text.append(temp)
    print ord(x)

print c_text

for x in c_text:
    pass
    

    
