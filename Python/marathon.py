'''
문제 : 완주하지 못한 선수

'''
def solution(participant, completion):
    answer=''

    participant.sort()
    completion.sort()

    print(participant, completion)

    i = 0
    for p in participant:
        if(p != completion[i]):
            answer = p
            break
        i+=1
    return answer


if __name__=="__main__":
    participant=["leo","kiki","eden"]
    completion=["eden","leo"]
    print(solution(participant,completion))