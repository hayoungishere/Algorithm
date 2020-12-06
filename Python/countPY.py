'''
문제 : 문자열 내 p와 y의 개수
p와 y의 개수가 같으면 True, 다르면 False를 반환
문자열에 둘다 없는 경우는 True를 반환한다.

접근 : 대소문자를 구별하지 않기때문에 모두 소문자로 치환후 개수 카운트
'''

def solution(s):
    answer = True
    p=0
    y=0
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    s = s.lower()
    print(s)
    
    for i in range(len(s)):
        if (s[i] == 'y'):
            y+=1
        if (s[i] == 'p'):
            p+=1
    
    if(p != y) :
        answer = False

    return answer