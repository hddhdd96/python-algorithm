from math import prod
 
def solution(clothes):
    dic = {}
    
    for _, kind in clothes:
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 2 #������ �Ʒ����� ���ϱ� ���� +1�� �ϹǷ�
 
    answer = prod(dic.values())-1
    
    return answer