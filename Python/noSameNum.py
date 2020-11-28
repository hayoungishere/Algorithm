'''
문제 : 같은 숫자는 싫어
0부터 9까지로 이루어져 있는 배열이 주어졌을때 연속으로 나타나는 숫자는 하나를 제외하고 제거한 다음 반환하라
단, 원소들의 순서는 유지되어야한다.

접근: arr의 앞에서부터 보면서 answer의 마지막에 들어간 값과 같지 않으면 추가한다.

'''

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if(answer[len(answer)-1] != arr[i]): answer.append(arr[i])

    return answer


if __name__ == "__main__":
    arr = [1,1,3,3,0,1,1]
    print(solution(arr))