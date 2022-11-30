class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ') # 문자열 공백을 기준으로 리스트화
        for i in range(len(s)):
            s[i] = s[i][::-1] #문자열 뒤집기
        return ' '.join(s) #리스트를 문자열로