#[Programmers] 프로그래머스 파이썬 > 땅따먹기
def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])): 
            #앞의 행에서 해당 열 제외 최대값 더하기 갱신
            land[i][j] += max(land[i-1][0:j] + land[i-1][j+1:])
    return max(land[-1])