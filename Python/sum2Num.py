'''
문제 : 두 정수 사이의 합
두 정수 a, b가 주어졌을때 a와 b 사이의 모든 정수의 합을 반환하라
단, a와 b의 대소관계는 정해져있지 않다
'''

def solution(s):
    answer = True
    if a > b:
        temp = a
        a = b
        b = temp
        
    for i in range(a,b+1):
        answer+=i
    return answer