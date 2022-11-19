def solution(brown, yellow):
    S = brown + yellow
    for y in range(3, S//2):
        if S % y == 0:
            x = S // y
            if (x-2) * (y-2) == yellow:
                return [x, y]