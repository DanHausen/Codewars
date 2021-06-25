def persistence(n):
    res = [int(x) for x in str(n)]
    times = 0
    number = 1
    while len(res) > 1:
        for i in res:
            number *= i
        res.clear()
        res = [int(x) for x in str(number)]
        number = 1 
        times+=1
        print(times)
    return times
    
persistence(39)

# Smart practices:
# import operator
# def persistence(n):
#     i = 0
#     while n>=10:
#         n=reduce(operator.mul,[int(x) for x in str(n)],1)
#         i+=1
#     return i

# persistence = lambda n,c=0: persistence(reduce(lambda x,y:int(x)*int(y),str(n)),c+1) if n >=10 else c