'''
정수 배열 numbers가 주어지면 서로 다른 인덱스에 있는 두 수를 뽑아 더해서 만들수 있는 모든 수를
배열에 오름차순으로 담아 반환하라.

접근 : set 자료형을 사용해서 unique를 유지하자
'''
def solution(numbers):
    answer = []
    s = set()
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            s.add(numbers[i]+numbers[j])
    
    
    for item in s:
        answer.append(item)
    
    answer.sort()
    return answer

