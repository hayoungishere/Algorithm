'''
문제 : 크레인 인형뽑기 게임

접근 : 인형의 위치별로 Queue를 생성해서 먼저들어간 인형을 뽑기 완료 통에 옮긴후
뽑기 완료 통의 마지막 두개의 인형을 비교해서
같으면 완료통에서 제거 및 제거된 인형의 수를 2개 증가시킨다.
'''

def solution(board, moves):
    answer = 0
    q=[]

    for i in range(len(board[0])):
        q.append([])

    for b in board:
        for idx in range(len(b)):
            if b[idx] != 0:
                q[idx].append(b[idx])


    out = []
    tail = 0
    for i in moves:
        if len(q[i-1]) > 0:
            out.append(q[i-1][0])
            del q[i-1][0]
        size = len(out)
        if size > 1 :
            if out[size-1] == out[size-2]:
                del out[size-1]
                del out[size-2]
                answer+=2

    return answer


if __name__=="__main__":

    b=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    m=[1,5,3,5,1,2,1,4]
    print(solution(b,m))