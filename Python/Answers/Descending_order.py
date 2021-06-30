#https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def descending_order(num):
    numList = [int(i) for i in str(num)]
    numList = sorted(numList, reverse = True)
    s = ''.join(map(str,numList))
    return int(s)
 
#Smart practices:   
# def Descending_Order(num):
#     return int("".join(sorted(str(num), reverse=True)))

#Descending_Order = lambda n: int(''.join(reversed(sorted(str(n)))))