'''
문제 : 수박수박수

접근 : 홀수 => "박" 추가, 짝수 => "수"추가
'''


def solution(n):
    answer = ''
    
    for i in range(n):
        if( i%2 == 0 ) :
            answer +="수"
        else:
            answer += "박"

    return answer

