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
    
# Smart practices:
# def tribonacci(signature, n):
#     res = signature[:n]
#     for i in range(n - 3): res.append(sum(res[-3:]))
#     return res
  
# def tribonacci(signature,n):
#     return signature[:n] if n<=len(signature) else tribonacci(signature + [sum(signature[-3:])],n)