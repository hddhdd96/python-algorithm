def solution(n):
    answer = 1
    for i in range(1, n//2 + 1):
        t = i
        while t < n:
            i+=1
            t += i
            if t == n:
                answer+=1
    return answer