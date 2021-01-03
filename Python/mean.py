'''
문제 : 평균 구하기
   정수를 담고 있는 배열 arr의 평균값을 반환하라.

'''

def solution(arr):
    answer = 0
    for i in arr:
        answer +=i
    answer /=len(arr)
    return answer

if __name__=="__main__":
    print(solution([1,2,3,4]))
    print(solution([5,5]))