#https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python
# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

# Example:
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'
# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'
# namelist([])
# # returns ''
# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

def namelist(names):
    str = ''
    if len(names) != 0:
        array = []
        for i in range(0,len(names) -1):
            array.append(names[i]['name'])
        str = ', '.join(array)
        str += ' & ' + names[-1]['name'] if str != '' else names[-1]['name']
    return str
    
#BEST PRACTICES:

# def namelist(names):
#     if len(names) > 1:
#         return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
#                                 names[-1]['name'])
#     elif names:
#         return names[0]['name']
#     else:
#         return ''
        
        
# def namelist(names):
#   return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]