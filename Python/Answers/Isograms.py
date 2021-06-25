def is_isogram(string):
    upperCaseString = string.upper()
    for i in upperCaseString:
        spaces = " "
        slashes = "-"
        if upperCaseString.count(i) > 1:
            return False        
        elif string.count(spaces) > 1 or string.count(slashes) > 1:
            return False        
        else:
            pass        
    return True
    
# Smart practices:  
# def is_isogram(string):
#     return len(string) == len(set(string.lower()))
#
# def is_isogram(string):
#     string = string.lower()
#     for letter in string:
#         if string.count(letter) > 1: return False
#     return True