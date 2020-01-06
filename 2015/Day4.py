import hashlib as hl
AoCInput = "ckczppom"

i = 1
while i > 0:
    temp = AoCInput + str(i)
    temp = hl.md5(temp.encode()).hexdigest()
    # if str(temp[:5]) == '00000': # Part I 
    if str(temp[:6]) == '000000':   # Part II
        print(i)
        break
    i += 1
        