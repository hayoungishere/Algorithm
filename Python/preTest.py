'''
문제 : 모의고사
    일정한 패턴으로 문제를 찍는 3명의 점수 중 가장 높은 점수를 받은 사람을 반환하라
    단, 가장 높은 점수를 받은 사람이 여러명인 경우 맞힌 사람의 번호를 오름차순으로 정렬하여 반환하시오.

접근 :
    {1번: 맞춘개수, 2번 : 맞춘개수, 3번: 맞춘개수}
    딕셔너리를 '맞춘개수'로 정렬해서 비교한다

'''

def solution(answers):
    answer = []
    supo1 =[1,2,3,4,5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    i1,i2,i3 = 0,0,0
    count = [0,0,0]
    for a in answers:
        if(supo1[i1] == a): count[0]+=1
        if(supo2[i2] == a): count[1]+=1
        if(supo3[i3] == a): count[2]+=1
        i1+=1; i2+=1; i3+=1
        i1%=len(supo1); i2 %=len(supo2); i3 %= len(supo3)
    temp ={1:count[0], 2:count[1], 3:count[2]} # 맞춘 개수

    result = sorted(temp.items(), key=lambda x:x[1])
    
    answer.append(result[2][0])
    if(result[2][1]== result[1][1]): answer.append(result[1][0])
    if(result[2][1] == result[0][1]): answer.append(result[0][0])

    answer.sort()
    return answer



if __name__=="__main__":
    answers=[2,2,2,3,3,3]
    print(solution(answers))

