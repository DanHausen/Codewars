def order(sentence):    
    dict = {}
    list = []
    sentenceSplit = sentence.split(" ")
    
    for i in sentenceSplit:
        for c in i:
            uniCode = ord(c)
            if uniCode >= ord("0") and uniCode <= ord("9"):
                dict[c] = sentenceSplit.index(i)
                list.append(uniCode - ord("0"))
                break
    list.sort()
    
    res = []
    for i in list:
        res.append(sentenceSplit[dict[str(i)]])
    return " ".join(i for i in res)
    
#Smart practices:
# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
  
# def extract_number(word):
#     for l in word: 
#         if l.isdigit(): return int(l)
#     return None
# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=extract_number))