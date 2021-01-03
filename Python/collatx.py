'''
문제 : 콜라츠 추측
    입력된 수가 짝수라면 2로 나누고 홀수면 3을 곱하고 1을 더한다.
    결과로 나온 수에 같은 작업을 1이 될때 까지 반복한다.
    이 작업을 몇 번이나 반복해야하는지 반환하는 함수를 작성하라.
    단, 위 작업을 500번 반복해도 1이 되지 않는다면 1을 반환하라.

'''

def solution(num):
    answer = 0
    while answer < 500:
        if num == 1: 
            break
        if num%2 == 0:
            num = num/2
        else:
            num = num*3 + 1
        answer+=1
    if answer ==500:
        answer = -1
    return answer

if __name__=="__main__":
    print(solution(6))
    print(solution(16))
    print(solution(626331))