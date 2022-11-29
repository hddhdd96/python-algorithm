def solution(n):
    answer = []
    for i in range(n+1):
        if i == 0 or i == 1:
            answer.append(i)
        else:
            t = answer[i-1] + answer[i-2]
            answer.append(t)
    return answer[-1] % 1234567