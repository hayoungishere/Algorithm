'''
문제 : a배열과 b배열의 내적을 구하라
'''

def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer