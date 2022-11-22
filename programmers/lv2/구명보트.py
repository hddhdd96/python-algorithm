from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    deq = deque(people)
    
    while deq:
        if len(deq) >= 2:
            if deq[0] + deq[-1] <= limit:
                deq.pop()
                deq.popleft()
                answer += 1
            elif deq[0] + deq[-1] > limit:
                answer += 1
                deq.pop()
        else:
            deq.pop()
            answer += 1
    return answer