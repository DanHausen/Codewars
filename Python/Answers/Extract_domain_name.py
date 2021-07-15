#https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

#np
def domain_name(url):
    listUrl = []
    bool = False
    str = ''
    for i in url:
        if bool == True:
            if i == '.':
                break
            listUrl.append(i)
        if i == '.' or i == '/':
            bool = True
    if listUrl[0] == '/':
        del listUrl[0]
    for i in listUrl:
        str += i
    return str
    
##BEST PRACTICES:
# def domain_name(url):
#     return url.split("//")[-1].split("www.")[-1].split(".")[0]
    
# import re
# def domain_name(url):
#     return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
    
# def domain_name(url):
#     url = url.replace('www.','')
#     url = url.replace('https://','')
#     url = url.replace('http://','')
    
#     return url[0:url.find('.')]
    
# def domain_name(url):
#     return url.split("://")[-1].split(".")[-2]
    
# def domain_name(url):
#     url = url.split('//')[-1]
#     url = url.split('/')[0]
#     url = url.split('.')[-2]
#     return url

