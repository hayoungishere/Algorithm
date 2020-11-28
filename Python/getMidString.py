'''
문제 : 가운데 글자 가져오기

접근 : 길이를 받아와서 가운데 글자를 가져오자
홀수 -> 한글자, 짝수 : 두글자
'''

def solution(s):
    answer = ''
    
    if len(s)%2 != 0 :
        answer = s[int(len(s)/2)]
    else:
        answer = s[int(len(s)/2)-1]+s[int(len(s)/2)]



    return answer


if __name__ == "__main__":
    s = 'abcsd'
    print(solution(s))