def tribonacci(signature, n):
    index = 0
    if n < 1:
        return []
    if n < len(signature):
        return signature[0:n]
    seq = signature[:]
    while index < n:
        add = sum(seq[index:index+3])
        seq.append(add)
        index+=1
    return seq[0:n]