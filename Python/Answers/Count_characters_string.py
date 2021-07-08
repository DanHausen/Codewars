#The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

#What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    list = {}
    for i in string:
        if i not in list:
            list[i] = string.count(i)
    return list;
    
#BEST PRACTICES:
# from collections import Counter
# def count(string):
#     return Counter(string)
    
    
# def count(string):  
#     return {i: string.count(i) for i in string}
    
    
# def count(s):
#     return {x:s.count(x) for x in set(s)}