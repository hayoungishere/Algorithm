'''
문제 : 문자열 다루기 기본
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인하는 함수를 구현하라

접근 : 
문자열 -> 정수로 변환 시도를 했을때 Exception이 발생한다면 문자열 중간에 숫자가 아닌 문자가 포함되어있다는 의미이므로
False를 반환한다.
'''

def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False

    try :
        int(s)
    except:
        answer = False


    return answer

if __name__=="__main__":
    print(solution("a111"))
    print(solution("12345"))
    print(solution("1234"))