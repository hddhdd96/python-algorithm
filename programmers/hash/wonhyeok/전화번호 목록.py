def solution(phone_book):
    # ���̼� ����
    phone_book.sort(key=len)
    num_set = set()
    
    # �պ��� �߶󰡸� ���տ� �����ϴ��� Ȯ��
    for num in phone_book:
        for i in range(1,len(num)+1):
            if num[:i] in num_set:
                return False
        num_set.add(num)
    
    return True
