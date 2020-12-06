'''
문제 : 소수 찾기
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

접근
2부터 확인한다. 이때 i가 소수인 경우 i의 배수는 모두 소수가 아니기 떄문에
이를 미리 체크하고 넘어갈 수 있게끔한다.
'''

def solution(n):
    answer = 0
    
    temp = [1]*(n+1)
    for i in range(2,n+1):
        if(temp[i] == 1):
            temp[i] = 0
            answer += 1
            j=2
            
            while(i*j <= n):
                temp[i*j] = 0
                j+=1
            
        
    return answer