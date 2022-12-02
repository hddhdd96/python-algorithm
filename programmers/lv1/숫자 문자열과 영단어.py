def solution(s):
    num = ['zero', 'one', 'two','three','four','five','six','seven','eight', 'nine']
    answer = ''
    for i, n in enumerate(num):
        if n in s:
            s = s.replace(n, str(i))
        answer = s
    return int(answer)