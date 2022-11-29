def solution(n):
    n1, n2 = 1, 2
    if n == 1:
        return 1
    for i in range(2,n):
        n1, n2 = n2, n1+n2
    return n2 % 1234567