def tribonacci(signature, n):
    list = []
    index = 0
    for i in signature:
        if len(list) >= 3:
            sum = list[i] + list[i-1] + list[i-2]
            list.append(sum)
        else:
            list.append(i)
        index += 1
    return list