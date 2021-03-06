# Algorithm
Practice problem solving for coding interview

## Step 1. Asking
명확하지 않은 부분에 대해서 질문해라
그러다 보면 처음에 생각했던 것과는 아주 다른, 그러나 때로 좀 더 쉬운 문제를 풀어야 한다는 결론에 마주하게 될 수 있다.

## Step 2. Design Algorithm
고려해야하는 사항은 다음과 같다.
* 시간과 공간 복잡도는?
* 데이터가 많아지면 어떻게 되나?
* 내 설계가 다른 이슈들을 파생시키지 않는가? 일례로, 변형된 이진 탐색 트리를 만들었다면, 여러분의 설계가 기존의 삽입, 탐색, 삭제 시간에 영향을 미치지는 않는가?
* 다른 이슈나 한계점이 있다면, 적절한 타협안을 만들었나? 그 타협안이 최적으로 동작하지 않는 시나리오로는 무엇이 있나?
* 면접관이 데이터의 특징을 명시했다면 그 특징을 활용하였는가? 면접관이 그런 정보를 줄 때에는 이유가 있기 마련이다.

처음부터 완벽한 답안을 낼 필요는 없다.


[알고리즘 설계의 다섯 가지 접근법]
1. 예증(Examplify)
문제를 구성하는 특정한 사례들을 나열한다음 일반적 규칙을 유도해 낼 수 있는지 살펴본다.

2. 패턴 매칭(Pattern matching)
우선 풀어야 할 알고리즘이 어떤 문제와 유사했는지 살핀다. 그리고 그 문제의 답을 수정하여, 지금 풀어야 하는 문제에 적용할 알고리즘을 개발한다.

3. 단순화와 일반화
우선, 자료형이나 데이터 양과 같은 제약 조건을 변경한다. 그런 다음, 단순화된 버전의 문제를 풀고 알고리즘이 구해지면 최종적으로 문제를 일반화하여 구해진 알고리즘을 보다 복잡한 형태로 다듬어 간다.

4. 초기사례로부터의 확장
재귀문제애 사용해라.

5. 자료구조 브레인스토밍
일련의 자료구조를 차례차례 적용해 보고 해결되는지 보는 것.
ex. 입력을 받으면서 중간값을 찾아봐라
최소힙과 최대힙 두개를 사용하여 두 힙의 크기가 균일하게 유지해나가라.

## Step 3. Pseudo Code

## Step 4. Code

* 자료구조를 풍부히 활용해라.
    좋은 자료구조를 선택하거나 스스로 정의해서 사용함으로써 OOP 설계를 신경쓴다는 인상을 남겨라
* 코드를 복잡하게 보이도록 하지 마라

## Step 5. Test
문제를 발견한다면 바로 고치지 말고 오류가 발생한 부분을 생각해보고 수정해라

* 극단적인 경우를 생각해라
* 사용자 실수를 생각해라(ex. 입력이 Null인 경우)
* 일반적인 경우


## 좋아 보이는 코드는?
* 정확함 : 예상한 입력이든 예상못한 입력이든 코드는 정확히 동작해야한다.
* 효율성 : 점근적 효율성과 실용적 효율성을 모두 고려해라
* 단순성 : 100줄 보다는 10줄!
* 가독성 : 필요한 부분에는 주석을 달자!
* 관리가능성 : 다른 개발자도 쉽게 관리 가능한 코드여야 한다.

    
자료구조를 일반적으로 사용하라
적절한 코드 재사용
모듈화
유연하고 튼튼한 코드
오류검사 : "결국에는 오류 검사를 위한 코드를 추가할 것"이라는 태도를 보여라



#자료구조
1. 배열과 문자열
2. 연결 리스트
3. 스택과 큐
4. 트리와 그래프


 




출처 : Cracking the Coding Interview 150 Programming Questions and Solutions