def persistence(n):
    res = [int(x) for x in str(n)]
    times = 0
    number = 1
    while len(res) > 1:
        for i in res:
            number *= i
            print(number)            
        res.clear()
        res.append(number) 
        times+=1
    return times
    
#Está dando erro pois ao limpar o 'res', o apend adiciona o numero por completo e não cada digito. E já que é um array, seu tamanho será 1, então o while é finalizado
    
persistence(39)