'''
K번째 수
rray	               :  commands	                        :  return
[1, 5, 2, 6, 3, 7, 4]  :  [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	:  [5, 6, 3]

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

접근
array[i:j]를 가져와서 정렬한 다음 k번째 수를 찾자
'''

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        x = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(x[commands[i][2]-1])
        
    return answer