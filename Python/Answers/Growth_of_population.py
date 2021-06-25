def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 = p0 + p0 * (percent/100) + aug
        years += 1
    return years
    
#Smart practices:
# def nb_year(p0, percent, aug, p, years = 0):
#     if p0 < p:
#         return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
#     return years