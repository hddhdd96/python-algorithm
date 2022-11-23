def solution(n):
    nbin = bin(n)[2:]
    nbinCount = nbin.count('1')
    while True:
        n += 1
        if nbinCount == bin(n)[2:].count('1'):
            return n