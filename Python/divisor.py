'''
문제: 나누어 떨어지는 숫자 배열
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

접근: divisor로 나눠 떨어지는 수를 answer에 저장한 다음
리턴할때 정렬해서 리턴!
'''
def solution(arr, divisor):
    answer = []
    
    for a in arr:
        if(a % divisor == 0):
            answer.append(a)
    
    
    if(len(answer) == 0):
        answer.append(-1)
    answer = sorted(answer)
    return answer