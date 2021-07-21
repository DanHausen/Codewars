#https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"


def to_camel_case(text):
    if text == '':
        return ''
    else:
        l = list(text)
        f = ''
        for i in range(len(l)-1):
               if l[i] == '-' or l[i] == '_':
                    l[i+1] = l[i+1].upper()
        for j in l:
            if j != '_' and j != '-':
                f += j
        return f
    
#BEST PRACTICES:
# def to_camel_case(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s


# from re import compile as reCompile
# PATTERN = reCompile(r'(?i)[-_]([a-z])')
# def to_camel_case(text):
#     return PATTERN.sub(lambda m: m.group(1).upper(), text)


# def to_camel_case(text):
#     return "".join([i if n==0 else i.capitalize() for n,i in enumerate(text.replace("-","_").split("_"))])