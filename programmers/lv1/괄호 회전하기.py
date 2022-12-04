def solution(s):
    answer = 0
    l = len(s)
    for i in range(l):
        temp = list(s[i:] + s[:i])
        stack = []
        while temp:
            p = temp.pop()
            if len(stack) == 0:
                stack.append(p)
            else:
                if p == '[' and stack[-1] == ']':
                    stack.pop()
                elif p == '{' and stack[-1] == '}':
                    stack.pop()
                elif p == '(' and stack[-1] == ')':
                    stack.pop()
                else:
                    stack.append(p)
        if len(stack) == 0:
            answer += 1
                
    return answer