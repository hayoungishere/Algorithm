'''
문제 : 문자열을 정수로 바꾸기
'''

def solution(s):
    answer = 0

    if s[0] == '+':
        answer = int(s[1:])
    elif s[0] == '-':
        answer = -int(s[1:])
    else:
        answer = int(s)


    return answer


if __name__=="__main__":

    print(solution("-1234"))
    print(solution("5555"))