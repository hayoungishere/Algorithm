'''
문제 : 예산
접근 : 적은 예산을 가진 부서별로 예산 우선 할당.
'''
def solution(d, budget):
    answer = 0
    d=sorted(d)
    i=0
    while budget>0:
        if i>=len(d): break
        budget-=d[i]
        i+=1
    if budget>=0:
        answer = i
    else:
        answer = i-1
    return answer