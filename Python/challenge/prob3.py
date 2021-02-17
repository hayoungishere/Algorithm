'''
중학교 영어교사인 현미는 방학동안 영단어 암기 카드를 만들어서 학생들에게 돌려 보면서 익히도록 하려 합니다.
각 학생들은 한 장씩 뎡단어 카드를 만들어 1번 학생은 자신이 마는 카드를 2번 학생에게, 2번 학생은 자신이 만든 카드를 3번 학생에게, 즉 모든 학생들이
자신의 다음 번호의 학생에게 카드를 전달했습니다. 마지막 번호인 학생은 자신이 만든 카드를 1번 학생에게 전달했습니다.
그 후에는 이 카드에 적힌 단어를 암기하고 나서 또 같은 방식으로 카드를 전달했고, 한 바퀴를 모두 돌아 이미 자신이 암기한 카드가 돌아오면 전달을 종료했습니다.

이렇게 했더니, 모든 학생이 모든 카드를 회람할 수 있다는 ㅓㅈㅁ은 좋았지만, 집이 멀다든지 앞뒤 번호 학생과 잘 만나지 않는 경우가 있다든지해서 카드들이 한 바퀴 회람되는 데 걸리는 시간이 너무 길었습니다.
그래서 이번 학기에 현미는 아이디어 하나를 제시했습니다. 모든 학생들이 자신이 이번에 암기한 카드를 다음 번에 전달해 주고 싶은 학생을 한명씩 지정하여, 다음 번호의 학생이 아니라 자신이 지정한 학생에게 카드를 전달하기로 한 것입니다.
단, 카드를 전달하고 싶은 사람이 없다면 자신에게 돌아온 카드에 적힌 단어를 암기한 후 카드를 버리기로 했습니다.
도, 이미 한번 암기한 카드가 자신에게 다시 돌아오면 그 카드도 버리기로 했습니다.

예를 들어, 열 세명의 학생으로 이뤄진 학급에서 각 학생이 자신이 카드를 전달하고 싶은 학생을 지정한 표가 아래와 같다고 가정하겠습니다. 
학생들은 모두 번호로만 표시합니다. 아무에게도 카드를 전달하지 않을 학생은 0이 표기 되어있습니다.

각 학생이 만든 카드가 자신을 포함하여 몇 명에게 전달되어 영단어 암기에 활용될 수 있었는지를 동그라미 주위에 붉은 숫자로 표시했습니다.

각 학생이 만든 카드가 가능한 많은 학생들에게 회람되도록 하고 싶었던 현미는 한 가지 아이디어를 냈습니다. 가장 많은 학생들에게 회람된 카드를 작성한 학생에게 상을 주겠다는 것입니다.

각 학생이 자신이 만든 또는 받은 카드를 전달할 다음 학생의 번호가 담긴 배열 next_student가 매개변수로 주어질 때, 몇 번 학생이 만든 카드가 가장 많은 학생들에게 회람될지 return  하도록 solution 함수를 완성해라

[제한사항]
* next_student는 각 학생이 카드를 전달할 다른 학생의 번호를 나열한 배열이다.
    * 학생 수가 n명이라면, 학생들에게는 1번부터 n번까지 번호가 매겨져 있다.
    * next_student의 k번째 원소는 k번 학생이 카드를 전달할 다른 학생의 번호다.
* next_student의 길이는 1 이상 1,000,000 이하이다.
    * next_student의 길이가 n일때, 학생 수는 n 명이다.
    * next_student의 원소는 0 이상 (next_student의 길이) 이하인 정수이다.
    * next_student의 k번째 원소가 k인 경우(자기 자신을 다른 학생으로 지목한 경우)는 없다.
    * 원소가 0인 경우 그 학생은 자신이 만든 카드와 받은 카드 모두 다른 학생에게 전달하지 않는다.
'''

def solution(next_student):
    answer = 0
    print(next_student)
    return answer

if __name__ =="__main__":
    solution([[5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2]]) # 3
    solution([6, 10, 8, 5, 8, 10, 5, 1, 6, 7]) # 9