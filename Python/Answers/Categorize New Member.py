def open_or_senior(data):
    listResult = []
    for i in data:
        listResult.append("Senior" if i[0] >= 55 and i[1] > 7 else "Open")
    return listResult
    
#Smart practices:
# def openOrSenior(data):
#   return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]